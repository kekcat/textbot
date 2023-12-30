from datetime import datetime

timeName = "/time"
timeHelp = "Gets the current date and time"

def getTime(**kwargs):
    date = datetime.now()
    return f"{kwargs}" + date.strftime("%Y %b %d %I:%M%p, %H:%M:%S")
