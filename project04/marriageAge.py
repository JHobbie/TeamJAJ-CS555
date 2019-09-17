import utils

def calculateAge(individual, inputDateObj):
    birthDate = individual["BIRT"][0]
    try:
        birthDateObj = utils.calcDate(birthDate)
    except:
        print("Could not parse individual's birthdate")
        # We get no credit for detecting syntactic errors, but may want to know when 
        return -1
    else:
        ageAtInputDate = inputDateObj.year - birthDateObj.year -  (1 if (inputDateObj.month< birthDateObj.month) else (1 if ((inputDateObj.month == birthDateObj.month) and (inputDateObj.day < birthDateObj.day)) else 0))
        print(individual["NAME"][0] + " is " + str(ageAtInputDate) + "years old")
        return ageAtInputDate


def marriageAllowed(family, husband, wife):
    allowableMarriage = True
    marriageDate = utils.calcDate(family["MARR"][0])
    wifeAgeAtMarriage = calculateAge(wife, marriageDate)
    husbandAgeAtMarriage = calculateAge(husband, marriageDate)
    if wifeAgeAtMarriage < 14 or husbandAgeAtMarriage < 14:
        allowableMarriage = False
    return allowableMarriage

def detectPedophilia(familyDict, individualDict):
    anomalyList = []
    for key in familyDict.keys():
        print(key)
        print(familyDict[key])
        currentFamily = familyDict[key]
        husband = individualDict[currentFamily["HUSB"][0]]
        wife = individualDict[currentFamily["WIFE"][0]]
        if not marriageAllowed(currentFamily, husband, wife):
            anomalyList += [ "Anomaly US10: %s (%s) and %s (%s) married too young in family %s!" %(wife['NAME'][0], wife['ID'], husband['NAME'][0], husband['ID'], currentFamily['ID']) ]
            print("anomaly found!")
    return anomalyList