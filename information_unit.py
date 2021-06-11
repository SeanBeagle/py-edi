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
    _segments = list()
    _segment_terminator = str()

    def __init__(self, file):
        self._segment_terminator = EdiParser.get_segment_terminator(file)
        self._segments = EdiParser.get_segments(file, self.segment_terminator)

    def __str__(self):
        return "Transaction Set"

    def __repr__(self):
        return f'{self.__class__.__name__}({self[:10]}...)'

    def __len__(self):
        return len(self.segments)

    @property
    def segments(self):
        return self._segments

    @property
    def segment_terminator(self):
        return self._segment_terminator


class EdiParser:
    @staticmethod
    def get_segment_terminator(file):
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
    def get_element_separator(file):
        with open(file, 'r') as fh:
            string = fh.read(4)
            if string.startswith('ISA'):
                return string[3]
            else:
                raise Exception('File does not start with ISA')

    @staticmethod
    def get_segments(file, segment_terminator):
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
                if not char:
                    segments += segment
        return segments

    @staticmethod
    def get_data_elements(line, data_element_separator):
        return [DataElement(item) for item in line.split(data_element_separator)][1:]

    @staticmethod
    def get_segment_id(line, data_element_separator):
        return line[:line.find(data_element_separator)]
