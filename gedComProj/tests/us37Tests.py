import unittest
import gedComProj.src.us37Story as us37Story

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(us37TestCase)
    return suite
class us37TestCase(unittest.TestCase):
    def setUp(self):
        self.mom = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['10 AUG 1989'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['6 NOV 2019']}
        #1
        self.dad = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F01'], 'BIRT': ['21 FEB 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
        #3
        self.child1 = {'NAME': ['Candy /Kane/'],  'FAMS': ['F02'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I03'}
        #5
        self.child2 = {'NAME': ['Reese /Bar/'], 'FAMS' : ['F04'], 'BIRT': ['20 MAY 1994'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I05'}
        #4
        self.child1Spouse = {'NAME': ['George /Kane/'],  'FAMS': ['F02'], 'BIRT': ['20 MAY 1994'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I04'}
        #6
        self.grandChild = {'NAME': ['Marshmallow /Sugar/'], 'FAMS': ['F03'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I06'}
        #7
        self.grandChildSpouse = {'NAME': ['Brown /Sugar/'], 'FAMS': ['F03'], 'BIRT': ['20 MAY 1994'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I07'}
        #8
        self.greatgrandchild = {'NAME': ['Agave /Sugar/'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I08'}
        #9
        self.child2Spouse = {'NAME': ['Vanilla /Bar/'], 'FAMS' : ['F04'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I09'}
        #10
        self.grandChild2 = {'NAME': ['Caramel /Bar/'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I10'}

        self.family01 = {'MARR': ['19 FEB 1990'], 'WIFE': ['I02'], 'CHIL': ['I03', 'I05'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F01'}
        self.family02 = {'MARR': ['19 FEB 1990'], 'WIFE': ['I03'], 'CHIL': ['I06'], 'HUSB': ['I04'], 'type': 'FAM', 'ID': 'F02'}
        self.family03 =  {'MARR': ['19 FEB 1990'], 'WIFE': ['I06'], 'CHIL': ['I08'], 'HUSB': ['I07'], 'type': 'FAM', 'ID': 'F03'}
        self.family04 =  {'MARR': ['19 FEB 1990'], 'WIFE': ['I09'], 'CHIL': ['I10'], 'HUSB': ['I05'], 'type': 'FAM', 'ID': 'F03'}
        self.individualDict = {'I02' : self.mom, 'I01' : self.dad, 'I03' : self.child1, 'I04' : self.child1Spouse, 'I05' : self.child2, 'I06' : self.grandChild, 'I07' : self.grandChildSpouse, 'I08' : self.greatgrandchild, 'I09' : self.child2Spouse, 'I10' : self.grandChild2}
        self.familyDict = {'F01' : self.family01, 'F02' : self.family02, 'F03' : self.family03, 'F04' : self.family04}

        
    def tearDown(self):
        self.mom = None
        self.dad = None
        self.child1 = None
        self.child2 = None
        self.child1Spouse = None
        self.grandChild = None
        self.grandChildSpouse = None
        self.greatgrandchild = None
        self.child2Spouse = None
        self.grandChild2 = None
    
    def test_us37(self):
        survivorsList = us37Story.listSurvivors(self.familyDict, self.individualDict)
        self.assertEqual(6, len(survivorsList[0][1]), "Deceased individual has 6 survivors")


        
if __name__ == '__main__':
    unittest.main()

    
