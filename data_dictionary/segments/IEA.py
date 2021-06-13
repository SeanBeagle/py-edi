id = 'IEA'
name = 'Interchange Control Trailer'
type = 'Control Segment'
purpose = 'To define the end of an interchange of zero or more functional groups and interchange-related control segments'


IEA01 = {'ReferenceDesignator': 'IEA01',
         'ReferenceNumber': 'I16',
         'Name': 'Number of Included Functional Groups',
         'RequirementDesignator': 'M',
         'type': 'N0',
         'length': [1, 5]}

IEA02 = {'ReferenceDesignator': 'IEA02',
         'ReferenceNumber': 'I12',
         'Name': 'Interchange Control Number',
         'RequirementDesignator': 'M',
         'type': 'N0',
         'length': [9, 9]}

data_elements = [IEA01, IEA02]
