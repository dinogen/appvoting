import unittest
import candidate
import user
import votation

class candidate_test(unittest.TestCase):
    def test_validate_1(self):
        o = candidate.candidate_dto()
        o.votation_id = 1
        self.assertEqual(1,candidate.validate_dto(o))
    def test_validate_2(self):
        o = candidate.candidate_dto()
        o.votation_id = None
        o.u.user_id = 1
        self.assertEqual(2,candidate.validate_dto(o))
    def test_validate_3(self):
        o = candidate.candidate_dto()
        o.votation_id = 1
        o.u.user_id = 999
        self.assertEqual(3,candidate.validate_dto(o))
    def test_validate_4(self):
        o = candidate.candidate_dto()
        o.votation_id = 1
        o.u.user_id = 1
        self.assertEqual(0,candidate.validate_dto(o))
    def test_validate_5(self):
        o = candidate.candidate_dto()
        o.votation_id = 999 # don't exist
        o.u.user_id = 1
        self.assertEqual(4,candidate.validate_dto(o))

if __name__ == '__main__':
    unittest.main()
