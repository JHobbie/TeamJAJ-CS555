import unittest
import gedComProj.src.us05Story as us05Story

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(us05TestCase)
    return suite
class us05TestCase(unittest.TestCase):
    def setUp(self):
        self.deadBeforeMarriageWife = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['10 AUG 1989'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I01', 'DEAT': ['7 OCT 1998']}
        self.deadBeforeMarriageHusband = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['10 AUG 1989'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['7 OCT 2019']}
        
        self.bothDeadBeforeMarriageWife = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F04'], 'BIRT': ['10 AUG 1989'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I07', 'DEAT': ['7 OCT 1998']}
        self.bothDeadBeforeMarriageHusband = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F04'], 'BIRT': ['10 AUG 1989'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I08', 'DEAT': ['7 OCT 1998']}

        self.deadAfterMarriageWife = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F02'], 'BIRT': ['4 OCT 1970'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I03', 'DEAT': ['7 OCT 2019']}
        self.deadAfterMarriageHusband = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F02'], 'BIRT': ['4 OCT 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I04', 'DEAT': ['7 OCT 2019']}

        self.livingWife = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F03'], 'BIRT': ['4 OCT 1970'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I05'}
        self.livingHusband = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F03'], 'BIRT': ['10 AUG 1989'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I06'}
        

        self.beforeMarriage = {'MARR': ['14 FEB 1999'], 'WIFE': ['I01'], 'HUSB': ['I02'], 'type': 'FAM', 'ID': 'F01'}
        self.bothDead = {'MARR': ['14 FEB 1999'], 'WIFE': ['I07'], 'HUSB': ['I08'], 'type': 'FAM', 'ID': 'F04'}
        self.afterMarriage = {'MARR': ['14 FEB 2000'], 'WIFE': ['I03'], 'HUSB': ['I04'], 'type': 'FAM', 'ID': 'F02'}
        self.noDeath = {'MARR': ['14 FEB 2000'], 'WIFE': ['I05'], 'HUSB': ['I06'], 'type': 'FAM', 'ID': 'F03'}
        
        self.familyDict01 = {'F01': self.beforeMarriage, 'F02' : self.afterMarriage, 'F03': self.noDeath}
        self.familyDict02 = {'F01': self.beforeMarriage, 'F02' : self.afterMarriage, 'F03': self.noDeath, 'F04': self.bothDead}
        self.individualDict = {'I01' : self.deadBeforeMarriageWife, 'I02' : self.deadBeforeMarriageHusband, 'I03' : self.deadAfterMarriageWife, 'I04' : self.deadAfterMarriageHusband, 'I05': self.livingWife, 'I06': self.livingHusband, 'I07': self.bothDeadBeforeMarriageWife, 'I08': self.bothDeadBeforeMarriageHusband}
    
    def tearDown(self):
        self.deadBeforeMarriageWife = None
        self.deadBeforeMarriageHusband = None
        self.bothDeadBeforeMarriageWife = None
        self.bothDeadBeforeMarriageHusband = None
        self.deadAfterMarriageWife = None
        self.deadAfterMarriageHusband = None
        self.livingHusband = None
        self.livingWife = None
        self.beforeMarriage = None
        self.afterMarriage = None
        self.noDeath = None
        self.familyDict01 = None
        self.familyDict02 = None
        self.individualDict = None
    
    def test_us05(self):
        err_msg = us05Story.checkMarriageBeforeDeath(self.familyDict01, self.individualDict)
        self.assertEqual(1, len(err_msg), "Individual I01 in Family F01 died before they married.")
        err_msg = us05Story.checkMarriageBeforeDeath(self.familyDict02, self.individualDict)
        self.assertEqual(3, len(err_msg), "Individual I01 in Family F01 died before they married. And individuals I07 and I08 died before they married")

if __name__ == '__main__':
    unittest.main()
