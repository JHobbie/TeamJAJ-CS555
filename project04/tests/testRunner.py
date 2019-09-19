import unittest
import  project04.tests.utilsTests as utilsTests
import project04.tests.marriageAgeTests as marriageAgeTests, project04.tests.includeAgeTests as includeAgeTests

if __name__ == '__main__':
    #mainTestSuite = mainTests.suite()
    utilsTestSuite = utilsTests.suite()
    marriageAgeTestSuite = marriageAgeTests.suite()
    includeAgeTestSuite = includeAgeTests.suite()
    alltests = unittest.TestSuite([utilsTestSuite, marriageAgeTestSuite, includeAgeTestSuite])
    unittest.TextTestRunner(verbosity=2).run(alltests)