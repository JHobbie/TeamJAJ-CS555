'''
Team JAJ
CS 555 Project
I pledge my honor that I have abided by the Stevens Honor System.
'''
import sys
import utils
import marriageAge
import includeAge
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

if __name__ == "__main__":
    fileName = raw_input("Please enter the desired GEDCOM file name: ")
    fileName = fileName.strip()
    outputFileName = "parsedOutput" + fileName
    if (len(fileName) > 0):
        if(len(fileName) <= 4):
            fileName += ".ged"
            outputFileName += ".txt"
        elif(fileName[-4:] == ".ged"):
            outputFileName = outputFileName[0:-4] + ".txt"
        else:
            fileName += ".ged"
            outputFileName += ".txt"
        loadedFile = open(fileName, 'r')
        writtenFile = open(outputFileName, 'a')
        currentObject = {}
        for i in loadedFile: #TODO: Refactor at some point (IE Probably Never)
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
        includeAge.addAgeToAll(individualDict)
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
        writefi = open('printoutput.txt', 'a')
        writefi.write('Individuals:\n')
        writefi.write(indiTable.get_string() + '\n')
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
        us10Anomalies = marriageAge.detectPedophilia(familyDict, individualDict)
        utils.writeErrors(us10Anomalies, writefi)
        writefi.close()
    

