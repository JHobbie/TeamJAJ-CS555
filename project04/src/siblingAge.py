#import project04.src.utils.py as utils

def siblingAge(familyDict, individualDict):
    for key in familyDict.keys():
        currentFam = familyDict[key]
        kidList = currentFam["CHIL"]
        newKidList = []
        for kid in kidList:
            currKid = individualDict[kid]
            newKidList.append(currKid)
        newKidList.sort(s=lambda child: child['AGE'])
        newKidList.reverse()
        return newKidList

            
