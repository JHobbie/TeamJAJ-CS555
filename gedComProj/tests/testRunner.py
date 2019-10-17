import unittest
import gedComProj.tests.utilsTests as utilsTests
import gedComProj.tests.marriageAgeTests as marriageAgeTests, gedComProj.tests.includeAgeTests as includeAgeTests
import gedComProj.tests.illegitimateAgeTests as illegitimateAgeTests, gedComProj.tests.correctGenderTests as correctGenderTests
import gedComProj.tests.dateCheckTests as dateCheckTests, gedComProj.tests.siblingAgeTests as siblingAgeTests
import gedComProj.tests.siblingMarriageTests as siblingMarriageTests, gedComProj.tests.noParentMarriageTests as noParentMarriageTests
import gedComProj.tests.recentBirthsTests as recentBirthsTests, gedComProj.tests.recentDeathsTests as recentDeathsTests
import gedComProj.tests.listDeceasedTests as listDeceasedTests, gedComProj.tests.livingMarriedTests as livingMarriedTests
import gedComProj.tests.us05Tests as us05Tests

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
    us05TestsSuite = us05Tests.suite()
    alltests = unittest.TestSuite([utilsTestSuite, marriageAgeTestSuite, includeAgeTestSuite, correctGenderTestSuite, illegitimateAgeTestSuite, dateCheckTestSuite, siblingAgeTestSuite, siblingMarriageTestSuite, noParentMarriageTestSuite, recentBirthsTestSuite, recentDeathsTestSuite, listDeceasedTestSuite, livingMarriedTestSuite, us05TestsSuite])
    unittest.TextTestRunner(verbosity=2).run(alltests)
