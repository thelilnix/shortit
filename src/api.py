"""API module for connecting and preparing results."""

import requests
import properties

class UrlAPI:
    def __init__(self):
        self.__long_url = ""

    def set_url(self, url):
        self.__long_url = url

    def request_short_url(self):
        
        try:
            result = requests.get(properties.API_URL + self.__long_url)
        except ConnectionError as err:
            return -1, err

        return result
