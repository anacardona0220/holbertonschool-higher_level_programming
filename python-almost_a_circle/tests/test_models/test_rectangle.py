import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
import io


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
        # with self.assertRaises(TypeError):
        #     rectangle8 = Rectangle(1,2,3,4,5)

    def test_area_calculate(self):
        rectangle9 = Rectangle(2, 6)
        area = rectangle9.area()
        self.assertEqual(area, 12)

    def test_display_without_xy(self):
        rect = Rectangle(4, 5, 0, 0, 10)
        expected_output = "####\n####\n####\n####\n####\n"
        self.assertEqual(rect.display(), expected_output)

    def test_display_without_y(self):
        rect = Rectangle(4, 5, 2, 0, 10)
        expected_output = "  ####\n  ####\n  ####\n  ####\n  ####\n"
        self.assertEqual(rect.display(), expected_output)

    def __str__(self):
        """ str special method """
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_xy + str_wh

    # def setUp(self):
    #     # Runs before every test
    #     self.rectangle10 = Rectangle(4, 5)  # Rectangle without x and y
    #     self.rectangle11 = Rectangle(4, 5, x=2)  # Rectangle without y
    #     self.rectangle12 = Rectangle(4, 5, x=2, y=3)  # Rectangle with x and y

    # def test_display_without_x_and_y(self):
    #     expected_output = "####\n####\n####\n####\n####\n"
    #     with patch("sys.stdout", new=io.StringIO()) as fake_output:
    #         self.rectangle10.display()
    #         self.assertEqual(fake_output.getvalue(), expected_output)

    # def test_display_without_y(self):
    #     expected_output = "\n\n  ####\n  ####\n  ####\n  ####\n  ####\n"
    #     with patch("sys.stdout", new=io.StringIO()) as fake_output:
    #         self.rectangle11.display()
    #         self.assertEqual(fake_output.getvalue(), expected_output)

    # def test_display(self):
    #     expected_output = "    ####\n    ####\n    ####\n    ####\n    ####\n"
    #     with patch("sys.stdout", new=io.StringIO()) as fake_output:
    #         self.rectangle12.display()
    #         self.assertEqual(fake_output.getvalue(), expected_output)

    def test_str(self):
        rectan = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rectan), "[Rectangle] (5) 3/4 - 1/2")


if __name__ == '__main__':
    unittest.main()
