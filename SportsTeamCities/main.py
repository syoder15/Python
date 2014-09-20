'''

@author: Sam
Project that gives you the names of teams in a city
Also offers to open the team's website if so desired
'''

#Prompt user for which nba team they would like to 

from teamConversion import *

#new = 2

teamsDict = []


cityInput = ""


print "Entering 'exit' or 'quit' at any point in time will exit"
while cityInput.lower() != "quit" or cityInput.lower() != "exit" :
    cityInput = raw_input("Please enter a city for which you'd like to see the sports teams: ")
    #if they have elected to quit
    if cityInput.lower() == "quit" or cityInput.lower() == "exit" :
        print "Thank you!"
        break
        
    #If the city doesn't have a team
    if validCity(cityInput) != True:
        print "Sorry! That city does not have an NFL or NBA team."
    
    #city does have team
    #we want to list the teams in that city for them
    #then ask if they want to go to a specific team's website
    else :
        print "Here are the teams located in that city: "
        printTeams(cityInput)
        #ask if they would like to see one of the team websites
        teamInput = raw_input("Would you like to go to the website of one of these teams? (yes/no) ")
        
        while teamInput.lower() != "yes" and teamInput.lower() != "no" and teamInput.lower() != "quit" and teamInput.lower() != "exit":
            teamInput = raw_input("Sorry, expected response is a yes or a no. Would you like to go to the website of one of these teams? ")
        
        #prioritizing exit over everything
        if teamInput.lower() == "quit" or teamInput.lower() == "exit" :
            print "Thank you!"
            break
        
        #if they say yes, we want to ask them which team they'd like to see
        
        elif teamInput.lower() == "yes":
            teamInput = raw_input("Which of the teams would you like to see? ")
            
            #while the team they entered is misspelled
            while validTeam(cityInput, teamInput) != True:
                if teamInput.lower() == "quit" or teamInput.lower() == "exit" :
                    print "Thank you!"
                    break
                teamInput = raw_input("Sorry! You may have misspelled the team name, or not chosen one of the options. \nPlease try again: ")
            
            #Finally spelled the team correctly, or chose a proper team
            #we want to open the browser now
            openWebsite(cityInput, teamInput, cityAbbrev(cityInput))   

        #They answered no they would not
        #we must ask them to enter a city they'd like to see
        else :
            continue


