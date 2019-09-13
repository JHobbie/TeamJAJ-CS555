'''
Team JAJ
CS 555 Project03
I pledge my honor that I have abided by the Stevens Honor System.
'''
import sys


tags0 = ["HEAD", "TRLR", "NOTE"]
tags1 = ["NAME", "SEX", "BIRT", "DEAT", "FAMC",
    "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"]
tags2 = ["DATE"]
other_tags = ["INDI", "FAM"]
familyDict = {}
individualDict = {}
dictDict = {"FAM": familyDict, "INDI": individualDict}
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
    currentObject = []
    for i in loadedFile:
        oldLine = "-->" + i.strip() + "\n"
        lineArr = i.split()
        lev = int(lineArr[0])
        tag = lineArr[1]
        arg = ' '.join(lineArr[2:])
        constructedLine = ""
        if lev > 2:
            constructedLine = "<--" + str(lev) + "|"+tag+"|"+"N"+"|"+arg.strip() + "\n"
        elif (lev == 1 and tag in tags1) or (lev == 2 and tag in tags2):
           constructedLine = "<--"+str(lev)+"|" + tag+"|"+"Y"+"|"+arg.strip() + "\n"
           tup = (tag, arg)
           currentObject.append(tup)
        elif lev == 0 and tag in tags0:
            constructedLine = "<--"+str(lev)+"|" + tag+"|"+"Y"+"|"+arg.strip() + "\n"
            if len(currentObject) >= 2:
               dictDict[currentObject[0]][currentObject[1]] = currentObject
            currentObject = []
        elif lineArr[-1] in other_tags and lev == 0:
            constructedLine = "<--"+str(lev)+"|"+ str(lineArr[-1]).strip()+"|"+"Y"+"|"+ str(lineArr[1]) + "\n"
            if len(currentObject)>=2:
                dictDict[currentObject[0]][currentObject[1]] = currentObject
                writtenFile.write(str(currentObject))
            currentObject = []
            currentObject.append(str(lineArr[-1]).strip())
            currentObject.append(lineArr[1])
        else:
            constructedLine = "<--"+str(lev)+ "|"+tag+"|"+"N"+"|"+arg.strip() + "\n"
        print (oldLine, constructedLine)
        writtenFile.write(oldLine)
        writtenFile.write(constructedLine)
    loadedFile.close()
    writtenFile.close()
    


