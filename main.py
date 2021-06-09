from edi_parser import EdiParser
from data_element import data_element
from transaction_set import EDI850
import unittest

if __name__ == '__main__':
    '''
    file = "/Users/seanbeagle/go/ElectronicDataInterchange/data/810-OUT_884_20210201_100923.DMS"
    parser = EdiParser()
    parser.parse(file)

    for element in data_element.DataElement.all():
        print(element)
    '''

    class Dog:
        name = str()
        _id = int()
        breed = str()
        color = str()

        def __init__(self, name, id, breed, color):
            self.name = name.capitalize()
            self.id = id
            self.breed = breed
            self.color = color

        @property
        def id(self):
            return self._id

        @id.setter
        def id(self, id):
            if id < 1:
                self._id = id
                raise Exception("ID out of range")
            else:
                print("dats a goooood id")
                self._id = id

        def bark(self):
            print(self.name + " the " + self.breed + " says WOOF!")


    test_dog = Dog("rufus", 1, 'poodle', 'white')

    class TestDogClass(unittest.TestCase):
        def test_id_less_than_one_throws_exception(self):
            self.assertRaises(Exception, Dog, 'rufus', 0, 'poodle', 'white')

        def test_breed_is_poodle(self):
            self.assertEqual(test_dog.breed, 'shepherd')


    tc = TestDogClass()
    tc.test_id_less_than_one_throws_exception()
    tc.test_breed_is_poodle()



