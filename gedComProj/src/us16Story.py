def getSurname(nameStr):
	surnameInd = nameStr.find('/')
	return nameStr[surnameInd:]

def maleLastNames(individualDict, familyDict):
	errmsg = []
	for key in familyDict.keys():
		currFam = familyDict[key]
		husb = individualDict[currFam['HUSB'][0]]
		surname = getSurname(husb['NAME'][0])
		if 'CHIL' in currFam.keys():
			childList = currFam['CHIL']
			for cKey in childList:
				child = individualDict[cKey]
				if child['SEX'][0] == 'M' and (surname != getSurname(child['NAME'][0])):
					errmsg += ["Error US16: Individual " + child['ID'] + "'s surname does not match Family " + currFam['ID'] + "'s surname."]
	return errmsg

