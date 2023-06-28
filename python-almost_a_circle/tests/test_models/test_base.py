import unittest
from models.base import Base

class BaseTestCase(unittest.TestCase):
    def test_assigning_id(self):
        # Requirement 1: Base() for assigning automatically an ID
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

        # Requirement 2: Base() for assigning automatically an ID + 1 of the previous
        obj2 = Base()
        self.assertEqual(obj2.id, 2)

    def test_saving_passed_id(self):
        # Requirement 3: Base(89) saving the ID passed
        obj3 = Base(89)
        self.assertEqual(obj3.id, 89)

if __name__ == '__main__':
    unittest.main()