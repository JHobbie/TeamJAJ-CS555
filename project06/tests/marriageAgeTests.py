import unittest
import project06.src.marriageAge as marriageAge

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(marriageAgeTestCase)
    return suite
class marriageAgeTestCase(unittest.TestCase):
    def setUp(self):
        self.underageInd = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['10 AUG 1989'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['7 OCT 2019']}
        self.ofAgeInd = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F01'], 'BIRT': ['4 OCT 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
        self.ofAgeInd2 = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F02'], 'BIRT': ['4 OCT 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I03'}
        self.familyBad = {'MARR': ['14 FEB 1990'], 'WIFE': ['I02'], 'CHIL': ['I03', 'I05', 'I06', 'I07'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F01'}
        self.familyGood = {'MARR': ['14 FEB 2000'], 'WIFE': ['I03'], 'CHIL': [ 'I05', 'I06', 'I07'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F02'}
        self.familyDict = {'F01': self.familyBad, 'F02' : self.familyGood}
        self.individualDict = {'I02' : self.underageInd, 'I01' : self.ofAgeInd , 'I03' : self.ofAgeInd2}
    def tearDown(self):
        self.underageInd = None
        self.ofAgeInd = None
        self.family = None
        self.familyGood = None
        self.familyBad = None 
        self.familyDict = None 
        self.individualDict = None

    def test_marriageAllowed(self):
        marriageNotAllowed = marriageAge.marriageAllowed(self.familyBad, self.ofAgeInd, self.underageInd)
        self.assertFalse(marriageNotAllowed, "This marriage should not be allowed")
        marriageAllowed = marriageAge.marriageAllowed(self.familyGood, self.ofAgeInd, self.ofAgeInd2)
        self.assertTrue(marriageAllowed, "This marriage should be allowed")

    def test_detectPedophilia(self):
        anomalyList = marriageAge.detectPedophilia(self.familyDict, self.individualDict)
        self.assertEqual(1, len(anomalyList), "There should only be one illegal family")

if __name__ == '__main__':
    unittest.main()