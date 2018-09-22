import unittest
import guarantor
import user
import votation

class guarantor_test(unittest.TestCase):
    def test_validate_1(self):
        o = guarantor.guarantor_dto()
        o.votation_id = 1
        self.assertEqual(1,guarantor.validate_dto(o))
    def test_validate_2(self):
        o = guarantor.guarantor_dto()
        o.votation_id = None
        o.u.user_id = 1
        self.assertEqual(2,guarantor.validate_dto(o))
    def test_validate_3(self):
        o = guarantor.guarantor_dto()
        o.votation_id = 1
        o.u.user_id = 999
        self.assertEqual(3,guarantor.validate_dto(o))
    def test_validate_4(self):
        o = guarantor.guarantor_dto()
        o.votation_id = 1
        o.u.user_id = 1
        self.assertEqual(0,guarantor.validate_dto(o))
    def test_validate_5(self):
        o = guarantor.guarantor_dto()
        o.votation_id = 999 # don't exist
        o.u.user_id = 1
        self.assertEqual(4,guarantor.validate_dto(o))

if __name__ == '__main__':
    unittest.main()
