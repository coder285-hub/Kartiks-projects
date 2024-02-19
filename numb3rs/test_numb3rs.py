import unittest
from numb3rs import validate

class TestValidateIPv4(unittest.TestCase):
    def test_valid_ipv4(self):
        self.assertTrue(validate("192.168.0.1"))
        self.assertTrue(validate("10.0.0.1"))
        self.assertTrue(validate("255.255.255.255"))

    def test_invalid_ipv4(self):
        self.assertFalse(validate("275.3.6.28"))
        self.assertFalse(validate("192.168.0"))
        self.assertFalse(validate("192.168.0.256"))
        self.assertFalse(validate("192.168.0.-1"))
        self.assertFalse(validate("192.168.0.1.2"))

    def test_invalid_format(self):
        self.assertFalse(validate("192.168.0.1.2.3"))
        self.assertFalse(validate("192.168.0..1"))
        self.assertFalse(validate("192.168.0"))

if __name__ == '__main__':
    unittest.main()
