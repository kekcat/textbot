from Program.Backend.Texting.TextingService import TextService


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

        newCommand = Command(function=self.helpCommand, name="/mynumber", helpString="Shows the current number being texted")
        self.commands["/mynumber"] = newCommand

    
    def addExtension(self, function, name, helpString):
        newCommand = Command(function=function, name=name, helpString=helpString)

        self.commands[str(newCommand.name)] = newCommand

    
    def recvLoop(self, textingContainer):
        data = textingContainer.recvMessage()

        if data != 0:
            self.content = data[1]
            self.number = data[0]
            print(f"Message from {self.number}, Contents {self.content}")
            
            try:
                if self.content.isspace():
                    self.content.split(' ')
                    
                    Command = self.commands[str(self.content[0])]
                    retString = Command.function(self.number, self.content[1])
                    print(f"To {self.number}, Returning {retString}, Command {self.content[0]}")
                    textingContainer.parseString(retString, str(self.number))

                else:
                    Command = self.commands[str(self.content)]
                    retString = Command.function(self.number)
                    print(retString)
                    textingContainer.parseString(retString, str(self.number))
                    
            except KeyError:
                textingContainer.sendMessage(self.number, "invalid command")
                print(f"Invalid command, Contents {self.content}")

    ghf
    def helpCommand(self):
        helpList = []
        
        for command in self.commands:
            commandObject = self.commands[command]

            help = commandObject.helpString
            name = commandObject.name

            helpList.append("{} - {}".format(name, help))

        return "|".join(helpList)

    
    def getNumber(self):
        return "Your number is {}".format(self.number)







    

    

        