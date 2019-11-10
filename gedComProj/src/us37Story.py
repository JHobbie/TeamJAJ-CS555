import datetime

def listRecentDeaths(familyDict, individualDict):
    currDate = datetime.datetime.today()
    pastDate = currDate - datetime.timedelta(days=30)
    deathList = []

    for key in individualDict.keys():
        currInd = individualDict[key]
        if 'DEAT' in currInd.keys():
            deatDate = datetime.datetime.strptime(currInd['DEAT'][0], '%d %b %Y')
            if pastDate <= deatDate < currDate:
                deathList += [currInd['ID']]
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
	return fullSurvivorsList

#2
mom = {'NAME': ['Ginger /Bred/'],  'FAMS': ['F01'], 'BIRT': ['10 AUG 1989'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['6 NOV 2019']}
#1
dad = {'NAME': ['Hersh E. /Bar/'],  'FAMS': ['F01'], 'BIRT': ['21 FEB 1970'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I01'}
#3
child1 = {'NAME': ['Candy /Kane/'],  'FAMS': ['F02'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I03'}
#5
child2 = {'NAME': ['Reese /Bar/'], 'FAMS' : ['F04'], 'BIRT': ['20 MAY 1994'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I05'}
#4
child1Spouse = {'NAME': ['George /Kane/'],  'FAMS': ['F02'], 'BIRT': ['20 MAY 1994'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I04'}
#6
grandChild = {'NAME': ['Marshmallow /Sugar/'], 'FAMS': ['F03'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I06'}
#7
grandChildSpouse = {'NAME': ['Brown /Sugar/'], 'FAMS': ['F03'], 'BIRT': ['20 MAY 1994'], 'SEX': ['M'], 'type': 'INDI', 'ID': 'I07'}
#8
greatgrandchild = {'NAME': ['Agave /Sugar/'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I08'}
#9
child2Spouse = {'NAME': ['Vanilla /Bar/'], 'FAMS' : ['F04'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I09'}
#10
grandChild2 = {'NAME': ['Caramel /Bar/'], 'BIRT': ['20 MAY 1994'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I10'}

family01 = {'MARR': ['19 FEB 1990'], 'WIFE': ['I02'], 'CHIL': ['I03', 'I05'], 'HUSB': ['I01'], 'type': 'FAM', 'ID': 'F01'}
family02 = {'MARR': ['19 FEB 1990'], 'WIFE': ['I03'], 'CHIL': ['I06'], 'HUSB': ['I04'], 'type': 'FAM', 'ID': 'F02'}
family03 =  {'MARR': ['19 FEB 1990'], 'WIFE': ['I06'], 'CHIL': ['I08'], 'HUSB': ['I07'], 'type': 'FAM', 'ID': 'F03'}
family04 =  {'MARR': ['19 FEB 1990'], 'WIFE': ['I09'], 'CHIL': ['I10'], 'HUSB': ['I07'], 'type': 'FAM', 'ID': 'F03'}
individualDict = {'I02' : mom, 'I01' : dad, 'I03' : child1, 'I04' : child1Spouse, 'I05' : child2, 'I06' : grandChild, 'I07' : grandChildSpouse, 'I08' : greatgrandchild, 'I09' : child2Spouse, 'I10' : grandChild2}
familyDict = {'F01' : family01, 'F02' : family02, 'F03' : family03, 'F04' : family04}

print(listSurvivors(familyDict, individualDict))