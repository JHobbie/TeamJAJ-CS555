import unittest
import gedComProj.src.us38Story as us38Story

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(us38TestCase)
    return suite
class us38TestCase(unittest.TestCase):
    def setUp(self):
        self.mom = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['15 AUG 1989'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['6 NOV 2019']}
        #1
        self.dad = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F01'], 'BIRT': ['23 NOV 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
        #3
        self.child1 = {'NAME': ['Candy /Kane/'],  'FAMS': ['F02'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I03'}
        #5
        self.child2 = {'NAME': ['Reese /Bar/'], 'FAMS' : ['F04'], 'BIRT': ['29 NOV 1994'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I05'}
        
        self.family01 = {'MARR': ['19 FEB 1990'], 'WIFE': ['I02'], 'CHIL': ['I03', 'I05'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F01'}
        self.individualDict = {'I02' : self.mom, 'I01' : self.dad, 'I03' : self.child1, 'I05' : self.child2}
        self.familyDict = {'F01' : self.family01}

        
    def tearDown(self):
        self.mom = None
        self.dad = None
        self.child1 = None
        self.child2 = None

    
    def test_us38(self):
        bdayList = us38Story.upcomingBirthdays(self.individualDict)
        self.assertEqual(2, len(bdayList), "There are two upcoming birthdays in the family")


        
if __name__ == '__main__':
    unittest.main()

    
