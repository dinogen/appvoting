import unittest
import votation

class votation_test(unittest.TestCase):
    def test_insert(self):
        v = votation.votation_dto()
        v.votation_id = 'votation.test.1'
        v.votation_description = 'Votation record test 1'
        v.votation_type = 'casual'
        v.promoter_user_id = 1
        v.begin_date = '2018-01-01'
        v.end_date = '2018-01-15'
        votation.delete_votation_by_id(v.votation_id)
        votation.insert_votation_dto(v)
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
    def test_validate_id(self):
        self.assertFalse(votation.validate_votation_id(""))
        self.assertFalse(votation.validate_votation_id("abc 123"))
        self.assertFalse(votation.validate_votation_id(" 123.232"))
        self.assertFalse(votation.validate_votation_id("a#s"))
        self.assertFalse(votation.validate_votation_id("dinogen@ga"))
        self.assertTrue(votation.validate_votation_id("dinogen.ga"))
        self.assertTrue(votation.validate_votation_id("test123"))

if __name__ == '__main__':
    unittest.main()
