from Program.Backend.Utils.configReading import readConfig
import pytextnow as texting


class TextService():
    def __init__(self):
        configFile = "ptnConfig.json"
        self.auth_data = readConfig(fileName=configFile)

        self.c = texting.Client(username=self.auth_data['username'], sid_cookie=self.auth_data['connect.sid'], csrf_cookie=self.auth_data['_csrf'])

    
    def reloadSystem(self, called):
        self.c = texting.Client(username=self.auth_data['username'], sid_cookie=self.auth_data['connect.sid'], csrf_cookie=self.auth_data['_csrf'])
        self.called()

    
    def recvMessage(self):
        try:
            new_messages = self.c.get_unread_messages()

        except:
            self.reloadSystem(self.recvMessage)
        
        for message in new_messages:
            message.mark_as_read()
            
            print(str(message.content))
            print(str(message.number))

            if message.content:    
                return [str(message.number), str(message.content)]
        return 0  


    def sendMessage(self, number, contents):
        try:
            self.c.send_sms(number, contents)

        except: 
            self.reloadSystem()
            self.c.send_sms(number, contents)

    
    def parseString(self, string, number):
        Messages = string.split("|")
            
        for message in Messages:
            self.sendMessage(number, message)

    
    def mainSetup(self):
        configFile = 'ptnconfig.json'
        config = readConfig(configFile)

        for item in config:
            if item == "setup":
                continue

            val = input("Please enter {} here:".format(item))
            config[item] = val






    