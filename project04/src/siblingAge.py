def siblingAge(familyDict, individualDict, file):
    file.write('US28 Ordering Siblings by age:\n')
    for key in familyDict.keys():
        currentFam = familyDict[key]
        file.write("Family id %s \n" %  (currentFam['ID']))
        if( "CHIL" in currentFam):
            kidList = currentFam["CHIL"]
            newKidList = []
            for kid in kidList:
                currKid = individualDict[kid]
                newKidList.append(currKid)
            newKidList.sort(key = lambda child: child['AGE'])
            newKidList.reverse()
            for kid in newKidList:
                file.write("%s: %s is %d years old\n" %(kid['ID'], kid['NAME'][0], kid['AGE']))
        else:
            file.write("No children in this family\n")
    return

            
