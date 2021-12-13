from utime import sleep_ms

def print_humidity():
  lcd.putstr("Wilgotnosc\n   %s" % bme.humidity)

def print_pressure():
  lcd.putstr("Cisnienie\n   %s" % bme.pressure)

def print_temperature():
  lcd.putstr("Temperatura\n    %s" % bme.temperature)

while True:
  for func in (print_humidity, print_pressure, print_temperature):
    lcd.clear()
    lcd.move_to(0, 0)
    func()
    sleep_ms(10000)
