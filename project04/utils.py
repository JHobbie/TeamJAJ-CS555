import datetime


def calcDate(dateString):
    return datetime.datetime.strptime(dateString, '%d %b %Y')

def writeErrors(errorList, file):
    for error in errorList:
        file.write(error + "\n")
    return