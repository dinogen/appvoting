#!/usr/bin/env python3
import unittest
import user_test
import votation_test
import candidate_test
import guarantor_test
import backend_test

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(user_test.user_test))
test_suite.addTest(unittest.makeSuite(votation_test.votation_test))
test_suite.addTest(unittest.makeSuite(candidate_test.candidate_test))
test_suite.addTest(unittest.makeSuite(guarantor_test.guarantor_test))
test_suite.addTest(unittest.makeSuite(backend_test.test_create_election))
test_suite.addTest(unittest.makeSuite(backend_test.test_send_hash))
test_suite.addTest(unittest.makeSuite(backend_test.test_send_passphrase))
test_suite.addTest(unittest.makeSuite(backend_test.test_confirm_passphrase))
test_suite.addTest(unittest.makeSuite(backend_test.test_status))

r = unittest.TextTestRunner()
r.run(test_suite)
