'''
Amandeep Singh
CS 555 Project02
I pledge my honor that I have abided by the Stevens Honor System.
'''
import sys



tags0 = ["HEAD","TRLR","NOTE"]
tags1 = ["NAME","SEX","BIRT","DEAT","FAMC","FAMS","MARR","HUSB","WIFE","CHIL","DIV"]
tags2 = ["DATE"]
other_tags = ["INDI","FAM"]
familyDict = {}
individualDict = {}

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
    for i in loadedFile:
        oldLine = "-->" + i.strip() + "\n"
        lineArr = i.split()
        lev = int(lineArr[0])
        tag = lineArr[1]
        arg = ' '.join(lineArr[2:])
        constructedLine =""
        if lev > 2:
            constructedLine = "<--"+str(lev)+ "|"+tag+"|"+"N"+"|"+arg.strip() + "\n"
        elif (lev == 0 and tag in tags0) or (lev == 1 and tag in tags1) or (lev == 2 and tag in tags2):
           constructedLine = "<--"+str(lev)+"|"+tag+"|"+"Y"+"|"+arg.strip() + "\n"
        elif lineArr[-1] in other_tags and lev == 0:
            constructedLine = "<--"+str(lev)+"|"+str(lineArr[1])+"|"+"Y"+"|"+str(lineArr[-1]).strip() + "\n"
        else:
            constructedLine = "<--"+str(lev)+ "|"+tag+"|"+"N"+"|"+arg.strip() + "\n"
        print (oldLine, constructedLine)
        writtenFile.write(oldLine)
        writtenFile.write(constructedLine)
    loadedFile.close()
    writtenFile.close()
    


