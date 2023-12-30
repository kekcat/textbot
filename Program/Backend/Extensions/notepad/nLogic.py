import numbers
from Program.Backend.Utils.configReading import readConfig, updateConfig


notes = readConfig("Program/Backend/Extensions/notepad/notepadData.json")


def createNotepad(**kwargs):
    notes[kwargs] = ''

    return "Notepad created, /notepadwrite to add text"


def writeNotepad(**kwargs):
    number = kwargs[0]
    data = kwargs[1]

    try:
        notes[number] = data
        return "Successfully written"

    except:
        return "Notepad not created, use /createnotepad"


def deleteNotepad(**kwargs):
    try:
        notes[kwargs] = ''
        return "Notepad data deleted"

    except:
        return "Notepad not yet created"


