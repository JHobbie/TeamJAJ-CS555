import unittest
import gedComProj.src.us34Story as us34Story

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(us34TestCase)
    return suite
class us34TestCase(unittest.TestCase):
    def setUp(self):
        self.underageInd = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['10 AUG 1926'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['7 OCT 2019']}
        self.ofAgeInd = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F01'], 'BIRT': ['4 OCT 1900'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
        self.ofAgeInd2 = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F02'], 'BIRT': ['4 OCT 1900'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I03'}
        self.familyBad = {'MARR': ['14 FEB 1950'], 'WIFE': ['I02'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F01'}
        self.familyGood = {'MARR': ['14 FEB 1950'], 'WIFE': ['I03'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F02'}
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

    def test_us34(self):
        anomalyList = us34Story.detectAgeDiff(self.familyDict, self.individualDict)
        self.assertEqual(1, len(anomalyList), "There should only be one odd family")

if __name__ == '__main__':
    unittest.main()