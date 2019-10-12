#US29

def listDeceased(individualDict):
	retlist = []
	for key in individualDict.keys():
		currInd = individualDict[key]
		if 'DEAT' in currInd.keys():
			retlist += [("US29: " + currInd['NAME'][0] + "is deceased.")]
	if retlist == []:
		retlist += [("US29: There are no deceased individuals.")]
	return retlist

ginger = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['10 AUG 1979'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['9 OCT 2002']}
hersh = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F01'], 'BIRT': ['4 OCT 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
candy = {'NAME': ['Candy /Kane/'],  'FAMS': ['F02'], 'BIRT': ['20 DEC 1991'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I03'}
george = {'NAME': ['George /Kane/'],  'FAMS': ['F02'], 'BIRT': ['29 FEB 1992'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I04'}
reese = {'NAME': ['Reese /Bar/'], 'BIRT': ['20 MAY 1994'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I05'}

family = {'MARR': ['19 FEB 1980'], 'WIFE': ['I02'], 'CHIL': ['I05'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F01'}
family2 = {'MARR': ['14 FEB 2000'], 'WIFE': ['I03'], 'CHIL': [ 'I02'], 'HUSB': ['I04'], 'type': 'FAM', 'ID': 'F02'}

famDict = {'F01': family, 'F02' : family2}
indiDict = {'I02' : ginger, 'I01' : hersh, 'I03' : candy, 'I04' : george, 'I05' : reese}


print(listDeceased(indiDict))
        