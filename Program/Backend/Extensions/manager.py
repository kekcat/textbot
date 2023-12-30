from Program.Backend.Extensions.weather.weatherLogic import get_weather, weatherHelp, weatherName
from Program.Backend.Extensions.time.timeLogic import getTime, timeHelp, timeName
from Program.Backend.Extensions.notepad.nLogic import createNotepad, writeNotepad, deleteNotepad

def loadExtensions(messageContainer):
    messageContainer.addExtension(function=get_weather, name=weatherName, helpString=weatherHelp)
    messageContainer.addExtension(function=getTime, name=timeName, helpString=timeHelp)
    messageContainer.addExtension(function=createNotepad, name="/createnotepad", helpString='')
    messageContainer.addExtension(function=writeNotepad, name="/notepadwrite", helpString='')
    messageContainer.addExtension(function=deleteNotepad, name="/deletenotepad", helpString='')


