from data_dictionary.segments import segment_definitions


class Element:
    """The smallest information unit in the information structure.

    A data element may be a single character code, a series of characters constituting a literal description or a
    numeric quantity. The data element has two primary attributes, length and type. The length characteristic of a data
    element may be fixed or variable. Each data element is identified by a number used for reference in the Data Element
    Dictionary.
    """
    _number = str  # Data Element Reference Number
    _value = str

    @property
    def number(self):
        """Unique reference number assigned to the data element"""
        return self._number

    @property
    def value(self):
        return self._value

    def __init__(self, value, number=None):
        self._value = value
        self._number = number

    def __str__(self):
        return self._value

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.value}", number="{self.number}")'

    def __len__(self):
        return len(self.value)


class Segment:
    """The intermediate unit of information in a transaction set.

    Segments consist of logically related data elements in a defined sequence, with a data element separator preceding
    each data element and a segment terminator character following the last data element. Segments have a predetermined
    segment identifier that comprises the first characters of the segment. When segments are combined to form a
    transaction set, their use in the transaction set is defined by a segment requirement designator and a segment
    sequence. Some segments may be repeated, and groups of segments may be repeated as loops.
    """

    _id = str
    _value = str
    _element_separator = str  # Data Element Separator
    _elements = list

    @property
    def id(self):
        """Unique identifier consisting of two or three alpha/numeric characters"""
        return self._id

    @property
    def value(self):
        return self._value

    @property
    def element_separator(self):
        """Precedes each data element within a segment. Usually an asterisk (*)"""
        return self._data_element_separator

    @property
    def elements(self):
        return self._elements

    def __init__(self, value, separator='*'):
        self._value = value
        self._data_element_separator = separator
        self._id = EdiParser.get_segment_id(value, separator)
        self._elements = EdiParser.get_data_elements(value, separator, self.id)
        SegmentValidator.validate_segment(self)

    def __str__(self):
        return self.value

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.value}", separator="{self.element_separator}")'

    def __len__(self):
        return len(self.elements)


class TransactionSet:
    """Composed of a specific group of segments that represent a common business document.

    Each transaction set consists of the transaction set header (ST) as the first segment and contains at least one
    segment before the transaction set trailer (SE).
    """

    _header = Segment
    _trailer = Segment
    _segments = list

    @property
    def header(self):
        """Segment with id='ST'"""
        return self._header

    @property
    def trailer(self):
        """Segment with id='SE'"""
        return self._trailer

    @property
    def segments(self):
        """List of segments that belong to the transaction set"""
        return self._segments

    def __init__(self, segments):
        self._header, self._trailer = segments[0], segments[-1]
        self._segments = segments[1: -1]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'{self.__class__.__name__}(Segments={len(self)})'

    def __len__(self):
        return len(self.segments)


class FunctionalGroup:
    """Composed of one or more transaction sets of the same or similar types.

    Enclosed by functional group header (GS) and functional group trailer (GE) segments.
    """

    _header = Segment
    _trailer = Segment
    _transaction_sets = list

    @property
    def header(self):
        """Segment with id='GS'"""
        return self._header

    @property
    def trailer(self):
        """Segment with id='GE'"""
        return self._trailer

    @property
    def transaction_sets(self):
        return self._transaction_sets

    def __init__(self, segments: list):
        self._header, self._trailer = segments[0], segments[-1]
        self._transaction_sets = EdiParser.get_transaction_sets(segments[1: -1])

    def __repr__(self):
        return f'{self.__class__.__name__}(TransactionSets={len(self)})'

    def __len__(self):
        return len(self.transaction_sets)


class Interchange:
    """Interchange Envelope.

    TODO(sbeagle): describe
    """
    _header = Segment
    _trailer = Segment
    _functional_groups = list
    _segment_terminator = str

    def __init__(self, file):
        self._segment_terminator = EdiParser.get_segment_terminator(file)
        segments = EdiParser.get_segments(file, self.segment_terminator)
        self._header, self._trailer = segments[0], segments[-1]
        SegmentValidator.validate_interchange_envelope(self.header, self.trailer)
        self._functional_groups = EdiParser.get_functional_groups(segments[1: -1])

    def __repr__(self):
        return f'{self.__class__.__name__}(FunctionalGroups={len(self)})'

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self.functional_groups)

    @property
    def header(self):
        """Segment with id='ISA'"""
        return self._header

    @property
    def trailer(self):
        """Segment with id='IEA'"""
        return self._trailer

    @property
    def functional_groups(self):
        """List of FunctionalGroup objects that belong to this Interchange"""
        return self._functional_groups

    @property
    def segment_terminator(self):
        """ Special character that terminates each segment. Usually tilde (~) or newline (\n) character"""
        return self._segment_terminator


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
    def get_data_elements(line: str, data_element_separator: str, segment_id: str = None):
        items = line.split(data_element_separator)[1:]
        elements = []
        definition = segment_definitions.get(segment_id)
        if definition:
            element_definitions = definition.get('elements')
            for i, item in enumerate(items):
                reference_number = element_definitions[i].get('ReferenceNumber')
                elements.append(Element(item, reference_number))
        else:
            for item in items:
                elements.append(Element(item))
        return elements

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


class DataElementValidator:
    @classmethod
    def validate(cls, element: Element, rules: dict):
        min_length = rules.get('length')[0]
        max_length = rules.get('length')[1]

        cls.check_length(element, min_length, max_length)
        return True

    @staticmethod
    def check_length(element: Element, min_length: int, max_length: int):
        if min_length <= len(element) <= max_length:
            return True
        elif min_length == max_length:
            raise ValueError(f'Length of "{element}": {len(element)} is not {min_length}')
        if not min_length+10 <= len(element) <= max_length+10:
            raise ValueError(f'Length of "{element}": {len(element)} is not between {min_length}-{max_length+1}')


class SegmentValidator:
    @staticmethod
    def validate_interchange_envelope(header: Segment, trailer: Segment):
        assert header.id == 'ISA', ValueError(f'Expected ISA, not {header.id}')
        assert trailer.id == 'IEA', ValueError(f'Expected IEA, not {header.id}')

        header_element_definitions = segment_definitions.get('ISA').get('elements')
        for data_element, definition in zip(header.elements, header_element_definitions):
            DataElementValidator.validate(data_element, definition)

        trailer_element_definitions = segment_definitions.get('IEA').get('elements')
        for data_element, definition in zip(trailer.elements, trailer_element_definitions):
            DataElementValidator.validate(data_element, definition)

    @staticmethod
    def validate_segment(segment: Segment):
        segment_definition = segment_definitions.get(segment.id)
        if segment_definition:
            element_definitions = segment_definition.get('elements')
            for data_element, definition in zip(segment.elements, element_definitions):
                DataElementValidator.validate(data_element, definition)
            print(f'Validated: {segment.id}')