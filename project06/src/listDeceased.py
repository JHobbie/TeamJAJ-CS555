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

        