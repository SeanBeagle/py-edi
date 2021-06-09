from segment.isa import ISA


class EdiParser:
    data = {}
    segments = []
    _byte = None
    _position = -1
    segment_terminator = None
    element_separator = None
    fh = None

    def parse(self, file):
        with open(file, 'r') as self.fh:
            self.data['ISA'] = self._read_isa()
            self.segment_terminator = self._read_segment_terminator()
            self.data['GS'] = self._read_gs()
            self.data['ISA'] = ISA(self.data['ISA'], self.element_separator)

        print(self.data['ISA'])
        print(f"Element Separator = '{self.element_separator}'")
        print(f"Segment Terminator = '{self.segment_terminator}'")

    def _read_isa(self):
        segment = ''
        while self._read_byte():
            segment += self._byte
            if self._byte == '>':
                if segment.startswith('ISA'):
                    self.element_separator = segment[3]
                return segment

    def _read_gs(self):
        segment = ''
        while self._read_byte():
            if self._byte != self.segment_terminator:
                segment += self._byte
            else:
                return segment

    def _read_segment_terminator(self):
        terminator = ''
        while self._read_byte():
            if self._byte == 'G':
                return terminator
            else:
                terminator += self._byte

    def _read_byte(self):
        self._byte = self.fh.read(1)
        self._position += 1
        return self._byte