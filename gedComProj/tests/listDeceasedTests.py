import unittest
import gedComProj.src.listDeceased as listDeceased

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(listDeceasedTestCase)
    return suite

class listDeceasedTestCase(unittest.TestCase):
	def setUp(self):
		self.ginger = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['10 AUG 1979'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['9 OCT 2002']}
		self.hersh = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F01'], 'BIRT': ['4 OCT 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
		self.candy = {'NAME': ['Candy /Kane/'],  'FAMS': ['F02'], 'BIRT': ['20 DEC 1991'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I03'}
		self.george = {'NAME': ['George /Kane/'],  'FAMS': ['F02'], 'BIRT': ['29 FEB 1992'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I04', 'DEAT': ['8 JUL 2001']}
		self.reese = {'NAME': ['Reese /Bar/'], 'BIRT': ['20 MAY 1994'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I05', 'DEAT': ['10 APR 1996']}

		self.family = {'MARR': ['19 FEB 1980'], 'WIFE': ['I02'], 'CHIL': ['I05'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F01'}
		self.family2 = {'MARR': ['14 FEB 2000'], 'WIFE': ['I03'], 'CHIL': [ 'I07'], 'HUSB': ['I04'], 'type': 'FAM', 'ID': 'F02'}

		self.famDict = {'F01': self.family, 'F02' : self.family2}
		self.indiDict = {'I02' : self.ginger, 'I01' : self.hersh, 'I03' : self.candy, 'I04' : self.george, 'I05' : self.reese}

	def tearDown(self):
		self.ginger = None
		self.hersh = None
		self.candy = None
		self.george = None
		self.reese = None

	def test_listDeceased(self):
		deadList = listDeceased.listDeceased(self.indiDict)
		self.assertEqual(3, len(deadList), "Individuals Ginger Bred, George Kane, and Reese Bar are deceased.")

if __name__ == '__main__':
    unittest.main()

