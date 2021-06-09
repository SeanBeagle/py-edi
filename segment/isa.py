class ISA:
    elements = []
    segment = ''
    element_separator = ''

    def __init__(self, segment: str, element_separator: str):
        self.segment = segment
        self.element_separator = element_separator
        self.elements = segment.split(element_separator)

        self.validate_segment()

    def __repr__(self):
        return f'ISA("{self.segment}")'

    def validate_segment(self):
        assert(self.segment.startswith('ISA'))
        assert(self.element_separator == self.segment[3])
