import unittest
import gedComProj.src.noSibMarriage as noSibMarriage

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(siblingMarriageTestCase)
    return suite
class siblingMarriageTestCase(unittest.TestCase):
    def setUp(self):
        self.sister = {'NAME': ['Ginger /Sister/'],  'FAMS': ['F01'], 'FAMC': ['F00'],'BIRT': ['10 AUG 1989'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['7 OCT 2019']}
        self.brother = {'NAME': ['Hersh E. /Brother/'],  'FAMS': ['F01'], 'FAMC': ['F00'], 'BIRT': ['4 OCT 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
        self.unrelatedInd1 = {'NAME': ['Not Brother'],  'FAMS': ['F02'], 'BIRT': ['4 OCT 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I03'}
        self.unrelatedInd2 = {'NAME': ['Not Sister'],  'FAMS': ['F02'], 'BIRT': ['4 OCT 1970'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I04'}
        self.familyBad = {'MARR': ['14 FEB 1990'], 'WIFE': ['I02'], 'CHIL': ['I03', 'I05', 'I06', 'I07'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F01'}
        self.familyGood = {'MARR': ['14 FEB 2000'], 'WIFE': ['I03'], 'CHIL': [ 'I05', 'I06', 'I07'], 'HUSB': ['I04'], 'type': 'FAM', 'ID': 'F02'}
        self.familyDict = {'F01': self.familyBad, 'F02' : self.familyGood}
        self.individualDict = {'I02' : self.sister, 'I01' : self.brother , 'I03' : self.unrelatedInd1, 'I04': self.unrelatedInd2}
    def tearDown(self):
        self.sister = None
        self.brother = None
        self.unrelatedInd1 = None
        self.unrelatedInd2 = None
        self.familyGood = None
        self.familyBad = None 
        self.familyDict = None 
        self.individualDict = None

    def test_spouseNotSibling(self):
        goodFamily = noSibMarriage.spouseNotSibling(self.familyGood, self.familyDict, self.individualDict)
        self.assertEqual(0, len(goodFamily), "There should be no illegal family detected for the good family")
        badFamily = noSibMarriage.spouseNotSibling(self.familyBad, self.familyDict, self.individualDict)
        self.assertEqual(1, len(badFamily), "There should only be one illegal family")

    def test_noSiblingIncest(self):
        anomalyList = noSibMarriage.noSiblingIncest(self.familyDict, self.individualDict)
        self.assertEqual(1, len(anomalyList), "There should only be one illegal family")

if __name__ == '__main__':
    unittest.main()