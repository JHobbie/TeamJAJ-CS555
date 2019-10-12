import unittest
import project06.tests.utilsTests as utilsTests
import project06.tests.marriageAgeTests as marriageAgeTests, project06.tests.includeAgeTests as includeAgeTests
import project06.tests.illegitimateAgeTests as illegitimateAgeTests, project06.tests.correctGenderTests as correctGenderTests
import project06.tests.dateCheckTests as dateCheckTests, project06.tests.siblingAgeTests as siblingAgeTests
import project06.tests.siblingMarriageTests as siblingMarriageTests, project06.tests.noParentMarriageTests as noParentMarriageTests
import project06.tests.recentBirthsTests as recentBirthsTests, project06.tests.recentDeathsTests as recentDeathsTests
import project06.tests.listDeceasedTests as listDeceasedTests, project06.tests.livingMarriedTests as livingMarriedTests

if __name__ == '__main__':
    #mainTestSuite = mainTests.suite()
    utilsTestSuite = utilsTests.suite()
    marriageAgeTestSuite = marriageAgeTests.suite()
    includeAgeTestSuite = includeAgeTests.suite()
    correctGenderTestSuite = correctGenderTests.suite()
    illegitimateAgeTestSuite = illegitimateAgeTests.suite()
    dateCheckTestSuite = dateCheckTests.suite()
    siblingAgeTestSuite = siblingAgeTests.suite()
    siblingMarriageTestSuite = siblingMarriageTests.suite()
    noParentMarriageTestSuite = noParentMarriageTests.suite()
    recentBirthsTestSuite = recentBirthsTests.suite()
    recentDeathsTestSuite = recentDeathsTests.suite()
    listDeceasedTestSuite = listDeceasedTests.suite()
    livingMarriedTestSuite = livingMarriedTests.suite()
    
    alltests = unittest.TestSuite([utilsTestSuite, marriageAgeTestSuite, includeAgeTestSuite, correctGenderTestSuite, illegitimateAgeTestSuite, dateCheckTestSuite, siblingAgeTestSuite, siblingMarriageTestSuite, noParentMarriageTestSuite, recentBirthsTestSuite, recentDeathsTestSuite, listDeceasedTestSuite, livingMarriedTestSuite])
    unittest.TextTestRunner(verbosity=2).run(alltests)
