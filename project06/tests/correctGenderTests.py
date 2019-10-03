import unittest
import project06.src.correctGender as correctGender

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(correctGenderTestCase)
    return suite
class correctGenderTestCase(unittest.TestCase):
    def setUp(self):
        #i02
        self.wrongGender = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['10 AUG 1989'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['7 OCT 2019']}
        #i01
        self.rightGender = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F01'], 'BIRT': ['4 OCT 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
        #i03
        self.rightGender2 = {'NAME': ['Candy /Kane/'],  'FAMS': ['F02'], 'BIRT': ['16 JUN 1992'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I03'}
        #i04
        self.rightGender3 = {'NAME': ['George /Kane/'],  'FAMS': ['F02'], 'BIRT': ['25 AUG 1995'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I04'}

        self.familyBad = {'MARR': ['14 FEB 1990'], 'WIFE': ['I02'], 'CHIL': ['I03', 'I05', 'I06', 'I07'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F01'}
        self.familyGood = {'MARR': ['14 FEB 2000'], 'WIFE': ['I03'], 'CHIL': [ 'I05', 'I06', 'I07'], 'HUSB': ['I04'], 'type': 'FAM', 'ID': 'F02'}
        
        self.familyDict = {'F01': self.familyBad, 'F02' : self.familyGood}
        self.individualDict = {'I02' : self.wrongGender, 'I01' : self.rightGender, 'I03' : self.rightGender2, 'I04' : self.rightGender3}
    
    def tearDown(self):
        self.wrongGender = None
        self.rightGender2 = None
        self.rightGender = None
        self.rightGender3 = None
    
    def test_confirmGender(self):
        err_msg = correctGender.confirmGender(self.familyDict, self.individualDict)
        self.assertEqual(1, len(err_msg), "Individual I02 in Family F01 has the wrong gender.")

if __name__ == '__main__':
    unittest.main()
