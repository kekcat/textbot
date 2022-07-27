from Program.Extensions.manager import loadExtensions
from Program.Texting.CommandModel import Message
from Program.Texting.TextingService import TextService
from Program.Extensions.manager import loadExtensions


def testing():
    messageContainer = Message()
    textingContainer = TextService()
    loadExtensions(messageContainer)
    
    while 1:
        messageContainer.recvLoop(textingContainer)
