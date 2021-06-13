from data_dictionary.segments import segment_definitions


class Element:
    """Data Element.

    The data element is the smallest information unit in the information structure. A data element may be a single
    character code, a series of characters constituting a literal description or a numeric quantity. The data element
    has two primary attributes, length and type. The length characteristic of a data element may be fixed or variable.
    Each data element is identified by a number used for reference in the Data Element Dictionary.

    Attributes:
        number (str):
            Data elements are assigned a unique reference number. This reference number is used in the diagrams of all
            segments to aid in locating the data element definitions and specifications. For example, Data Element 93
            is ‘‘Name’’.
        value (str): The data in the element
    """
    _number = str  # Data Element Reference Number
    _value = str

    @property
    def number(self):
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
    """Segment.

    A segment is the intermediate unit of information in a transaction set. Segments consist of logically related data
    elements in a defined sequence, with a data element separator preceding each data element and a segment terminator
    character following the last data element. Segments have a predetermined segment identifier that comprises the first
    characters of the segment. When segments are combined to form a transaction set, their use in the transaction set is
    defined by a segment requirement designator and a segment sequence. Some segments may be repeated, and groups of
    segments may be repeated as loops.

    Properties:
        id (str):
            Each segment has a unique identifier consisting of the combination of two or three alpha/numeric characters.
            The segment identifiers are specified in the first positions of each individual segment. The segment
            identifier is not a data element.
        value (str):
        element_separator (str):
            An asterisk (*) separator precedes each data element within a segment. When there is no data being
            transmitted for a defined element, the asterisk is transmit- ted to preserve the data element sequence.
            Transmission of the data segment terminator code indicates that all remaining non-transmitted elements in
            the segment are blank.
        elements (list): List of Element objects
    """

    _id = str
    _value = str
    _element_separator = str  # Data Element Separator
    _elements = list

    @property
    def id(self):
        return self._id

    @property
    def value(self):
        return self._value

    @property
    def element_separator(self):
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
    """Transaction Set.

    A transaction set is composed of a specific group of segments that represent a common business document (for
    example, a purchase order or an invoice). Each transaction set consists of the transaction set header (ST) as the
    first segment and contains at least one segment before the transaction set trailer (SE).
    """

    _header = Segment  # Transaction Set Header (ST)
    _trailer = Segment  # Transaction Set Trailer (SE)
    _segments = list

    @property
    def header(self):
        return self._header

    @property
    def trailer(self):
        return self._trailer

    @property
    def segments(self):
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
    """Functional Group.
    A functional group is composed of one or more transaction sets of the same or similar types, enclosed by functional
    group header (GS) and functional group trailer (GE) segments.
    """

    _header = Segment  # Functional Group Header (GS)
    _trailer = Segment  # Functional Group Header (GE)
    _transaction_sets = list

    @property
    def header(self):
        return self._header

    @property
    def trailer(self):
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

    Properties:
        segment_terminator (str):
            Each segment is terminated by a special character inserted in the segment immediately following the last
            data element to be transmitted. The non-printable tilde (~) character is used to terminate segments in UCS
            transmissions.
    """
    _header = Segment  # Interchange Control Header (ISA)
    _trailer = Segment  # Interchange Control Trailer (IEA)
    _functional_groups = list
    _segment_terminator = str

    @property
    def header(self):
        return self._header

    @property
    def trailer(self):
        return self._trailer

    @property
    def functional_groups(self):
        return self._functional_groups

    @property
    def segment_terminator(self):
        return self._segment_terminator

    def __init__(self, file):
        self._segment_terminator = EdiParser.get_segment_terminator(file)
        segments = EdiParser.get_segments(file, self.segment_terminator)
        self._header, self._trailer = segments[0], segments[-1]
        SegmentValidator.validate_isa(self.header)
        self._functional_groups = EdiParser.get_functional_groups(segments[1: -1])

    def __repr__(self):
        return f'{self.__class__.__name__}(FunctionalGroups={len(self)})'

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self.functional_groups)


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
    def validate_isa(segment: Segment):
        assert segment.id == 'ISA', ValueError('Expected ISA')
        element_definitions = segment_definitions.get('ISA').get('elements')
        for data_element, definition in zip(segment.elements, element_definitions):
            DataElementValidator.validate(data_element, definition)

    @staticmethod
    def validate_segment(segment: Segment):
        segment_definition = segment_definitions.get(segment.id)
        if segment_definition:
            element_definitions = segment_definition.get('elements')
            for data_element, definition in zip(segment.elements, element_definitions):
                DataElementValidator.validate(data_element, definition)
            print(f'Validated: {segment.id}')