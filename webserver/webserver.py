import tinyweb


# Create web server application
app = tinyweb.webserver()

bme_sensor = None

# Index page
@app.route('/')
async def index(request, response):
    # Start HTTP response with content-type text/html
    await response.start_html()
    # Send actual HTML page
    await response.send("""
    <html>
    <head>
        <title>Weather Station v0.0.1 ;)</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <p>Wilgotność: %s</p>
        <p>Ciśnienie: %s</p>
        <p>Temperatura: %s</p>
    </body>
    </html>
    """ % (bme_sensor.humidity, bme_sensor.pressure, bme_sensor.temperature))


def run(ip, bme):
    global bme_sensor
    bme_sensor = bme
    app.run(host=ip, port=80)