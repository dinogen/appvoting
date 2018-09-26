import unittest
import backend



class test_create_election(unittest.TestCase):
    def test_success(self):
        """Election successfully created with 3 candidates and 4 guarantors"""
        result = backend.create_election(999,3,4)
        self.assertTrue(result)
        
        
        



if __name__ == '__main__':
    unittest.main()

