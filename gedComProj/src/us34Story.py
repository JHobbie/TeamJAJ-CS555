import gedComProj.src.utils as utils


def checkForDiff(family, husband, wife):
    allowableMarriage = True
    marriageDate = utils.calcDate(family["MARR"][0])
    wifeAgeAtMarriage = utils.calculateAge(wife, marriageDate)
    husbandAgeAtMarriage = utils.calculateAge(husband, marriageDate)
    ageDifference = abs(wifeAgeAtMarriage - husbandAgeAtMarriage)
    if (((wifeAgeAtMarriage > husbandAgeAtMarriage) and (ageDifference >= husbandAgeAtMarriage)) or ((wifeAgeAtMarriage < husbandAgeAtMarriage) and (ageDifference >= wifeAgeAtMarriage))):
        allowableMarriage = False
    return allowableMarriage

def detectAgeDiff(familyDict, individualDict):
    anomalyList = []
    for key in familyDict.keys():
        currentFamily = familyDict[key]
        husband = individualDict[currentFamily["HUSB"][0]]
        wife = individualDict[currentFamily["WIFE"][0]]
        if not checkForDiff(currentFamily, husband, wife):
            anomalyList += [ "Anomaly US34: %s (%s) and %s (%s) have a large age difference in family %s!" %(wife['NAME'][0], wife['ID'], husband['NAME'][0], husband['ID'], currentFamily['ID']) ]
    return anomalyList