from machine import Pin
from dht import DHT11
from time import sleep

dht11 = DHT11(Pin(15))
fan = Pin(13, Pin.OUT)

while True:
    dht11.measure()
    temp = dht11.temperature()
    if temp > 32:
        fan.on()
    else:
        fan.off()
    sleep(1)
