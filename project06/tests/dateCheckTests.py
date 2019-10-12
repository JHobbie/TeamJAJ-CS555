import unittest
import project06.src.dateCheck as dateCheck

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(dateCheckTestCase)
    return suite
class dateCheckTestCase(unittest.TestCase):
    def setUp(self):
        #i02
        self.badDate = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['10 AUG 1989'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['7 OCT 2019']}
        #i01
        self.goodDate = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F01'], 'BIRT': ['21 FEB 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
        #i03
        self.badDate2 = {'NAME': ['Candy /Kane/'],  'FAMS': ['F02'], 'BIRT': ['20 DEC 1991'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I03'}
        #i04
        self.goodDate2 = {'NAME': ['George /Kane/'],  'FAMS': ['F02'], 'BIRT': ['29 FEB 1992'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I04'}

        self.familyBad = {'MARR': ['19 FEB 2021'], 'WIFE': ['I02'], 'CHIL': ['I03', 'I05', 'I06', 'I07'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F01'}
        self.familyGood = {'MARR': ['14 FEB 2000'], 'WIFE': ['I03'], 'CHIL': [ 'I05', 'I06', 'I07'], 'HUSB': ['I04'], 'type': 'FAM', 'ID': 'F02'}
        
        self.familyDict = {'F01': self.familyBad, 'F02' : self.familyGood}
        self.individualDict = {'I02' : self.badDate, 'I01' : self.goodDate, 'I03' : self.badDate2, 'I04' : self.goodDate2}

    
    def tearDown(self):
        self.badDate = None
        self.badDate2 = None
        self.goodDate = None
        self.goodDate2 = None
    
    
    def test_dateCheck(self):
        err_msg = dateCheck.dateCheck(self.familyDict, self.individualDict)
        self.assertEqual(3, len(err_msg), "Individual I02 in Family F01 has an invalid death date, Individual I03 in Family F01 has an invalid birth date, Family F01 has an invalid marriage date")

if __name__ == '__main__':
    unittest.main()
