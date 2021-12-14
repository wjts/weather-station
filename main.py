import webserver.webserver as webserver
import uasyncio

def print_humidity():
  lcd.putstr("Wilgotnosc\n   %s" % bme.humidity)

def print_pressure():
  lcd.putstr("Cisnienie\n   %s" % bme.pressure)

def print_temperature():
  lcd.putstr("Temperatura\n    %s" % bme.temperature)

async def handle_webserver():
  await webserver.run(bme)

async def handle_lcd():
  while True:
    for func in (print_humidity, print_pressure, print_temperature):
      lcd.clear()
      lcd.move_to(0, 0)
      func()
      uasyncio.sleep(10)


async def main():
  # await uasyncio.create_task(handle_webserver())
  # await uasyncio.create_task(handle_lcd())
  loop = uasyncio.get_event_loop()
  loop.create_task(handle_webserver())
  loop.create_task(handle_lcd())
  loop.run_forever()


