'''

@author: Sam
File containing helper functions (such as getting the city abbreviation and checking if a team is in a city)
REMEMBER TO NORMALIZE NORMALIZE NORMALIZE
'''

from dictionary import *
import webbrowser
#Remember to normalize all things for dictionary

#gives the abbreviation of the city for the website's sake
def cityAbbrev(city):
    city = city.lower() #normalize
    return teamDict[city]["Abbrev"]

#go to city in the dictionary, and see if this particular team is there
def validTeam(city, givenTeam):
    #loop through the leagues
    city = city.lower() #normalize
    for league in teamDict[city] :
        #loop through teams in each league
        for team in teamDict[city][league] :
            #if the city has a team of that name confirm
            if team.lower() == givenTeam.lower() : #normalize
                return True
    #otherwise we are going to say no we don't have that guy
    return False

#checks whether this is a city in the dictionary
def validCity(city):
    city = city.lower() #normalize
    #use built in method to determine if city is in dictionary
    return teamDict.has_key(city)

def printTeams(city):
    city = city.lower() #normalize
    for league in teamDict[city]:
        if league != "Abbrev": #we do not want to print the city abbreviation
            for team in teamDict[city][league]:
                print team


def getLeague(city, team):
    city = city.lower()
    for league in teamDict[city] :
        #loop through teams in each league
        for dictTeam in teamDict[city][league] :
            #if the city has a team of that name confirm
            if dictTeam.lower() == team.lower() : #normalize
                return league


#opens up the website to a particular team
#using webbrowser.open
#HANDLE THE LA ISSUE
    #Clippers abbrev is lac, lakers lal, dodgers lad, angels laa
def openWebsite(city, team, abbrev):
    team = team.lower()
    #handling the la issue
    if team == "clippers" :
        abbrev = "lac"
    elif team == "lakers":
        abbrev = "lal"
    elif team == "giants":
        abbrev = "nyg"
    elif team == "jets":
        abbrev = "nyj"
    
    
   
    league = (getLeague(city, team)).lower()
    new = 2
    
    url = 'http://www.espn.go.com/%(league)s/team/_/name/%(abbreviation)s' % {"league" : league, "abbreviation" : abbrev}
    
    webbrowser.open(url, new)
    