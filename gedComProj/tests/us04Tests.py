import unittest
import gedComProj.src.us04Story as us04Story

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(us04TestCase)
    return suite
class us04TestCase(unittest.TestCase):
    def setUp(self):
        self.divorceBeforeMarriageFam = {'MARR': ['14 FEB 2000'], 'WIFE': ['I03'], 'HUSB': ['I04'], 'type': 'FAM', 'ID': 'F03', 'DIV' : ['13 FEB 2000']}
        self.divorceAfterMarriageFam = {'MARR': ['14 FEB 2000'], 'WIFE': ['I03'], 'HUSB': ['I04'], 'type': 'FAM', 'ID': 'F02', 'DIV' : ['15 FEB 2000']}
        self.noDivorceFam = {'MARR': ['14 FEB 1999'], 'WIFE': ['I01'], 'HUSB': ['I02'], 'type': 'FAM', 'ID': 'F01'}

        self.familyDict = {'F01': self.noDivorceFam, 'F02' : self.divorceAfterMarriageFam, 'F03': self.divorceBeforeMarriageFam}
    
    def tearDown(self):
        self.divorceBeforeMarriageFam = None
        self.divorceAfterMarriageFam = None
        self.noDivorceFam = None

        self.familyDict = None
    
    def test_us04(self):
        err_msg = us04Story.checkMarriageBeforeDivorce(self.familyDict)
        self.assertEqual(1, len(err_msg), "Family F03 divorced before they married.")

if __name__ == '__main__':
    unittest.main()
