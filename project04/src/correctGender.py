#mport project04.src.utils as utils

#US21
def confirmGender(familyDict, individualDict):
    err_msg = []
    for key in familyDict.keys():
        currFam = familyDict[key]
        husb = individualDict[currFam['HUSB'][0]]
        wife = individualDict[currFam['WIFE'][0]]
        if wife['SEX'][0] != 'F':
            err_str = "Anomaly US21: Gender of individual " + wife['ID'] + ": " + wife['NAME'][0] + " does not match role."
            err_msg.append(err_str)
        if husb['SEX'][0] != 'M':
            err_str = "Anomaly US21: Gender of individual " + husb['ID'] + ": " + husb['NAME'][0] + " does not match role."
            err_msg.append(err_str)
    return err_msg

