try:
  import usocket as socket
except:
  import socket

from time import sleep

from machine import Pin, SoftI2C
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

import hardware

from sensors import BME280
from wifi import wifi
# import PMS5003
from machine import UART
from esp32_gpio_lcd import GpioLcd


# import PMS
# import PMSTEST

# ESP32 - Pin assignment
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
# ESP8266 - Pin assignment
# i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)



# uart = UART(1,baudrate=9600,tx=25,rx=26)
# uart.init(9600, parity=None, stop=1)
# pms = PMS5003.PMS5003(uart)
# pms.set_pms()
# print(pms.read_pms())

lcd = GpioLcd(rs_pin=Pin(19),
                  enable_pin=Pin(23),
                  d4_pin=Pin(18),
                  d5_pin=Pin(17),
                  d6_pin=Pin(16),
                  d7_pin=Pin(15),
                  num_lines=2, num_columns=20)

lcd.clear()
lcd.move_to(0, 0)
lcd.putstr("Starting wifi...")

lcd.putstr("\n%s" % wifi.connect())
sleep(3)

bme = BME280.BME280(i2c=i2c)

"""
import webserver.webserver as webserver
import uasyncio
loop = uasyncio.get_event_loop()
loop.create_task(webserver.run(bme))
loop.run_forever()
"""