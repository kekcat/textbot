#from Extensions.extensionTemplate.templateLogic import logic, templateHelp, templateName
from Program.Extensions.weather.weatherLogic import get_weather, weatherHelp, weatherName

def loadExtensions(messageContainer):
    messageContainer.addExtension(function=get_weather, name=weatherName, helpString = weatherHelp)
    #messageContainer.addExtension(function=logic, name=templateHelp, helpString=templateName)


