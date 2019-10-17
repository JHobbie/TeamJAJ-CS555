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


def writeErrors(errorList, file):
    for error in errorList:
        file.write(error + "\n")
    return