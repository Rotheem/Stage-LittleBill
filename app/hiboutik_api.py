import logging
from fastapi import Depends
import requests

from app.dependencies import get_settings
from app.settings import Settings


logger = logging.getLogger("logger")


def get_hiboutik_api(settings: Settings = Depends(get_settings)):
    return HiboutikAPI(settings)


class HiboutikAPI:
    def __init__(self, settings: Settings):
        self.url = settings.HIBOUTIK_API_URL
        self.user = settings.HIBOUTIK_API_USER
        self.key = settings.HIBOUTIK_API_KEY

    def treat_response(self, response: requests.Response) -> dict | list[dict] | str:
        try:
            response.raise_for_status()
            logger.debug(response.json())
            return response.json()
        except Exception:
            logger.error(response.text)
            return response.text

    def get(self, url, params=None, json=None):
        with requests.get(
            self.url + url,
            params=params,
            json=json,
            auth=(self.user, self.key),
        ) as response:
            return self.treat_response(response)

    def post(self, url, params=None, json=None):
        with requests.post(
            self.url + url,
            params=params,
            json=json,
            auth=(self.user, self.key),
        ) as response:
            return self.treat_response(response)

    def put(self, url, params=None, json=None):
        with requests.put(
            self.url + url,
            params=params,
            json=json,
            auth=(self.user, self.key),
        ) as response:
            return self.treat_response(response)

    def delete(self, url, params=None, json=None):
        with requests.delete(
            self.url + url,
            params=params,
            json=json,
            auth=(self.user, self.key),
        ) as response:
            return self.treat_response(response)

    def patch(self, url, params=None, json=None):
        with requests.patch(
            self.url + url,
            params=params,
            json=json,
            auth=(self.user, self.key),
        ) as response:
            return self.treat_response(response)
