import unittest
import votation
import random

class votation_test(unittest.TestCase):
    def test_load_by_id(self):
        """Load the test votation present in the create.sql file"""
        v1 = votation.load_votation_by_id(1)
        self.assertIsNotNone(v1)
        self.assertEqual(1, v1.votation_id)
        self.assertEqual("votation test 1", v1.votation_description)
        self.assertEqual("random", v1.votation_type)
        self.assertEqual(1, v1.promoter_user_id)
        self.assertEqual('2018-10-01', v1.begin_date)
        self.assertEqual('2018-10-30', v1.end_date)
        self.assertEqual(0,v1.votation_status)
        
    def test_insert(self):
        v = votation.votation_dto()
        v.votation_description = 'Votation automated test ' + str(random.randint(0,500))
        v.votation_type = 'random'
        v.promoter_user_id = 1
        v.begin_date = '2018-01-01'
        v.end_date = '2018-01-15'
        v.votation_status = 2
        self.assertTrue( votation.insert_votation_dto(v) )
        self.assertGreater(v.votation_id,0)
        v1 = votation.load_votation_by_id(v.votation_id)
        self.assertIsNotNone(v1)
        self.assertEqual(v.votation_id, v1.votation_id)
        self.assertEqual(v.votation_description, v1.votation_description)
        self.assertEqual(v.votation_type, v1.votation_type)
        self.assertEqual(v.promoter_user_id, v1.promoter_user_id)
        self.assertEqual(v.begin_date, v1.begin_date)
        self.assertEqual(v.end_date, v1.end_date)
    def test_validate_string_date(self):
        self.assertTrue(votation.validate_string_date("2018-01-01"))
        self.assertTrue(votation.validate_string_date("1999-01-01"))
        self.assertTrue(votation.validate_string_date("2999-12-31"))
        self.assertFalse(votation.validate_string_date(""))
        self.assertFalse(votation.validate_string_date("a"))
        self.assertFalse(votation.validate_string_date("2180"))
        self.assertFalse(votation.validate_string_date("2018-32-10"))
        self.assertFalse(votation.validate_string_date("2018-02-30"))


if __name__ == '__main__':
    unittest.main()
