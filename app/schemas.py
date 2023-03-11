from pydantic import BaseModel


class GeographicDataResponse(BaseModel):
    latitude: float
    longitude: float
    country: str
