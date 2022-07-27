from Program.Texting.TextingService import TextService


class Command:
    def __init__(self, function, name, helpString = "None"):
        self.helpString = helpString
        self.function = function
        self.name = name
        self.enabled = True


class Message:
    def __init__(self):
        self.commands = {}

        newCommand = Command(function=self.helpCommand, name="/help", helpString="displays info for all commands")
        self.commands["/help"] = newCommand

    
    def addExtension(self, function, name, helpString):
        newCommand = Command(function=function, name=name, helpString=helpString)

        self.commands[str(newCommand.name)] = newCommand

    
    def recvLoop(self, textingContainer):
        data = textingContainer.recvMessage()

        if data != 0:
            content = data[1]
            number = data[0]
            
            try:
                Command = self.commands[str(content)]
                retString = Command.function()
                print(retString)
                textingContainer.parseString(retString, str(number))
            
            except KeyError:
                textingContainer.sendMessage(number, "invalid command")

    
    def helpCommand(self):
        helpList = []
        
        for command in self.commands:
            commandObject = self.commands[command]

            help = commandObject.helpString
            name = commandObject.name

            helpList.append("{} - {}".format(name, help))

        return "|".join(helpList)






    

    

        