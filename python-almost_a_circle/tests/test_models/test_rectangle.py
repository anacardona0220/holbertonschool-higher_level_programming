import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
import io
from io import StringIO


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
            rectangle5 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            rectangle6 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            rectangle7 = Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            rectangle7 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            rectangle7 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            rectangle7 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            rectangle7 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            rectangle7 = Rectangle(1, 2, 3, -4)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
            
            def test_rectangle_area(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)
        rect.width = 10
        rect.height = 3
        self.assertEqual(rect.area(), 30)

    def test_rectangle_str(self):
        rect = Rectangle(4, 5, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 4/5"
        self.assertEqual(str(rect), expected_output)

    def test_display(self):
        rect = Rectangle(4, 5, 2, 3, 1)
        expected_output = "\n\n\n  ####\n  ####\n  ####\n  ####\n  ####\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)

    def test_rectangle_display_without_x_y(self):
        rectangle = Rectangle(5, 3)
        expected_output = "#####\n#####\n#####\n"
        with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_rectangle_display_without_y(self):
        rectangle = Rectangle(5, 3, 2)
        expected_output = "  #####\n  #####\n  #####\n"
        with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_rectangle_update_with_args(self):
        rect = Rectangle(4, 5, 2, 3, 1)
        rect.update(2, 6, 7, 1, 4)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 4)

    def test_rectangle_update_with_kwargs(self):
        rect = Rectangle(4, 5, 2, 3, 1)
        rect.update(id=2, width=6, height=7, x=1, y=4)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 4)

    def test_rectangle_update_with_args_and_kwargs(self):
        rect = Rectangle(4, 5, 2, 3, 1)
        rect.update(2, width=6, height=7, y=4)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 4)

    def test_to_dictionary(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        rect_dict = rect.to_dictionary()
        expected_dict = {
            "x": 2,
            "y": 3,
            "id": 1,
            "height": 10,
            "width": 5
        }
        self.assertDictEqual(rect_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
