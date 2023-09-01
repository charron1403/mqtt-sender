import time

import RPi.GPIO as GPIO
import dht11
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    client.subscribe("XX/temp/sensor")

if __name__ == '__main__':
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect("10.4.1.42", 1883, 60)

    instance = dht11.DHT11(pin=17)

    while 1:
        result = instance.read()

        if result.is_valid():
            client.publish("Temp: %-3.1f C" % result.temperature)
