from typing import List
from pydantic import BaseModel

class Fuels(BaseModel):
    gas_price: float
    kerosine_price: float
    co2_cost: float
    wind_speed: float

class PowerPlant(BaseModel):
    name: str
    type: str
    efficiency: float 
    pmax: float
    pmin: float

class Payload_total(BaseModel):
    load: float
    fuels: Fuels 
    powerplants: List[PowerPlant] 