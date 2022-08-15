from Program.Backend.Extensions.manager import loadExtensions
from Program.Backend.Texting.CommandModel import Message
from Program.Backend.Texting.TextingService import TextService
from Program.Backend.Extensions.manager import loadExtensions


def testing():
    messageContainer = Message()
    textingContainer = TextService()
    loadExtensions(messageContainer)
    
    while 1:
        messageContainer.recvLoop(textingContainer)
