import requests
from sense_hat import SenseHat
from sensor import value
import time

while True:
    data = {
    'humidity' : value(),
    'location' : 'swe',
    'dateTime' : time.ctime()
    }
    formResponse = requests.post(
        url = 'http://192.168.0.49:5000/Upload',
        data=data ,
        headers= {
            'Content-Type': 'application/x-www-form-urlencoded'
        })
    time.sleep(10)

