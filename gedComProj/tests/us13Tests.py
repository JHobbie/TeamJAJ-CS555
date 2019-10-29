import unittest
import gedComProj.src.us13Story as us13Story

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(us13TestCase)
    return suite
class us13TestCase(unittest.TestCase):
    def setUp(self):
        #i02
	self.mom = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['10 AUG 1989'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['9 OCT 2020']}
	#i01
	self.dad = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F01'], 'BIRT': ['21 FEB 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
	#i03
	self.child1 = {'NAME': ['Candy /Kane/'],  'FAMS': ['F02'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I03'}
	#i05
	self.child2 = {'NAME': ['Reese /Bar/'], 'BIRT': ['20 MAY 1994'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I05'}
	#i07
	self.child3 = {'NAME': ['Lemon /Drop/'],  'FAMS': ['F03'], 'BIRT': ['21 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I07'}
	#i06
	self.child4 = {'NAME': ['Mars /Bar/'], 'BIRT': ['22 MAY 1994'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I06'}
	#i08
	self.child5 = {'NAME': ['Twix /Bar/'], 'BIRT': ['20 JAN 1995'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I08'}
	#i09
	self.child6 = {'NAME': ['Kitkat /Bar/'], 'BIRT': ['20 FEB 1995'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I09'}

	self.family = {'MARR': ['19 FEB 1990'], 'WIFE': ['I02'], 'CHIL': ['I03', 'I05', 'I06', 'I07', 'I08', 'I09'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F01'}


	self.familyDict = {'F01': self.family}
	self.individualDict = {'I02' : self.mom, 'I01' : self.dad, 'I03' : self.child1, 'I05' : self.child2, 'I06' : self.child4, 'I07' : self.child3, 'I08' : self.child5, 'I09' : self.child6}


    
    def tearDown(self):
        self.mom = None
        self.dad = None
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None
        self.child5 = None
        self.child6 = None
        self.family = None 
        self.familyDict = None
        self.individualDict = None     
    
    def test_us13(self):
        errmsg = us13Story.checkSiblingAgeDifference(self.familyDict, self.individualDict)
        self.assertEqual(7, len(errmsg), "Family should have seven accounts of too close.")


if __name__ == '__main__':
    unittest.main()
