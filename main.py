import webserver.webserver as webserver
import uasyncio

def print_humidity():
  humidity = bme.humidity
  lcd.putstr("Wilgotnosc\n   %s" % humidity)
  print("Wilgotnosc\n   %s" % humidity)

def print_pressure():
  pressure = bme.pressure
  lcd.putstr("Cisnienie\n   %s" % pressure)
  print("Cisnienie\n   %s" % pressure)

def print_temperature():
  temperature = bme.temperature
  lcd.putstr("Temperatura\n    %s" % temperature)
  print("Temperatura\n    %s" % temperature)

async def handle_webserver():
  await webserver.run(ip_address, bme)

async def handle_lcd():
  while True:
    for func in (print_humidity, print_pressure, print_temperature):
      lcd.clear()
      lcd.move_to(0, 0)
      func()
      await uasyncio.sleep(10)


async def main():
  uasyncio.create_task(handle_lcd())
  uasyncio.create_task(handle_webserver())

  # this line must be here! otherwise it isnt working...
  await uasyncio.sleep(1)

uasyncio.run(main())