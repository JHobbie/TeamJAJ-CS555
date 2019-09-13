'''
Amandeep Singh
CS 555 Project02
I pledge my honor that I have abided by the Stevens Honor System.
'''
import sys

#f = open("proj02test.ged", "r")
#f = open("project01_gedcomFile.ged", "r")
f = open("testGedJo.ged", "r")
tags0 = ["HEAD","TRLR","NOTE"]
tags1 = ["NAME","SEX","BIRT","DEAT","FAMC","FAMS","MARR","HUSB","WIFE","CHIL","DIV"]
tags2 = ["DATE"]
other_tags = ["INDI","FAM"]

for i in f:
    sys.stdout.write("-->" + i)

    lineArr = i.split()
    lev = int(lineArr[0])
    tag = lineArr[1]
    arg = ' '.join(lineArr[2:])

    if lev > 2:
        print("<--"+str(lev)+ "|"+tag+"|"+"N"+"|"+arg)
    elif (lev == 0 and tag in tags0) or (lev == 1 and tag in tags1) or (lev == 2 and tag in tags2):
        print("<--"+str(lev)+"|"+tag+"|"+"Y"+"|"+arg)
    elif lineArr[-1] in other_tags and lev == 0:
        print("<--"+str(lev)+"|"+str(lineArr[1])+"|"+"Y"+"|"+str(lineArr[-1]))
    else:
        print("<--"+str(lev)+ "|"+tag+"|"+"N"+"|"+arg)
    


