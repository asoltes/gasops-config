import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from modules.module_date_time import DateTime
import unittest

date = DateTime()

class TestDateTimeConvert(unittest.TestCase):

    def test_underscore_date(self):
        date_input = "1992-11-30"
        actual = DateTime.convert_to_underscore_format(date_input)
        expected = "1992_11_30"
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()