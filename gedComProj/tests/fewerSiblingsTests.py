import unittest
import gedComProj.src.fewerSiblings as fewerSiblings

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(fewerSiblingsTestCase)
    return suite
class fewerSiblingsTestCase(unittest.TestCase):
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
	self.child3 = {'NAME': ['Lemon /Drop/'],  'FAMS': ['F03'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I07'}
	#i06
	self.child4 = {'NAME': ['Mars /Bar/'], 'BIRT': ['20 MAY 1994'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I06'}
	#i08
	self.child5 = {'NAME': ['Twix /Bar/'], 'BIRT': ['20 MAY 1994'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I08'}
	#i09
	self.child6 = {'NAME': ['Kitkat /Bar/'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I09'}


	self.child7 = {'NAME': ['A /Bar/'],  'FAMS': ['F02'], 'BIRT': ['31 JAN 1997'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I10'}
	#i05
	self.child8 = {'NAME': ['B /Bar/'], 'BIRT': ['31 JAN 1997'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I11'}
	#i07
	self.child9 = {'NAME': ['C /Bar/'],  'FAMS': ['F03'], 'BIRT': ['31 JAN 1997'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I12'}
	#i06
	self.child10 = {'NAME': ['C /Bar/'], 'BIRT': ['31 JAN 1997'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I13'}
	#i08
	self.child11 = {'NAME': ['D /Bar/'], 'BIRT': ['31 JAN 1997'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I14'}
	#i09
	self.child12 = {'NAME': ['E /Bar/'], 'BIRT': ['31 JAN 1997'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I15'}


	self.child13 = {'NAME': ['G /Bar/'], 'BIRT': ['4 JUN 1995'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I16'}

	self.child14 = {'NAME': ['H /Bar/'], 'BIRT': ['4 JUN 1995'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I17'}
	self.child15 = {'NAME': ['I /Bar/'], 'BIRT': ['4 JUN 1995'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I18'}


	self.family = {'MARR': ['19 FEB 1990'], 'WIFE': ['I02'], 'CHIL': ['I03', 'I05', 'I06', 'I07', 'I08', 'I09', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15', 'I16', 'I17', 'I18'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F01'}


	self.familyDict = {'F01': self.family}
	self.individualDict = {'I02' : self.mom, 'I01' : self.dad, 'I03' : self.child1, 'I05' : self.child2, 'I06' : self.child4, 'I07' : self.child3, 'I08' : self.child5, 'I09' : self.child6, 'I10' : self.child7, 'I11' : self.child8, 'I12' : self.child9, 'I13' : self.child10, 'I14' : self.child11, 'I15' : self.child12, 'I16' : self.child13, 'I17' : self.child14, 'I18' : self.child15}

    
    def tearDown(self):
        self.mom = None
        self.dad = None
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None
        self.child5 = None
        self.child6 = None
        self.child7 = None
        self.child8 = None
        self.child9 = None
        self.child10 = None
        self.child11 = None
        self.child12 = None
        self.child13 = None
        self.child14 = None
        self.child15 = None
    
    
    def test_fewerSiblings(self):
        errmsg = fewerSiblings.fewerSiblings(self.familyDict)
        self.assertEqual(1, len(errmsg), "Family has too many children.")


if __name__ == '__main__':
    unittest.main()
