import sys

import unittest

from LDMP.testv2.test_func import CalculateLDNUnitSuite


def unitTests():
    suite = unittest.TestSuite()
    suite.addTest(CalculateLDNUnitSuite())
    return suite


def run_all():
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(unitTests())
