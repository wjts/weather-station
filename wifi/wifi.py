import json
import network

def connect():
    station = network.WLAN(network.STA_IF)

    if station.isconnected():
        print(station.ifconfig())
        return

    with open('wifi/config.json') as f:
        config = json.load(f)

    station.active(True)
    station.connect(config['ssid'], config['password'])

    while not station.isconnected():
        pass

    print(station.ifconfig())
    return station.ifconfig()[0]
