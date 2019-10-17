import gedComProj.src.utils as utils
import datetime

def addAgeToIndividual(individual):
    currentDate = datetime.date.today()
    indAge = utils.calculateAge(individual, currentDate)
    individual["AGE"]= indAge
    return

def addAgeToAll(individualDict):
    for key in individualDict.keys():
        addAgeToIndividual(individualDict[key])
    return