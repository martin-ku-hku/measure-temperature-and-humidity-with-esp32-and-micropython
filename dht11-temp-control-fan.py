from machine import Pin, PWM
from dht import DHT11
from time import sleep

dht11 = DHT11(Pin(15))
fan = PWM(Pin(13))

while True:
    dht11.measure()
    temp = dht11.temperature()
    if temp < 32:
        fan.duty(0)
    elif temp >= 32 and temp < 35:
        fan.duty(512)
    else:
        fan.duty(1023)
    sleep(1)
