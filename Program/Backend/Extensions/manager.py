from Program.Backend.Extensions.weather.weatherLogic import get_weather, weatherHelp, weatherName
from Program.Backend.Extensions.time.timeLogic import getTime, timeHelp, timeName

def loadExtensions(messageContainer):
    messageContainer.addExtension(function=get_weather, name=weatherName, helpString=weatherHelp)
    messageContainer.addExtension(function=getTime, name=timeName, helpString=timeHelp)


