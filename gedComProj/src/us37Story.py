import datetime

def listRecentDeaths(familyDict, individualDict):
    currDate = datetime.datetime.today()
    pastDate = currDate - datetime.timedelta(days=30)
    deathList = []

    for key in individualDict.keys():
        currInd = individualDict[key]
        try:
        	if 'DEAT' in currInd.keys():
	            deatDate = datetime.datetime.strptime(currInd['DEAT'][0], '%d %b %Y')
	            if pastDate <= deatDate < currDate:
	                deathList += [currInd['ID']]
        except ValueError:
        	pass
    return deathList

def findDescendants(individual, familyDict, individualDict):
	allDescendants = []
	indiFam = {}
	currChil = []
	if 'FAMS' in individual.keys():
		indiFam = familyDict[individual['FAMS'][0]]
	if 'CHIL' in indiFam:
		currChil = indiFam['CHIL']
	allDescendants += currChil
	for c in currChil:
		allDescendants += findDescendants(individualDict[c], familyDict, individualDict)
	return allDescendants

def findSpouse(individual, familyDict, individualDict):
	indiFam = {}
	if 'FAMS' in individual.keys():
		indiFam = familyDict[individual['FAMS'][0]]
		if individual['SEX'][0] == 'M':
			return indiFam['WIFE'][0]
		else:
			return indiFam['HUSB'][0]
	return []

def filterDeath(lst, individualDict):
	for i in lst:
		currInd = individualDict[i]
		if 'DEAT' in currInd.keys():
			lst.remove(i)

def listSurvivors(familyDict, individualDict):
	deceased = listRecentDeaths(familyDict, individualDict)
	fullSurvivorsList = []
	for dIndi in deceased:
		currInd = individualDict[dIndi]
		if 'FAMS' in currInd.keys():
			survivors = [findSpouse(currInd, familyDict, individualDict)] + findDescendants(currInd, familyDict, individualDict)
			filterDeath(survivors, individualDict)
			fullSurvivorsList += [('US37: Individual ' + dIndi + ' is survived by individuals: ', survivors)]
	if fullSurvivorsList == []:
		fullSurvivorsList += ["US37: No survivors or no recent deaths"]
	return fullSurvivorsList