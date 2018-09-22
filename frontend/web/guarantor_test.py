import unittest
import guarantor
import user
import votation
import random

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
    def test_hash_complete_yes(self):
        v = votation.votation_dto()
        v.votation_description = 'Guar automated test ' + str(random.randint(1,500))
        v.votation_type = 'random'
        v.promoter_user_id = 1
        v.begin_date = '2018-01-01'
        v.end_date = '2018-01-15'
        v.votation_status = 2
        votation.insert_votation_dto(v)
        g = guarantor.guarantor_dto()
        g.votation_id = v.votation_id
        g.u.user_id = 5
        g.hash_ok = 1
        guarantor.insert_dto(g)
        g = guarantor.guarantor_dto()
        g.votation_id = v.votation_id
        g.u.user_id = 6
        g.hash_ok = 1
        guarantor.insert_dto(g)
        self.assertTrue(guarantor.guarantors_hash_complete(v.votation_id))


if __name__ == '__main__':
    unittest.main()
