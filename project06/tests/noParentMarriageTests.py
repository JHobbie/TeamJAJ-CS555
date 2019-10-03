import unittest
import project06.src.noParentMarriage as noParentMarriage

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(noParentMarriageTestCase)
    return suite
class noParentMarriageTestCase(unittest.TestCase):
    def setUp(self):
        self.father = {'NAME': ['Hersh E. /Father/'],  'FAMS': ['F01'], 'FAMC': ['F00'], 'BIRT': ['4 OCT 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
        self.mother = {'NAME': ['Ginger /Mother/'],  'FAMS': ['F02'], 'FAMC': ['F00'],'BIRT': ['10 AUG 1989'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['7 OCT 2019']}
        
        self.daughter = {'NAME': ['Ginger /Daughter/'],  'FAMS': ['F01'], 'FAMC': ['F03'],'BIRT': ['10 AUG 1989'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I04', 'DEAT': ['7 OCT 2019']}
        self.son = {'NAME': ['Hersh E. /Son/'],  'FAMS': ['F02'], 'FAMC': ['F03'], 'BIRT': ['4 OCT 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I03'}
        
        self.unrelatedInd1 = {'NAME': ['Not Parent'],  'FAMS': ['F100'], 'BIRT': ['4 OCT 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I99'}
        self.unrelatedInd2 = {'NAME': ['Not Not Child'],  'FAMS': ['F100'], 'BIRT': ['4 OCT 1970'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I100'}

        
        self.familyParents = {'MARR': ['14 FEB 1990'], 'WIFE': ['I02'], 'CHIL': ['I03', 'I04'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F03'}
        self.familySon = {'MARR': ['14 FEB 1990'], 'WIFE': ['I02'], 'HUSB': ['I03'], 'type': 'FAM', 'ID': 'F02'}
        self.familyDaughter = {'MARR': ['14 FEB 1990'], 'WIFE': ['I04'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F01'}
        self.familyGood = {'MARR': ['14 FEB 2000'], 'WIFE': ['I100'], 'HUSB': ['I99'], 'type': 'FAM', 'ID': 'F100'}

        self.familyDict = {'F100': self.familyGood, 'F03' : self.familyParents, 'F02' : self.familySon, 'F01': self.familyDaughter}
        self.individualDict = {'I02' : self.mother, 'I01' : self.father , 'I03' : self.son, 'I04': self.daughter, 'I99': self.unrelatedInd1, 'I100': self.unrelatedInd2}
    def tearDown(self):
        self.father = None
        self.mother = None
        self.son = None
        self.daughter = None 
        self.unrelatedInd1 = None
        self.unrelatedInd2 = None
        self.familyGood = None
        self.familyParents = None 
        self.familySon = None 
        self.familyDaughter = None 
        self.familyDict = None 
        self.individualDict = None

    def test_spouseNotParent(self):
        goodFamily = noParentMarriage.spouseNotParent(self.familyGood, self.familyDict, self.individualDict)
        self.assertEqual(0, len(goodFamily), "There should be no illegal family detected for the good family")
        parentsFamily = noParentMarriage.spouseNotParent(self.familyParents, self.familyDict, self.individualDict)
        self.assertEqual(0, len(parentsFamily), "There should be no illegal family detected for the good family")
        sonFamily = noParentMarriage.spouseNotParent(self.familySon, self.familyDict, self.individualDict)
        self.assertEqual(1, len(sonFamily), "There should only be one illegal family")
        daughterFamily = noParentMarriage.spouseNotParent(self.familyDaughter, self.familyDict, self.individualDict)
        self.assertEqual(1, len(daughterFamily), "There should only be one illegal family")

    def test_noParentIncest(self):
        anomalyList = noParentMarriage.noParentIncest(self.familyDict, self.individualDict)
        self.assertEqual(2, len(anomalyList), "There should be two illegal familys")

if __name__ == '__main__':
    unittest.main()