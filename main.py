from information_unit import Interchange

if __name__ == '__main__':
    edi = Interchange("tests/test_data/EDI-810.txt")
    print(edi.header.elements)


