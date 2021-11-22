import configparser
import json

import requests

config = configparser.ConfigParser()
config.read('config.txt')


class Weather:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}"
                                .format(lat, lon, config.get('Weather', 'apikey')))
        print(response.json())


def main():
    Weather(44.8113, -91.4985)


if __name__ == "__main__":
    main()
