'''
Type:
    Nn: Numeric n=implied positions to right of decimal

- Number
- Name
- Description
- MinLength: (chars) not including ['+','-','.']
- MaxLength: (chars) not including ['+','-','.']
- Type
- Segment Where Used
- Transaction Set Used In
'''

empty_element = \
    {
        'Number': int(),
        'Name': str(),
        'Description': str(),
        'Type': str(),
        'MinLength': int(),
        'MaxLength': int(),
        'TransactionSets': list(),
        'segment': list()
    }

elements = [
    {
        'Number': 2,
        'Name': 'Number of Accepted Transaction Sets',
        'Type': 'N0',
        'MinLength': 1,
        'MaxLength': 6,
        'Description': 'Number of accepted Transaction Sets in a Functional Group',
        'TransactionSets': [997],
        'segment': ['AK9']
    },
    {
        'Number': 3,
        'Name': 'Free Form Message',
        'Type': 'AN',
        'MinLength': 1,
        'MaxLength': 60,
        'Description': 'Free-form text',
        'TransactionSets': [824, 875, 876, 878, 879, 888, 889,
                            894, 895, 940, 879, 880, 880, 882],
        'segment': ['G22', 'G23', 'TED', 'W09']
    },
    {
        'Number': 92,
        'Name': 'Purchase Order Type Code',
        'Description': 'Code specifying the type of Purchase Order',
        'Type': 'ID',
        'MinLength': 2,
        'MaxLength': 2,
        'TransactionSets': [180, 214, 850, 856, 857, 867, 875],
        'segment': ['BEG', 'G50', 'PRF']
    },
    {
        'Number': 324,
        'Name': 'Purchase Order Number',
        'Description': 'Identifying number for Purchase Order assigned by the orderer/purchaser',
        'Type': 'AN',
        'MinLength': 1,
        'MaxLength': 22,
        'TransactionSets': [180, 214, 812, 830, 857, 867, 875, 876, 895, 940, 945,
                            947, 846, 850, 852, 855, 856, 880, 880, 881, 882, 894],
        'segment': ['BAK', 'BCD', 'BEG', 'BFR', 'CS', 'G01', 'G48', 'G50',
                     'G82', 'G88', 'G92', 'PRF', 'SPO', 'W05', 'W06', 'XPO']
    },
    {
        'Number': 353,
        'Name': 'Transaction Set Purpose Code',
        'Type': 'ID',
        'Description': 'Code identifying purpose of transaction set',
        'MinLength': 2,
        'MaxLength': 2,
        'TransactionSets': [180, 812, 816, 824, 830, 831, 846, 856, 857, 864,
                            867, 877, 881, 883, 891, 947, 850, 855, 887, 888],
        'segment': ['BAK', 'BCD', 'BEG', 'BFR', 'BGN', 'BHT', 'BIA', 'BPT', 'BSN', 'OTI', 'SPI', 'W15', 'BMA', 'BMG']
    },
    {
        'Number': 373,
        'Name': 'Date',
        'Description': 'Date expressed as CCYYMMDD',
        'Type': 'DT',
        'MinLength': 8,
        'MaxLength': 8,
        'TransactionSets': [180, 214, 850, 852, 877, 878, 884, 885, 896, 940, 812, 816, 820, 824, 830, 831, 846, 855,
                            856, 857, 864, 867, 875, 876, 879, 879, 880, 880, 881, 882, 883, 886, 887, 888, 889, 891,
                            894, 895, 944, 945, 947],
        'segment': list()
    }
]

# .to_json() .to_csv() .to_xml()

class DataElement:
    number = int()
    name = str()
    type = str()
    description = str()
