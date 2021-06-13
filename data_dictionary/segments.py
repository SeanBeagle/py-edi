ISA = {
    'id': 'ISA',
    'type': 'Control Segment',
    'name': 'Interchange Control Header',
    'purpose': 'To start and identify an interchange of zero or more functional groups and interchange-related control segments',
    'elements': [
        {
            'ReferenceDesignator': 'ISA01',
            'ReferenceNumber': 'I01',
            'Name': 'Authorization Information Qualifier',
            'RequirementDesignator': 'M',
            'type': 'ID',
            'length': [2, 2]
        },
        {
            'ReferenceDesignator': 'ISA02',
            'ReferenceNumber': 'I02',
            'Name': 'Authorization Information',
            'RequirementDesignator': 'M',
            'type': 'AN',
            'length': [10, 10]
        },
        {
            'ReferenceDesignator': 'ISA03',
            'ReferenceNumber': 'I03',
            'Name': 'Security Information Qualifier',
            'RequirementDesignator': 'M',
            'type': 'ID',
            'length': [2, 2]
        },
        {
            'ReferenceDesignator': 'ISA04',
            'ReferenceNumber': 'I04',
            'Name': 'Security Information',
            'RequirementDesignator': 'M',
            'type': 'AN',
            'length': [10, 10]
        },
        {
            'ReferenceDesignator': 'ISA05',
            'ReferenceNumber': 'I05',
            'Name': 'Interchange ID Qualifier',
            'RequirementDesignator': 'M',
            'type': 'ID',
            'length': [2, 2]
        },
        {
            'ReferenceDesignator': 'ISA06',
            'ReferenceNumber': 'I06',
            'Name': 'Interchange Sender ID',
            'RequirementDesignator': 'M',
            'type': 'AN',
            'length': [15, 15]
        },
        {
            'ReferenceDesignator': 'ISA07',
            'ReferenceNumber': 'I05',  # I05
            'Name': 'Interchange ID Qualifier',
            'RequirementDesignator': 'M',
            'type': 'ID',
            'length': [2, 2]
        },
        {
            'ReferenceDesignator': 'ISA08',
            'ReferenceNumber': 'I07',  # I07
            'Name': 'Interchange Receiver ID',
            'RequirementDesignator': 'M',
            'type': 'AN',
            'length': [15, 15]
        },
        {
            'ReferenceDesignator': 'ISA09',
            'ReferenceNumber': 'I08',  # I08
            'Name': 'Interchange Date',
            'RequirementDesignator': 'M',
            'type': 'DT',
            'length': [6, 6]
        },
        {
            'ReferenceDesignator': 'ISA10',
            'ReferenceNumber': 'I09',  # I09
            'Name': 'Interchange Time',
            'RequirementDesignator': 'M',
            'type': 'TM',
            'length': [4, 4]
        },
        {
            'ReferenceDesignator': 'ISA11',
            'ReferenceNumber': 'I10',  # I10
            'Name': 'Interchange Control Standards Identifier',
            'RequirementDesignator': 'M',
            'type': 'ID',
            'length': [1, 1]
        },
        {
            'ReferenceDesignator': 'ISA12',
            'ReferenceNumber': 'I11',  # I11
            'Name': 'Interchange Control Version Number',
            'RequirementDesignator': 'M',
            'type': 'ID',
            'length': [5, 5]
        },
        {
            'ReferenceDesignator': 'ISA13',
            'ReferenceNumber': 'I12',  # I12
            'Name': 'Interchange Control Number',
            'RequirementDesignator': 'M',
            'type': 'N0',
            'length': [9, 9]
        },
        {
            'ReferenceDesignator': 'ISA14',
            'ReferenceNumber': 'I13',  # I13
            'Name': 'Acknowledgment Requested',
            'RequirementDesignator': 'M',
            'type': 'ID',
            'length': [1, 1]
        },
        {
            'ReferenceDesignator': 'ISA15',
            'ReferenceNumber': 'I14',
            'Name': 'Usage Indicator',
            'RequirementDesignator': 'M',
            'type': 'ID',
            'length': [1, 1]
        },
        {
            'ReferenceDesignator': 'ISA16',
            'ReferenceNumber': 'I15',  # I15
            'Name': 'Component Element Separator',
            'RequirementDesignator': 'M',
            'type': None,
            'length': [1, 1]
        }
    ]
}

IEA = {
    'id': 'IEA',
    'name': 'Interchange Control Trailer',
    'type': 'Control Segment',
    'purpose': 'To define the end of an interchange of zero or more functional groups and interchange-related control segments',
    'elements': [
        {
            'ReferenceDesignator': 'IEA01',
            'ReferenceNumber': 'I16',
            'Name': 'Number of Included Functional Groups',
            'RequirementDesignator': 'M',
            'type': 'N0',
            'length': [1, 5]
        },
        {
            'ReferenceDesignator': 'IEA02',
            'ReferenceNumber': 'I12',
            'Name': 'Interchange Control Number',
            'RequirementDesignator': 'M',
            'type': 'N0',
            'length': [9, 9]
        }
    ]
}

GS = {
    'id': 'GS',
    'name': 'Functional Group Header',
    'type': 'Control Segment',
    'purpose': 'To indicate the beginning of a functional group and to provide control information',
    'elements': [
        {
            'ReferenceDesignator': 'GS01',
            'ReferenceNumber': '479',
            'Name': 'Number of Included Functional Groups',
            'RequirementDesignator': 'M',
            'type': 'ID',
            'length': [2, 2]
        },
        {
            'ReferenceDesignator': 'GS02',
            'ReferenceNumber': '142',
            'Name': 'Application Sender’s Code',
            'RequirementDesignator': 'M',
            'type': 'AN',
            'length': [2, 15]
        },
        {
            'ReferenceDesignator': 'GS03',
            'ReferenceNumber': '124',
            'Name': 'Application Receiver’s Code',
            'RequirementDesignator': 'M',
            'type': 'AN',
            'length': [2, 15]
        },
        {
            'ReferenceDesignator': 'GS04',
            'ReferenceNumber': '373',
            'Name': 'Date',
            'RequirementDesignator': 'M',
            'type': 'DT',
            'length': [8, 8]
        },
        {
            'ReferenceDesignator': 'GS05',
            'ReferenceNumber': '337',
            'Name': 'Time',
            'RequirementDesignator': 'M',
            'type': 'TM',
            'length': [4, 8]
        },
        {
            'ReferenceDesignator': 'GS06',
            'ReferenceNumber': '28',
            'Name': 'Group Control Number',
            'RequirementDesignator': 'M',
            'type': 'N0',
            'length': [1, 9]
        },
        {
            'ReferenceDesignator': 'GS07',
            'ReferenceNumber': '455',
            'Name': 'Responsible Agency Code',
            'RequirementDesignator': 'M',
            'type': 'ID',
            'length': [1, 2]
        },
        {
            'ReferenceDesignator': 'GS08',
            'ReferenceNumber': '180',
            'Name': 'Version / Release / Industry Identifier Code',
            'RequirementDesignator': 'M',
            'type': 'AN',
            'length': [1, 12]
        }
    ]
}

GE = {
    'id': 'GE',
    'name': 'Functional Group Trailer',
    'type': 'Control Segment',
    'purpose': 'To indicate the end of a functional group and to provide control information',
    'elements': [
        {
            'ReferenceDesignator': 'GE01',
            'ReferenceNumber': '97',
            'Name': 'Number of Transaction Sets Included',
            'RequirementDesignator': 'M',
            'type': 'N0',
            'length': [1, 6]
        },
        {
            'ReferenceDesignator': 'GE02',
            'ReferenceNumber': '28',
            'Name': 'Group Control Number',
            'RequirementDesignator': 'M',
            'type': 'N0',
            'length': [1, 9]
        }
    ]
}

segment_definitions = {'ISA': ISA, 'IEA': IEA, 'GS': GS, 'GE': GE}
