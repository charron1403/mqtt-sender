import RPi.GPIO as GPIO
import dht11
import paho.mqtt.client as mqtt

if __name__ == '__main__':
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    client = mqtt.Client()

    client.connect("10.4.1.42", 1883, 60)

    instance = dht11.DHT11(pin=17)

    while 1:
        result = instance.read()

        if result.is_valid():
            client.publish("XX/temp/sensor", "Temp: %-3.1f" % result.temperature)
