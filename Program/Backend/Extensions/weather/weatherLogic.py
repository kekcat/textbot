from Program.Utils.configReading import readConfig
from datetime import datetime 

config = '/Program/Extensions/weather/weatherConfig.json'
weatherName = "/getweather"
weatherHelp = "NA"

def convert(val):
    val -= 273.15
    val = val * 9/5
    val += 32
    return round(val)
 

def get_weather():
    now = datetime.now()
    data = readConfig(config)

    if data == "":
        return "no api key"
    
    ret = '''Location: {}, {}|
    Conditions: {}|
    Temp: {} F, Feels like: {} F, High: {} F, Low: {} F|
    Pressure: {} hPa|
    Humidity: {}%|
    Visibility: {} meters|
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

    return "time: {} weather:".format(cur_time) + lines
