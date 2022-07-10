import requests as req
import json
from datetime import datetime
import pytextnow as ptn
from json_functions import file

config_file = 'config.json'
main_config = file(config_file)
auth_data = main_config.read()

c = ptn.Client(username=auth_data['username'], sid_cookie=auth_data['connect.sid'], csrf_cookie=auth_data['_csrf'])

def convert(val):
    val -= 273.15
    val = val * 9/5
    val += 32
    return round(val)

class main_commands:
    def __init__(self, number):
        self.number = number
        print(number)

        self.send('welcome {}'.format(number))
        self.send('type /help for help')

    def __del__(self):
        print("closing instance")
        self.send("closing, see you later!")

    def get_weather(self):
        now = datetime.now()
        weather_api_call = auth_data['weather_api']

        if weather_api_call == "":
            self.send("no api key")
            return 0

        w = req.get(weather_api_call)
        data = json.loads(w.text)
        print(data)
        
        ret = '''Location: {}, {}
        Conditions: {}
        Temp: {} F, Feels like: {} F, High: {} F, Low: {} F
        Pressure: {} hPa
        Humidity: {}%
        Visibility: {} meters
        Wind: {} met/sec '''

        lon = data['coord']['lon']
        lat = data['coord']['lat']
        sky = data['weather'][0]['main']
        t = data['main']['temp']
        feels = data['main']['feels_like']
        max = data['main']['temp_max']
        min = data['main']['temp_min']
        t = convert(t)
        feels = convert(feels)
        max = convert(max)
        min = convert(min)
        pres = data['main']['pressure']
        hum = data['main']['humidity']
        visi = data['visibility']
        speed = data['wind']['speed']
        final = ret.format(lon, lat, sky, t, feels, max, min, pres, hum, visi, speed)
        lines = final.split("\n")

        cur_time = now.strftime("%H:%M:%S")

        self.send("time: {} weather:".format(cur_time))
        for l in lines:
            self.send(l)

    def get_datetime(self):
        date = datetime.now()
        self.send(date.strftime("%Y %b %d %I:%M%p, %H:%M:%S"))

    def help(self):
        help_string = ['/weather - get weather data', '/time - get time data', '/auth [password] - auth for more commands, input password', '/close - close current text instance']

        for m in help_string:
            self.send(m)

        return 0

    def print_identity(self):
        return self

    def input_message(self, text_data):
        
        print(self.number)
        text_data = str(text_data)
        if text_data:
            text_data.split(' ')
            
            if text_data == '/weather':
                self.get_weather()
            
            elif text_data == '/help':
                self.help()
            
            elif text_data == '/time':
                self.get_datetime()
            
            elif text_data == '/date':
                self.get_datetime()
            
            elif text_data == '/close':
                self.__del__
            
            else:
                print("invalid")
                self.send("invalid command")
        
        return 0
    
    def send(self, con):
        print(con)
        c.send_sms(str(self.number), con)

def ptn_init(ac_numbers):
    print("STARTING...")

    texting_controller(ac_numbers)

def recv_message(): 
    new_messages = c.get_unread_messages()
    for message in new_messages:
        message.mark_as_read()

        if message.content:    
            return str(message.number), str(message.content)
    return 0, 0 

def new_inst(instance_number):
    globals()[f"{instance_number}"] = main_commands(number=instance_number)

def texting_controller(ac_numbers):
    print("READY")

    while 1:
        num, con = recv_message()
        if num != 0:    
            if num in ac_numbers:
                globals()[str(num)].input_message(text_data=con)
            else:
                ac_numbers.append(num)
                new_inst(num)

def send(num, con):
    c.send_sms(num, con)






