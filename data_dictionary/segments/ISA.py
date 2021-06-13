id = 'ISA'
type = 'Control Segment'
name = 'Interchange Control Header'
purpose = 'To start and identify an interchange of zero or more functional groups and interchange-related control segments'

ISA01 = {'ReferenceDesignator': 'ISA01',
         'ReferenceNumber': 'I01',
         'Name': 'Authorization Information Qualifier',
         'RequirementDesignator': 'M',
         'type': 'ID',
         'length': [2, 2]}

ISA02 = {'ReferenceDesignator': 'ISA02',
         'ReferenceNumber': 'I02',
         'Name': 'Authorization Information',
         'RequirementDesignator': 'M',
         'type': 'AN',
         'length': [10, 10]}

ISA03 = {'ReferenceDesignator': 'ISA03',
         'ReferenceNumber': 'I03',
         'Name': 'Security Information Qualifier',
         'RequirementDesignator': 'M',
         'type': 'ID',
         'length': [2, 2]}

ISA04 = {'ReferenceDesignator': 'ISA04',
         'ReferenceNumber': 'I04',
         'Name': 'Security Information',
         'RequirementDesignator': 'M',
         'type': 'AN',
         'length': [10, 10]}

ISA05 = {'ReferenceDesignator': 'ISA05',
         'ReferenceNumber': 'I05',
         'Name': 'Interchange ID Qualifier',
         'RequirementDesignator': 'M',
         'type': 'ID',
         'length': [2, 2]}

ISA06 = {'ReferenceDesignator': 'ISA06',
         'ReferenceNumber': 'I06',
         'Name': 'Interchange Sender ID',
         'RequirementDesignator': 'M',
         'type': 'AN',
         'length': [15, 15]}

ISA07 = {'ReferenceDesignator': 'ISA07',
         'ReferenceNumber': 'I05',  # I05
         'Name': 'Interchange ID Qualifier',
         'RequirementDesignator': 'M',
         'type': 'ID',
         'length': [2, 2]}

ISA08 = {'ReferenceDesignator': 'ISA08',
         'ReferenceNumber': 'I07',  # I07
         'Name': 'Interchange Receiver ID',
         'RequirementDesignator': 'M',
         'type': 'AN',
         'length': [15, 15]}

ISA09 = {'ReferenceDesignator': 'ISA09',
         'ReferenceNumber': 'I08',  # I08
         'Name': 'Interchange Date',
         'RequirementDesignator': 'M',
         'type': 'DT',
         'length': [6, 6]}

ISA10 = {'ReferenceDesignator': 'ISA10',
         'ReferenceNumber': 'I09',  # I09
         'Name': 'Interchange Time',
         'RequirementDesignator': 'M',
         'type': 'TM',
         'length': [4, 4]}

ISA11 = {'ReferenceDesignator': 'ISA11',
         'ReferenceNumber': 'I10',  # I10
         'Name': 'Interchange Control Standards Identifier',
         'RequirementDesignator': 'M',
         'type': 'ID',
         'length': [1, 1]}

ISA12 = {'ReferenceDesignator': 'ISA12',
         'ReferenceNumber': 'I11',  # I11
         'Name': 'Interchange Control Version Number',
         'RequirementDesignator': 'M',
         'type': 'ID',
         'length': [5, 5]}

ISA13 = {'ReferenceDesignator': 'ISA13',
         'ReferenceNumber': 'I12',  # I12
         'Name': 'Interchange Control Number',
         'RequirementDesignator': 'M',
         'type': 'N0',
         'length': [9, 9]}

ISA14 = {'ReferenceDesignator': 'ISA14',
         'ReferenceNumber': 'I13',  #I13
         'Name': 'Acknowledgment Requested',
         'RequirementDesignator': 'M',
         'type': 'ID',
         'length': [1, 1]}

ISA15 = {'ReferenceDesignator': 'ISA15',
         'ReferenceNumber': 'I14',
         'Name': 'Usage Indicator',
         'RequirementDesignator': 'M',
         'type': 'ID',
         'length': [1, 1]}

ISA16 = {'ReferenceDesignator': 'ISA16',
         'ReferenceNumber': 'I15',  # I15
         'Name': 'Component Element Separator',
         'RequirementDesignator': 'M',
         'type': None,
         'length': [1, 1]}

data_elements = [ISA01, ISA02, ISA03, ISA04, ISA05, ISA06, ISA07, ISA08,
                 ISA09, ISA10, ISA11, ISA12, ISA13, ISA14, ISA15, ISA16]