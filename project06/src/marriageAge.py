import project06.src.utils as utils


def marriageAllowed(family, husband, wife):
    allowableMarriage = True
    marriageDate = utils.calcDate(family["MARR"][0])
    wifeAgeAtMarriage = utils.calculateAge(wife, marriageDate)
    husbandAgeAtMarriage = utils.calculateAge(husband, marriageDate)
    if wifeAgeAtMarriage < 14 or husbandAgeAtMarriage < 14:
        allowableMarriage = False
    return allowableMarriage

def detectPedophilia(familyDict, individualDict):
    anomalyList = []
    for key in familyDict.keys():
        currentFamily = familyDict[key]
        husband = individualDict[currentFamily["HUSB"][0]]
        wife = individualDict[currentFamily["WIFE"][0]]
        if not marriageAllowed(currentFamily, husband, wife):
            anomalyList += [ "Anomaly US10: %s (%s) and %s (%s) married too young in family %s!" %(wife['NAME'][0], wife['ID'], husband['NAME'][0], husband['ID'], currentFamily['ID']) ]
            print("anomaly found!")
    return anomalyList