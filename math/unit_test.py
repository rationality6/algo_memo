import unittest
# from ./math/unit_test import get_components_from_mag
import lib


class TestStringMethods(unittest.TestCase):
    def test_get_components_from_mag(self):
        self.assertEqual(lib.get_components_from_mag(5, 20), (1.71, 4.7))

    def test_get_mag_from_components(self):
        self.assertEqual(lib.get_mag_from_components(6, 7), 9.219544457292887)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_equal(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
