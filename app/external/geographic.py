import aiohttp
from functools import lru_cache
from app.config import external_data
from app.handlers.exceptions import TownNotFoundException
from app.schemas import GeographicDataResponse


class Geographic:

    def __init__(self):
        self._distance_service_url = external_data.distance_service_url
        self._geocoding_service_url = external_data.geocoding_service_url
        self._distance_api_key = external_data.distance_api_key
        self._geocoding_api_key = external_data.geocoding_api_key

    def _get_distance_headers(self):
        headers = {
            "Content-Type": "application/json",
            "X-RapidAPI-Key": self._distance_api_key,
            "X-RapidAPI-Host": "distance-calculator.p.rapidapi.com"
        }
        return headers

    def _get_geocoding_headers(self):
        headers = {
            "X-RapidAPI-Key": self._geocoding_api_key,
            "X-RapidAPI-Host": "google-maps-geocoding.p.rapidapi.com"
        }
        return headers

    @staticmethod
    def _make_distance_query(lat_1: str, long_1: str, lat_2: str, long_2: str):
        querystring = {"lat_1": lat_1, "long_1": long_1, "lat_2": lat_2, "long_2": long_2,
                       "unit": "kilometers ", "decimal_places": "0"}
        return querystring

    async def get_distance(self, lat_1: str, long_1: str, lat_2: str, long_2: str):
        headers = self._get_distance_headers()
        params = self._make_distance_query(lat_1=lat_1, long_1=long_1, lat_2=lat_2, long_2=long_2)
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self._distance_service_url, headers=headers, params=params) as resp:
                return await resp.json()

    @staticmethod
    def _make_geographic_data_query(address: str, language: str):
        querystring = {"address": address, "language": language}
        return querystring

    async def _get_geographic_data(self, address: str, language: str):
        headers = self._get_geocoding_headers()
        params = self._make_geographic_data_query(address=address, language=language)
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self._geocoding_service_url, headers=headers, params=params) as resp:
                return await resp.json()

    async def get_geographic_coordinates(self, address: str, language: str):
        data = await self._get_geographic_data(address=address, language=language)
        if not data.get("results"):
            raise TownNotFoundException("Can't find town with this name. Try with another language")

        coordinates = data.get('results')[0].get('geometry').get('location')
        country = data.get('results')[0].get('address_components')[0].get('long_name')
        return GeographicDataResponse(latitude=coordinates["lat"], longitude=coordinates['lng'], country=country)

    # async def get_country(self, address: str, language: str):
    #     data = await self._get_geographic_data(address=address, language=language)
    #     if not data.get("results"):
    #         raise TownNotFoundException("Can't find town with this name. Try with another language")
    #
    #     country = data.get('results')[0].get('address_components')[0].get('long_name')
    #     return country


geographic_handler = Geographic()
