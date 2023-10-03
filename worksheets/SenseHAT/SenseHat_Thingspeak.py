from sense_hat import SenseHat
import requests
from time import sleep

sense = SenseHat()
sense.set_rotation(180)

red=[150,0,0]
green = [0,150,0]
blue = [0,0,150]

thingspeak_address = "https://api.thingspeak.com/update?api_key="

api_key = "7WFRBE3A9W6GRHYG"

def send_temperature():
    temperature = round(sense.get_temperature(), 2)
    print("The Temperature is ", temperature)
    reading = str(temperature)
    sense.show_message("Temperature is " + reading, text_colour=red)
    response = requests.post(thingspeak_address + api_key + "&field1=" + reading)
    print(response)

def send_pressure():
    pressure = round(sense.get_pressure(), 2)
    print("The pressure is ", pressure)
    reading = str(pressure)
    sense.show_message("Pressure is " + reading, text_colour=green)
    response = requests.post(thingspeak_address + api_key + "&field2=" + reading)
    print(response)

def send_humidity():
    humidity = round(sense.get_humidity(), 2)
    print("The humidity is ", humidity)
    reading = str(humidity)
    sense.show_message("Humidity is " + reading, text_colour=blue)
    response = requests.post(thingspeak_address + api_key + "&field3=" + reading)
    print(response)

    
while True:
    send_temperature()
    sleep(15)
    send_pressure()
    sleep(15)
    send_humidity()
    sleep(15)
