from configReading import readConfig, updateConfig #Neccesary imports

templateName = "/template"
templateHelp = "template help"

configFile = '' #Define optional config file for api keys, data, etc.
data = readConfig(configFile) # Reading config

def logic(): #Logic/code goes here
    return 0 #Return the message to be sent, be sure to include '/' to specify newlines. Too long of a string will result in failure to send.

