from machine import Pin
from dht import DHT11
from time import sleep

dht11 = DHT11(Pin(15))

while True:
    dht11.measure()
    temp = dht11.temperature()
    humid = dht11.humidity()
    print("Temperature: %.2f degree celsius; Humidity: %.2f percent" % (temp, humid))
    sleep(1)