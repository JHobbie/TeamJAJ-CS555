def siblingAge(familyDict, individualDict):
    retList = []
    #file.write('US28 Ordering Siblings by age:\n')
    for key in familyDict.keys():
        currentFam = familyDict[key]
        retList +=  [("Family id %s" %  (currentFam['ID']))]
        if( "CHIL" in currentFam):
            kidList = currentFam["CHIL"]
            newKidList = []
            for kid in kidList:
                currKid = individualDict[kid]
                newKidList.append(currKid)
            newKidList.sort(key = lambda child: child['AGE'])
            newKidList.reverse()
            for kid in newKidList:
                retList+=[("%s: %s is %d years old" %(kid['ID'], kid['NAME'][0], kid['AGE']))]
        else:
            retList+= ["No children in this family"]
    return retList

