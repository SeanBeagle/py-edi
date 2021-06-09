from data_element import data_dictionary


class DataElement:
    """The data element is the smallest information unit in the information structure.
    A data element may be a single character code, a series of characters constituting a literal description or a
    numeric quantity. The data element has two primary attributes, length and type. The length characteristic of a data
    element may be fixed or variable. Each data element is identified by a number used for reference in the Data Element
    Dictionary.

    number:
        Data Element Numbers are provided for cross-references.

    name:
        Data Element Names refer to three types of data_element.
        1. Elements which convey actual values or text information, i.e., amounts, quantities, descriptions.
           NOTE: When an element is defined as a percent, the data conveys actual percent- age, e.g., 10% is expressed
                 as 10.
        2. Elements described as codes which convey information through a coding structure in which the code indicates a
           specific definition: e.g., State or Province Code (Data Element 156) designates a particular state or
           province.
        3. Elements designated as qualifiers convey information about another data element through a coding structure.
           In these instances, the other data ele- ment being qualified is relatively non-specific by itself and is made
           specific by the value of the qualifier. For example, the definition of Identification Code Designator (Data
           Element 67) allows for an identifying code. The Identification Code Qualifier (Data Element 66) indicates the
           code set to which the identifying code belongs (DUNS, SCAC, ...). This concept must be qualified to be
           meaningful.

    description:
        Describes the data element and its intended functional use.

    min_length:
        Minimum number of characters defined for the data element.

    max_length:
        Maximum number of characters defined for the data element.
        Does not include the decimal point or sign (+ or -) for the number-type or decimal-type data data_element.

    type:
        A data element may be one of six types: numeric, decimal, identifier, string, date, or time.
        The symbols used to designate the data element types are as follows.
        ['Nn', 'ID', 'R', 'AN', 'DT', 'TM']
    """

    reference_number = int()
    name = str()
    description = str()
    min_length = int()
    max_length = int()
    type = str()
    segments = list()
    transaction_sets = list()

    def __init__(self, **kwargs):
        self.reference_number = kwargs.get('Number')
        self.name = kwargs.get('Name')
        self.description = kwargs.get('Description')
        self.min_length = kwargs.get('MinLength')
        self.max_length = kwargs.get('MaxLength')
        self.type = kwargs.get('Type')
        self.segments = kwargs.get('segment')
        self.transaction_sets = kwargs.get('TransactionSets')

    def __repr__(self):
        return f'{self.__class__.__name__}({self.reference_number}: {self.name})'

    @staticmethod
    def all():
        return [DataElement(**element) for element in data_dictionary.elements]
