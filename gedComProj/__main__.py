'''
Team JAJ
CS 555 Project
I pledge my honor that I have abided by the Stevens Honor System.
'''
import sys, os
import gedComProj.src.utils as utils
import gedComProj.src.marriageAge as marriageAge, gedComProj.src.includeAge as includeAge
import gedComProj.src.siblingAge as siblingAge, gedComProj.src.illegitimateDates as illegitimateDates, gedComProj.src.correctGender as correctGender, gedComProj.src.dateCheck as dateCheck
import gedComProj.src.noSibMarriage as noSibMarriage, gedComProj.src.noParentMarriage as noParentMarriage
import gedComProj.src.recentBirths as recentBirths, gedComProj.src.recentDeaths as recentDeaths
import gedComProj.src.listDeceased as listDeceased, gedComProj.src.livingMarried as livingMarried
import gedComProj.src.us04Story as us04Story, gedComProj.src.us05Story as us05Story

from prettytable import PrettyTable
tags0 = ["HEAD", "TRLR", "NOTE"]
tags1 = ["NAME", "SEX", "BIRT", "DEAT", "FAMC",
         "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"]
tags2 = ["DATE"]
other_tags = ["INDI", "FAM"]
dateTags = ["BIRT", "DEAT", "MARR",  "DIV"]
familyDict = {}
individualDict = {}
dictDict = {"FAM": familyDict, "INDI": individualDict}
def loadFile():
    fileName = raw_input("Please enter the desired GEDCOM file name: ")
    fileName = fileName.strip()
    outputFileName = "parsedOutput" + os.path.basename(fileName)
    if (len(fileName) > 0):
        if(len(fileName) <= 4):
            fileName += ".ged"
            outputFileName += ".txt"
        elif(fileName[-4:] == ".ged"):
            outputFileName = outputFileName[0:-4] + ".txt"
        else:
            fileName += ".ged"
            outputFileName += ".txt"
        return (fileName, outputFileName)
    else:
        print("You have entered an invalid file name!")
        raise ValueError

def writeFileAndFillDict(inputFileName, outputFileName):
    loadedFile = open(inputFileName, 'r')
    writtenFile = open(outputFileName, 'a')
    currentObject = {}
    for i in loadedFile: 
        if i.strip() == "":
            continue
        oldLine = "-->" + i.strip() + "\n"
        lineArr = i.split()
        lev = int(lineArr[0])
        tag = lineArr[1]
        arg = ' '.join(lineArr[2:])
        constructedLine = ""
        if lev > 2:
            constructedLine = "<--" + \
                str(lev) + "|"+tag+"|"+"N"+"|"+arg.strip() + "\n"
        elif (lev == 1 and tag in tags1) or (lev == 2 and tag in tags2):
            constructedLine = "<--"+str(lev)+"|" + \
                tag+"|"+"Y"+"|"+arg.strip() + "\n"
            if tag in dateTags:
                lastDate = tag
            if tag == "DATE":
                currentObject[lastDate] = [arg]
            else:
                if tag in currentObject:
                    currentObject[tag] = currentObject[tag]+[arg]
                else:
                    currentObject[tag] = [arg]
        elif lev == 0 and tag in tags0:
            constructedLine = "<--"+str(lev)+"|" + \
                tag+"|"+"Y"+"|"+arg.strip() + "\n"
            if currentObject != {}:
                dictDict[currentObject["type"]
                            ][currentObject["ID"]] = currentObject
            currentObject = {}
        elif lineArr[-1] in other_tags and lev == 0:
            constructedLine = "<--" + \
                str(lev)+"|" + str(lineArr[-1]).strip() + \
                "|"+"Y"+"|" + str(lineArr[1]) + "\n"
            if currentObject != {}:
                dictDict[currentObject["type"]
                            ][currentObject["ID"]] = currentObject
            currentObject = {}
            currentObject["type"] = str(lineArr[-1]).strip()
            currentObject["ID"] = lineArr[1]
        else:
            constructedLine = "<--" + \
                str(lev) + "|"+tag+"|"+"N"+"|"+arg.strip() + "\n"
        writtenFile.write(oldLine)
        writtenFile.write(constructedLine)
    loadedFile.close()
    writtenFile.close()
    return

def constructAndWriteIndiTable(file):
    file.write('Individuals:\n')
    indiTable = PrettyTable(
        ['ID', 'Name', 'Gender', 'Birth', 'Death', 'Alive', 'Child', 'Spouse', 'Age'])
    for key in individualDict:
        addlist = [key] + individualDict[key]['NAME'] + \
            individualDict[key]['SEX'] + individualDict[key]['BIRT']
        if 'DEAT' in individualDict[key].keys():
            addlist += individualDict[key]['DEAT']
            addlist.append('N')
        else:
            addlist.append('N/A')
            addlist.append('Y')
        if 'FAMC' in individualDict[key].keys():
            addlist += individualDict[key]['FAMC']
        else:
            addlist.append('N/A')
        if 'FAMS' in individualDict[key].keys():
            addlist += individualDict[key]['FAMS']
        else:
            addlist.append('N/A')
        addlist.append(individualDict[key]['AGE'])
        indiTable.add_row(addlist)
    file.write(indiTable.get_string() + '\n')
    return

def constructAndWriteFamTable(writefi):
    writefi.write('Families:\n')
    famTable = PrettyTable(['ID', 'Married', 'Divorced', 'Husband ID',
                            'Husband Name', 'Wife ID', 'Wife Name', 'Children'])
    for key in familyDict:
        addlist = [key] + familyDict[key]['MARR']
        if 'DIV' in familyDict.keys():
            addlist += familyDict[key]['DIV']
        else:
            addlist.append('N/A')
        hid = familyDict[key]['HUSB'][0]
        wid = familyDict[key]['WIFE'][0]
        addlist += [hid] + individualDict[hid]['NAME'] + \
            [wid] + individualDict[wid]['NAME']
        if 'CHIL' in familyDict[key].keys():
            addlist += [familyDict[key]['CHIL']]
        else:
            addlist.append('N/A')
        famTable.add_row(addlist)
    writefi.write(famTable.get_string() + "\n")

if __name__ == "__main__":
    fileName, outputFileName = loadFile()
    writeFileAndFillDict(fileName, outputFileName)
    includeAge.addAgeToAll(individualDict)
    writefi = open('printoutput.txt', 'a')
    constructAndWriteIndiTable(writefi)
    constructAndWriteFamTable(writefi)
    siblingList = siblingAge.siblingAge(familyDict,individualDict)
    us10Anomalies = marriageAge.detectPedophilia(familyDict, individualDict)
    us42Anomalies = illegitimateDates.badDate(familyDict, individualDict)
    us21Anomalies = correctGender.confirmGender(familyDict, individualDict)
    us18Anomalies = noSibMarriage.noSiblingIncest(familyDict, individualDict)
    us17Anomalies = noParentMarriage.noParentIncest(familyDict, individualDict)
    us01Anomalies = dateCheck.dateCheck(familyDict, individualDict)
    us04Errors = us04Story.checkMarriageBeforeDivorce(familyDict)
    us05Errors = us05Story.checkMarriageBeforeDeath(familyDict,individualDict)
    recentDeathsList = recentDeaths.listRecentDeaths(familyDict, individualDict)
    recentBirthsList = recentBirths.listRecentBirths(familyDict, individualDict)
    deceasedList = listDeceased.listDeceased(individualDict)
    livingMarriedList = livingMarried.livingMarried(individualDict, familyDict)
    
    utils.writeErrors(us10Anomalies, writefi)
    utils.writeErrors(us42Anomalies, writefi)
    utils.writeErrors(us21Anomalies, writefi)
    utils.writeErrors(us01Anomalies, writefi)
    utils.writeErrors(siblingList, writefi)

    utils.writeErrors(us18Anomalies, writefi)
    utils.writeErrors(us17Anomalies, writefi)
    utils.writeErrors(recentDeathsList, writefi)
    utils.writeErrors(recentBirthsList, writefi)

    utils.writeErrors(deceasedList, writefi)
    utils.writeErrors(livingMarriedList, writefi)

    print(familyDict)
    writefi.close()


