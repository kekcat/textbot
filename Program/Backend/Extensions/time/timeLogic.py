from datetime import datetime

timeName = "/time"
timeHelp = "Gets the current date and time"

def getTime():
    date = datetime.now()
    return date.strftime("%Y %b %d %I:%M%p, %H:%M:%S")
