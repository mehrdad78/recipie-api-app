"""
Sample Test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test the cacl module"""

    def test_add_numbers(self):
        res = calc.add(1,2)

        self.assertEqual(res,3)

    def test_substract_numbers(self):
        res = calc.substract(4,1)
        self.assertEqual(res,3)