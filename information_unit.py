class DataElement:
    _string = str()

    def __init__(self, string):
        self._string = string

    def __str__(self):
        return self._string

    def __repr__(self):
        return f'{self.__class__.__name__}({self})'

    @property
    def string(self):
        return self._string


class Segment:
    _id = str()
    _line = str()
    _data_element_separator = str()
    _data_elements = list()

    def __init__(self, line, data_element_separator='*'):
        self._line = line
        self._data_element_separator = data_element_separator
        self._data_elements = EdiParser.get_data_elements(line, data_element_separator)
        self._id = EdiParser.get_segment_id(line, data_element_separator)

    def __str__(self):
        return self._line

    def __repr__(self):
        return {f'{self.__class__.__name__}({self._id})'}

    def __len__(self):
        return len(self.data_elements)

    @property
    def id(self):
        return self._id

    @property
    def line(self):
        return self._line

    @property
    def data_elements(self):
        return self._data_elements

    @property
    def data_element_separator(self):
        return self._data_element_separator


class TransactionSet:
    _segments = list
    _header = Segment
    _trailer = Segment

    def __init__(self, segments):
        self._header, self._trailer = segments[0], segments[-1]
        self._segments = segments[1: -1]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'{self.__class__.__name__}(Segments={len(self)})'

    def __len__(self):
        return len(self.segments)

    @property
    def segments(self):
        return self._segments

    @property
    def header(self):
        return self._header

    @property
    def trailer(self):
        return self._trailer


class TransmissionEnvelope:
    _header = Segment  # Interchange Control Header (ISA)
    _trailer = Segment  # Interchange Control Trailer (IEA)
    _functional_groups = list
    _segment_terminator = str

    def __init__(self, file):
        self._segment_terminator = EdiParser.get_segment_terminator(file)
        segments = EdiParser.get_segments(file, self.segment_terminator)
        self._header, self._trailer = segments[0], segments[-1]
        self._functional_groups = EdiParser.get_functional_groups(segments[1: -1])

    def __repr__(self):
        return f'{self.__class__.__name__}(FunctionalGroups={len(self)})'

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self.functional_groups)

    @property
    def segment_terminator(self):
        return self._segment_terminator

    @property
    def header(self):
        return self._header

    @property
    def trailer(self):
        return self._trailer

    @property
    def functional_groups(self):
        return self._functional_groups


    """
    [ISA] [GS] [ST]               [SE] [GE] [IEA]
    |    |     |__TransactionSet__|    |    |
    |    |__FunctionalGroup____________|    |
    |__TransmissionEnvelope_________________|

    """

class FunctionalGroup:
    _header = Segment  # Functional Group Header (GS)
    _trailer = Segment  # Functional Group Header (GE)
    _transaction_sets = list

    def __init__(self, segments: list):
        self._header, self._trailer = segments[0], segments[-1]
        self._transaction_sets = EdiParser.get_transaction_sets(segments[1: -1])

    def __repr__(self):
        return f'{self.__class__.__name__}(TransactionSets={len(self)})'

    def __len__(self):
        return len(self.transaction_sets)

    @property
    def header(self):
        return self._header

    @property
    def trailer(self):
        return self._trailer

    @property
    def transaction_sets(self):
        return self._transaction_sets


class EdiParser:
    @staticmethod
    def get_segment_terminator(file: str):
        terminator = None
        with open(file, 'r') as fh:
            char = fh.read(1)
            while char:
                if char == '>':
                    terminator = fh.read(1)
                elif terminator and char == 'G':
                    return terminator
                char = fh.read(1)

    @staticmethod
    def get_element_separator(file: str):
        with open(file, 'r') as fh:
            string = fh.read(4)
            if string.startswith('ISA'):
                return string[3]
            else:
                raise Exception('File does not start with ISA')

    @staticmethod
    def get_segments(file: str, segment_terminator: str):
        segments = []
        with open(file, 'r') as fh:
            segment = ''
            char = fh.read(1)
            while char:
                if char == segment_terminator:
                    segments.append(Segment(segment))
                    segment = ''
                else:
                    segment += char
                char = fh.read(1)
        return segments

    @staticmethod
    def get_data_elements(line: str, data_element_separator: str):
        return [DataElement(item) for item in line.split(data_element_separator)][1:]

    @staticmethod
    def get_segment_id(line: str, data_element_separator: str):
        return line[:line.find(data_element_separator)]

    @staticmethod
    def get_functional_groups(segments: list):
        functional_groups = []
        fg = []
        for segment in segments:
            if segment.id == 'GE':
                fg.append(segment)
                functional_groups.append(FunctionalGroup(fg))
                fg = []
            elif not fg and segment.id != 'GS':
                raise Exception(f'Expecting GS segment not {segment.id}')
            else:
                fg.append(segment)
        if fg:
            raise Exception(f'Extra segments not inside functional group: {fg}')

        return functional_groups

    @staticmethod
    def get_transaction_sets(segments: list):
        transmission_sets = []
        ts = []
        for segment in segments:
            if segment.id == 'SE':
                ts.append(segment)
                transmission_sets.append(TransactionSet(ts))
                ts = []
            elif not ts and segment.id != 'ST':
                raise Exception(f'Expecting ST segment not {segment.id}')
            else:
                ts.append(segment)
        if ts:
            raise Exception(f'Extra segments not inside functional group: {ts}')

        return transmission_sets

