import unittest
from stringmanager import string2hex

class testtimeconv(unittest.TestCase):
    def test_string2hex_01(self):
        self.assertEqual("616263", string2hex("abc"))
        self.assertEqual("4D617263656C6C6F", string2hex("Marcello"))
        self.assertEqual("", string2hex(""))
        self.assertEqual(None, string2hex(None))
        
        
        



if __name__ == '__main__':
    unittest.main()

