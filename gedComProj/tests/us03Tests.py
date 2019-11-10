import unittest
import gedComProj.src.us03Story as us03Story

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(us03TestCase)
    return suite
class us03TestCase(unittest.TestCase):
    def setUp(self):
        self.mom = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['10 AUG 1989'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['9 AUG 1989']}
        #1
        self.dad = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F01'], 'BIRT': ['23 NOV 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
        #3
        self.child1 = {'NAME': ['Candy /Kane/'],  'FAMS': ['F02'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I03'}
        #5
        self.child2 = {'NAME': ['Reese /Bar/'], 'FAMS' : ['F04'], 'BIRT': ['18 FEB 1990'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I05', 'DEAT': ['16 JAN 1972']}
        #4
        self.child1Spouse = {'NAME': ['George /Kane/'],  'FAMS': ['F02'], 'BIRT': ['20 MAY 1994'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I04'}

        self.family01 = {'MARR': ['19 FEB 1990'], 'WIFE': ['I02'], 'CHIL': ['I03', 'I05'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F01'}
        self.family02 = {'MARR': ['19 FEB 1990'], 'WIFE': ['I03'], 'CHIL': ['I06'], 'HUSB': ['I04'], 'type': 'FAM', 'ID': 'F02'}
        self.individualDict = {'I02' : self.mom, 'I01' : self.dad, 'I03' : self.child1, 'I05' : self.child2, 'I04' : self.child1Spouse}
        self.familyDict = {'F01' : self.family01, 'F02' : self.family02}

        
    def tearDown(self):
        self.mom = None
        self.dad = None
        self.child1 = None
        self.child2 = None
        self.child1Spouse = None

    
    def test_us03(self):
        errmsg = us03Story.birthBeforeDeath(self.individualDict)
        self.assertEqual(2, len(errmsg), "Ginger Bred and Reese Bar died before they were born")


        
if __name__ == '__main__':
    unittest.main()

    
