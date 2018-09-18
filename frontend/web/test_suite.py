import unittest
import user_test
import votation_test
import candidate_test

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(user_test.user_test))
test_suite.addTest(unittest.makeSuite(votation_test.votation_test))
test_suite.addTest(unittest.makeSuite(candidate_test.candidate_test))

r = unittest.TextTestRunner()
r.run(test_suite)
