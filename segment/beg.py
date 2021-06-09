from .segment import Segment

BEG = Segment()

BEG = {
    'elements': [
    {'Name': 'BEG01', 'ElementNumber': 353, 'mandatory': True, 'obsolete': False},
    {'Name': 'BEG02', 'ElementNumber': 92, 'mandatory': True, 'obsolete': False},
    {'Name': 'BEG03', 'ElementNumber': 324, 'mandatory': True, 'obsolete': False},
    {'Name': 'BEG04', 'ElementNumber': 328, 'mandatory': False, 'obsolete': True},
    {'Name': 'BEG05', 'ElementNumber': 373, 'mandatory': True, 'obsolete': False},
    {'Name': 'BEG06', 'ElementNumber': 367, 'mandatory': False, 'obsolete': True},
    {'Name': 'BEG07', 'ElementNumber': 587, 'mandatory': True, 'obsolete': True},
    {'Name': 'BEG08', 'ElementNumber': 1019, 'mandatory': True, 'obsolete': False},
    {'Name': 'BEG09', 'ElementNumber': 1166, 'mandatory': True, 'obsolete': True},
    {'Name': 'BEG10', 'ElementNumber': 1232, 'mandatory': True, 'obsolete': True},
    {'Name': 'BEG11', 'ElementNumber': 786, 'mandatory': True, 'obsolete': True},
    {'Name': 'BEG12', 'ElementNumber': 640, 'mandatory': True, 'obsolete': True},
    ]
}

class BEG:
    name = "Beginning Segment for Purchase Order"
    purpose = "To indicate the beginning of the Purchase Order Transaction Set and transmit identifying numbers"
    elements = [
        {'Name': 'BEG01', 'ElementNumber': 353,  'mandatory': True,  'obsolete': False},
        {'Name': 'BEG02', 'ElementNumber': 92,   'mandatory': True,  'obsolete': False},
        {'Name': 'BEG03', 'ElementNumber': 324,  'mandatory': True,  'obsolete': False},
        {'Name': 'BEG04', 'ElementNumber': 328,  'mandatory': False, 'obsolete': True},
        {'Name': 'BEG05', 'ElementNumber': 373,  'mandatory': True,  'obsolete': False},
        {'Name': 'BEG06', 'ElementNumber': 367,  'mandatory': False, 'obsolete': True},
        {'Name': 'BEG07', 'ElementNumber': 587,  'mandatory': True,  'obsolete': True},
        {'Name': 'BEG08', 'ElementNumber': 1019, 'mandatory': True,  'obsolete': False},
        {'Name': 'BEG09', 'ElementNumber': 1166, 'mandatory': True,  'obsolete': True},
        {'Name': 'BEG10', 'ElementNumber': 1232, 'mandatory': True,  'obsolete': True},
        {'Name': 'BEG11', 'ElementNumber': 786,  'mandatory': True,  'obsolete': True},
        {'Name': 'BEG12', 'ElementNumber': 640,  'mandatory': True,  'obsolete': True},
    ]

validate = {
    'BEG01':
        {
            '00': 'Original: Used for all original purchase order submissions',
            '06': 'Confirmation: Used only to refer to purchase orders that were previously submitted by telephone or fax',
            '22': 'Information Copy'
        },
    'BEG02':
        {
            'BK': 'Blanket Order (Quantity Firm)',
            'BL': 'Bailment: Used to notify the supplier of a bailment withdrawal to be billed',
            'DS': 'Dropship: Used for multi point orders',
            'OS': 'Special Order: Order for product not normally distributed',
            'SA': 'Stand-alone Order'
        }

}