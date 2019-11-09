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

#US03

def birthBeforeDeath(individualDict):
    retlist = []
    for key in individualDict.keys():
        currInd = individualDict[key]
        birth = calcDate(currInd['BIRT'][0])
        if 'DEAT' in currInd.keys():
            death = calcDate(currInd['DEAT'][0])
            if death < birth:
                retList += [("Error US03: " + currInd['NAME'][0] + "'s birth date is after their death date.")]
    return retlist
    
