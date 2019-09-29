import unittest
import  project04.tests.utilsTests as utilsTests
import project04.tests.marriageAgeTests as marriageAgeTests, project04.tests.includeAgeTests as includeAgeTests
import project04.tests.illegitimateAgeTests as illegitimateAgeTests, project04.tests.correctGenderTests as correctGenderTests

if __name__ == '__main__':
    #mainTestSuite = mainTests.suite()
    utilsTestSuite = utilsTests.suite()
    marriageAgeTestSuite = marriageAgeTests.suite()
    includeAgeTestSuite = includeAgeTests.suite()
    correctGenderTestSuite = correctGenderTests.suite()
    illegitimateAgeTestSuite = illegitimateAgeTests.suite()
    alltests = unittest.TestSuite([utilsTestSuite, marriageAgeTestSuite, includeAgeTestSuite, correctGenderTestSuite, illegitimateAgeTestSuite])
    unittest.TextTestRunner(verbosity=2).run(alltests)