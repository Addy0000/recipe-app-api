# sample test

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):

    def test_add_numbers(self):
        """test adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_sub_numbers(self):
        """test suntracting numbers"""

        res = calc.sub(15, 10)

        self.assertEqual(res, 5)
