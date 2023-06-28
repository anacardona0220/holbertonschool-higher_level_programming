import unittest
from models.rectangle import Rectangle

class RectangleTestCase(unittest.TestCase):
    def test_valid_parameters(self):
        # Requirement 12: Rectangle(1, 2)
        rectangle1 = Rectangle(1, 2)
        self.assertEqual(rectangle1.width, 1)
        self.assertEqual(rectangle1.height, 2)
        self.assertEqual(rectangle1.x, 0)
        self.assertEqual(rectangle1.y, 0)

        # Requirement 13: Rectangle(1, 2, 3)
        rectangle2 = Rectangle(1, 2, 3)
        self.assertEqual(rectangle2.width, 1)
        self.assertEqual(rectangle2.height, 2)
        self.assertEqual(rectangle2.x, 3)
        self.assertEqual(rectangle2.y, 0)

        # Requirement 14: Rectangle(1, 2, 3, 4)
        rectangle3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle3.width, 1)
        self.assertEqual(rectangle3.height, 2)
        self.assertEqual(rectangle3.x, 3)
        self.assertEqual(rectangle3.y, 4)
        
    def test_invalid_parameters(self):
        with self.assertRaises(TypeError):
            rectangle4 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            rectangle5 = Rectangle(1,"2")
        with self.assertRaises(TypeError):
            rectangle6 = Rectangle(1,2,"3")
        with self.assertRaises(TypeError):
            rectangle7 = Rectangle(1,2,3,"4")
        # with self.assertRaises(TypeError):
        #     rectangle8 = Rectangle(1,2,3,4,5)
    def test_area_calculate(self):
        rectangle9 = Rectangle(2,6)
        area = rectangle9.area()
        self.assertEqual(area, 12)
        
    def test_display_calculate(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
            
        rectangle10 = Rectangle(2,6)
        display = rectangle10.area()
        self.assertEqual(display, 12)
       
        
        # display()` without `x` and `y`
		# `display()` without `y`
		# `display()`
        
if __name__ == '__main__':
    unittest.main()