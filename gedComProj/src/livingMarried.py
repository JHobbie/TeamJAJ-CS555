#US30

def livingMarried(individualDict, familyDict):
	retlist = []
	for key in familyDict.keys():
		currFam = familyDict[key]
		if 'MARR' in currFam.keys():
			husb = individualDict[currFam['HUSB'][0]]
			wife = individualDict[currFam['WIFE'][0]]
			if 'DEAT' not in husb.keys():
				if 'DEAT' not in wife.keys():
					retlist += [("US30: " + husb['NAME'][0] + "is living and married.")]
			if 'DEAT' not in wife.keys():
				if 'DEAT' not in husb.keys():
					retlist += [("US30: " + wife['NAME'][0] + "is living and married.")]
		else:
			retlist += [("There are no living and married individuals.")]
	return retlist
	