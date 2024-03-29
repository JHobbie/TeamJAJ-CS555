import datetime

def calcDate(dateString):
    try:
        calculatedDate = datetime.datetime.strptime(dateString, '%d %b %Y')
        return calculatedDate
    except:
        print("Could not parse date, returning now")
        # We get no credit for detecting syntactic errors, but may want to know when 
        return datetime.datetime.now()

def calculateAge(individual, inputDateObj):
    birthDate = individual["BIRT"][0]
    try:
        birthDateObj = calcDate(birthDate)
    except:
        print("Could not parse individual's birthdate")
        # We get no credit for detecting syntactic errors, but may want to know when 
        return -1
    else:
        ageAtInputDate = inputDateObj.year - birthDateObj.year -  (1 if (inputDateObj.month< birthDateObj.month) else (1 if ((inputDateObj.month == birthDateObj.month) and (inputDateObj.day < birthDateObj.day)) else 0))
        return ageAtInputDate

#US02

def birthBeforeMarriage(familyDict, individualDict):
    retList = []
    currDate = datetime.datetime.now()
    for key in familyDict.keys():
        currFam = familyDict[key]
        husb = individualDict[currFam['HUSB'][0]]
        wife = individualDict[currFam['WIFE'][0]]
        husbBirt = calcDate(husb['BIRT'][0])
        wifeBirt = calcDate(wife['BIRT'][0])
        marrDate = calcDate(currFam['MARR'][0])
        if marrDate < husbBirt:
            retList += [("Error US02: " + husb['NAME'][0] + "'s birth date is after their marriage date.")]
        if marrDate < wifeBirt:
            retList += [("Error US02: " + wife['NAME'][0] + "'s birth date is after their marriage date.")]
    return retList
        