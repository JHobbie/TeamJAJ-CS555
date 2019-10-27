import datetime

#US07

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

def lessThan150(individualDict):
    retList = []
    currDate = datetime.datetime.now()
    for key in individualDict.keys():
        currInd = individualDict[key]
        if 'DEAT' in currInd.keys():
            deathDate = calcDate(currInd['DEAT'][0])
            if calculateAge(currInd, deathDate) >= 150:
                retList += [("Error US07: " + currInd['NAME'][0] + "was too old when they passed away.")]
        else:
            age = calculateAge(currInd, currDate)
            if age >= 150:
                retList += [("Error US07: " + currInd['NAME'][0] + "is too old.")]
    return retList

