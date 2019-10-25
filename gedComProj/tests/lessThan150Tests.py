import unittest
import gedComProj.src.lessThan150 as lessThan150

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(lessThan150TestCase)
    return suite
class lessThan150TestCase(unittest.TestCase):
    def setUp(self):
        #i02
	self.mom = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['10 AUG 1800'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['9 OCT 2000']}
	#i01
	self.dad = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F01'], 'BIRT': ['21 FEB 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
	#i03
	self.child1 = {'NAME': ['Candy /Kane/'],  'FAMS': ['F02'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I03'}
	#i05
	self.child2 = {'NAME': ['Reese /Piece/'], 'BIRT': ['20 MAY 1860'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I05'}
	

	self.familyDict = {'F01': self.family}
	self.individualDict = {'I02' : self.mom, 'I01' : self.dad, 'I03' : self.child1, 'I05' : self.child2, 'I06' : self.child4, 'I07' : self.child3, 'I08' : self.child5, 'I09' : self.child6}

    def tearDown(self):
        self.mom = None
        self.dad = None
        self.child1 = None
        self.child2 = None
    
    
    def test_lessThan150(self):
        errmsg = lessThan150.lessThan150(self.individualDict)
        self.assertEqual(2, len(errmsg), "These two individuals have invalid ages.")


if __name__ == '__main__':
    unittest.main()
