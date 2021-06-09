class TransactionSet:
    """A transaction set is composed of a specific group of segment that represent a common business document.

     (for
    example, a purchase order or an invoice). Each transaction set consists of the transaction set header (ST) as the
    first segment and contains at least one segment before the transaction set trailer (SE).
    """
    number = int()
    name = str()
    functional_group_id = str()
    version = str()
    sections = list()  # eg: ['Header', 'Detail', 'Summary']

    def __init__(self, number, name):
        self.number = number
        self.name = name

    def my_function(self):
        print(self.name)


    @staticmethod
    def my_second_function():
        print("Hello World!")


ts = TransactionSet(number=850, name="tsnum2")
ts.name = "Purchase Order"




