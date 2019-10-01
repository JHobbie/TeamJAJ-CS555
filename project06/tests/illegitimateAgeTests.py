import unittest
import project04.src.illegitimateDates as illegitimateDates

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(illegitimateDatesTestCase)
    return suite
class illegitimateDatesTestCase(unittest.TestCase):
    def setUp(self):
        #i02
        self.badDate = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['10 AUG 1989'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['99 OCT 2019']}
        #i01
        self.badDate2 = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F01'], 'BIRT': ['30 FEB 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
        #i03
        self.goodDate = {'NAME': ['Candy /Kane/'],  'FAMS': ['F02'], 'BIRT': ['16 JUN 1992'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I03'}
        #i04
        self.goodDate2 = {'NAME': ['George /Kane/'],  'FAMS': ['F02'], 'BIRT': ['29 FEB 1992'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I04'}

        self.familyBad = {'MARR': ['14 FEB 1990'], 'WIFE': ['I02'], 'CHIL': ['I03', 'I05', 'I06', 'I07'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F01'}
        self.familyGood = {'MARR': ['14 FEB 2000'], 'WIFE': ['I03'], 'CHIL': [ 'I05', 'I06', 'I07'], 'HUSB': ['I04'], 'type': 'FAM', 'ID': 'F02'}
        
        self.familyDict = {'F01': self.familyBad, 'F02' : self.familyGood}
        self.individualDict = {'I02' : self.badDate, 'I01' : self.badDate2, 'I03' : self.goodDate, 'I04' : self.goodDate2}

        self.exBadDate = "300 AUG 2011"
        self.exGoodDate = "29 FEB 2012"
    
    def tearDown(self):
        self.badDate = None
        self.badDate2 = None
        self.goodDate = None
        self.goodDate2 = None
    
    def test_checkValidDate(self):
        bd = illegitimateDates.checkValidDate(self.exBadDate)
        self.assertFalse(bd, "Invalid Date")
        gd = illegitimateDates.checkValidDate(self.exGoodDate)
        self.assertTrue(gd, "Valid Date")
    
    def test_badDate(self):
        err_msg = illegitimateDates.badDate(self.familyDict, self.individualDict)
        self.assertEqual(2, len(err_msg), "Individual I02 in Family F01 has an invalid death date, Individual I01 in Family F01 has an invalid birth date.")

if __name__ == '__main__':
    unittest.main()
