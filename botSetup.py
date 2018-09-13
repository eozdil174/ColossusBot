import json
import os

def getData():
    try:
        with open('botConfig.json', 'r') as data:           #Using Json library to load the botConfig file ('r' stands for "read". So the file won't be affected from any kind of write process)
            config = json.load(data)                        #Getting the data from the json file
    except:                                                 #Used try-except to create the file if it doesn't exists yet
        with open('botConfig.json', 'w+') as newFile:       #Creating the botConfig.json file. 'w+' stands for "write and create"
            config = json.dump({'name':' ', 'token' : '', 'game' : ''}, newFile)        #You can add extra settings as you need
        getData()        #Recalling the function to get the data after creating the json file
    return config

configData = {}             #An empty dictionary for storing settings
def showData():
    os.system('cls')        #Cleaning the cmd / terminal screen
    try:
        for setting, value in getData().items():        #For every setting - value pair,
            configData[setting] = value                 #Put the pair to the dictionary
            print ("%s : %s" % (setting, value))        #Print the pair to screen

        print ("\nIf you want to change the settings use => {Setting name} {new value}\nIf you want to exit, type 'exit' (This won't save the changes you've made)")

    except:
        showData()              #We need that try except to prevent getting No Value error. That error happens when the botConfig.json file doesn't exists


answer = ''         #An empty string for getting user input

while answer != 'exit':
    showData()      #Refreshing the menu after every command

    answer = input("\nInput : ")    #Getting input
    inputStrings = answer.split()   #Splitting the input into words and putting them into a list


    if inputStrings[0] in configData.keys():                            #inputStrings[0] is the first word the user types (for example "name" or "exit")
        configData[inputStrings[0]] = " ".join(inputStrings[1:])        #Updating the dictionary with the new data. The join function makes the list elements more cleaner (for example : "['name' , 'eozdil'] ==> name eozdil")
        with open("botConfig.json", 'w') as fp:                         #Opening the config file in write mode ('w')
            json.dump(configData, fp)                                   #Writing the changes to the json file

        print ("Setting value updated")
