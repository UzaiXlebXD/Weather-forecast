import pyowm

owm = pyowm.OWM('df7bea93a7cea46f88f5881f827da9e5', language = "ru")

place = input("В каком вы городе?: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]
wind = w.get_wind()["speed"]

print("В городе " + place + " сейчас " + w.get_detailed_status())
print("Температрура сейчас в районе " + str(temp))
print("Скорость ветра сейчас " + str(wind))

if wind == 0:
    print("На улице нет ветра")
elif wind < 10:
    print("На улице слабый ветер")
elif wind < 20:
    print("На улице ветер")
else:
    print("На улице сильный ветер")

if temp < 3:
    print("На улице очень холодно, одевайся очень тепло")
elif temp < 10:
    print("На улице холодно,одевайся очень тепло ")
elif temp < 20:
    print("На улице прохладно одевайся потеплее ")
else:
    print("На улице тепло одевайся как тебе удобно")

input()