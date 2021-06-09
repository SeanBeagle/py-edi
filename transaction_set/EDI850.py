class Segment:
    id = str()
    required = bool()
    max_use = str()

    def __init__(self, id, max_use, required=True):
        self.id = id
        self.required = required
        self.max_use = max_use


class Loop:
    id = str()
    max_use = str()
    segments = list()

    def __init__(self, id, max_use, segments):
        self.id = id
        self.segments = segments
        self.max_use = max_use


EDI850_transaction_set = \
    {
        'Header': [
                Segment('ST', max_use='1', required=True),
                Segment('BEG', max_use='1', required=True),
                Segment('CUR', max_use='1', required=False),
                Segment('REF', max_use='>1', required=False),
                Segment('PER', max_use='3', required=False),
                Segment('TAX', max_use='>1', required=False),
                Segment('FOB', max_use='>1', required=False),
                Segment('CTP', max_use='>1', required=False),
                Segment('PAM', max_use='10', required=False),
                Segment('CSH', max_use='5', required=False),
                Segment('TC2', max_use='>1', required=False),
                Loop('SAC', max_use='25',
                     segments=[Segment('SAC', max_use=1, required=False),
                               Segment('CUR', max_use=1, required=False)]),
                Segment('ITD', max_use='>1', required=False),
                Segment('DIS', max_use='20', required=False),
                Segment('INC', max_use='1', required=False),
                Segment('DTM', max_use='10', required=False),
                Segment('LDT', max_use='12', required=False),
                Segment('LIN', max_use='5', required=False),
                Segment('SI', max_use='>1', required=False),
                Segment('PID', max_use='200', required=False),
                Segment('MEA', max_use='40', required=False),
                Segment('PWK', max_use='25', required=False),
                Segment('PKG', max_use='200', required=False),
                Segment('TD1', max_use='2', required=False),
                Segment('TD5', max_use='12', required=False),
                Segment('TD3', max_use='12', required=False),
                Segment('TD4', max_use='5', required=False),
                Segment('MAN', max_use='10', required=False),
                Segment('PCT', max_use='>1', required=False),
                Segment('CTB', max_use='5', required=False),
                Segment('TXI', max_use='>1', required=False),
                Loop('AMT', max_use='>1',
                     segments=[Segment('AMT', max_use='1', required=False),
                               Segment('REF', max_use='>1', required=False),
                               Segment('DTM', max_use='1', required=False),
                               Segment('PCT', max_use='>1', required=False),
                               Loop('AMT/FA1', max_use='>1',
                                    segments=[Segment('FA1', max_use='1', required=False),
                                              Segment('FA2', max_use='>1', required=True)])]),
                Loop('N9', max_use='1000',
                     segments=[Segment('N9', max_use='1', required=False),
                               Segment('DTM', max_use='>1', required=False),
                               Segment('MSG', max_use='1000', required=False)]),
                Loop('N1', max_use='200',
                     segments=[Segment('N1', max_use='1'),
                               Segment('N2', max_use='2'),
                               Segment('N3', max_use='2'),
                               Segment('N4', max_use='>1'),
                               Segment('NX2', max_use='>1'),
                               Segment('REF', max_use='12'),
                               Segment('PER', max_use='>1'),
                               Segment('SI', max_use='>1'),
                               Segment('FOB', max_use='1'),
                               Segment('TD1', max_use='2'),
                               Segment('TD5', max_use='12'),
                               Segment('TD3', max_use='12'),
                               Segment('TD4', max_use='5'),
                               Segment('PKG', max_use='200')]),
                Loop('LM', max_use='>1',
                     segments=[Segment('LM', max_use='1', required=False),
                               Segment('LQ', max_use='>1', required=False)]),
                Loop('SPI', max_use='>1',
                     segments=[Segment('SPI', max_use='1', required=False),
                               Segment('REF', max_use='5', required=False),
                               Segment('DTM', max_use='5', required=False),
                               Segment('MSG', max_use='50', required=False),
                               Loop('SPI/N1', max_use='20',
                                    segments=[Segment('N1', max_use='1', required=False),
                                              Segment('N2', max_use='2', required=False),
                                              Segment('N3', max_use='2', required=False),
                                              Segment('N4', max_use='1', required=False),
                                              Segment('REF', max_use='20', required=False),
                                              Segment('G61', max_use='1', required=False),
                                              Segment('MSG', max_use='50', required=False)]),
                               Loop('SPI/CB1', max_use='>1',
                                    segments=[Segment('CB1', max_use='1', required=False),
                                              Segment('REF', max_use='20', required=False),
                                              Segment('DTM', max_use='5', required=False),
                                              Segment('LDT', max_use='1', required=False),
                                              Segment('MSG', max_use='50', required=False)])]),
                Loop('ADV', max_use='>1',
                     segments=[Segment('ADV', max_use='1', required=False),
                               Segment('DTM', max_use='>1', required=False),
                               Segment('MTX', max_use='>1', required=False)])
        ],
        'Detail':
            [
                Loop('PO1', max_use='100000',
                     segments=[
                         Segment('PO1', max_use='1', required=True),
                         Segment('LIN', max_use='>1', required=False),
                         Segment('SI', max_use='>1', required=False),
                         Segment('CUR', max_use='1', required=False),
                         Segment('CN1', max_use='1', required=False),
                         Segment('PO3', max_use='25', required=False)]
                         )
            ],
        'Summary':
            [

            ]

    }





class EDI850:
    id = '850'
    name = 'Purchase Order'
    functional_group = 'PO'
    version = '004010UCS'

    headers = [
        {
            'SegmentID': 'ST',
            'RequirementDesignator': 'M',
            'MaxUse': '1'
        },
        {
            'SegmentID': 'BEG',
            'RequirementDesignator': 'M',
            'MaxUse': '1'
        }
    ]
