import unittest, datetime
import project04.src.includeAge as includeAge
import project04.src.utils as utils

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(includeAgeTestCase)
    return suite
class includeAgeTestCase(unittest.TestCase):
    def setUp(self):
        self.underageInd = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['10 AUG 1989'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['7 OCT 2019']}
        self.ofAgeInd = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F01'], 'BIRT': ['4 OCT 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
        self.individualDict = {'I02' : self.underageInd, 'I01' : self.ofAgeInd }
    def tearDown(self):
        self.underageInd = None
        self.ofAgeInd = None
        self.individualDict = None

    def test_addAge(self):
        currentDate = datetime.date.today()
        indAge = utils.calculateAge(self.underageInd, currentDate)
        includeAge.addAgeToIndividual(self.underageInd)
        self.assertTrue("AGE" in self.underageInd.keys(), "Age was not added")
        self.assertEqual(indAge, self.underageInd["AGE"],  "This individual should be %d years old" % (indAge))

    def test_addAgeToAll(self):
        includeAge.addAgeToAll(self.individualDict)
        for key in self.individualDict.keys():
            ind = self.individualDict[key]
            self.assertTrue("AGE" in ind.keys(),  "There should only be one illegal family")

if __name__ == '__main__':
    unittest.main()  