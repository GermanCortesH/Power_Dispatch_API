# Codigo para fastapi
from fastapi import FastAPI
import uvicorn
from .models import Payload_total
app = FastAPI()

@app.post("/productionplan")
def calculate_production_plan(data_received: Payload_total):
    dispatch_list = []
    
    gas_price = data_received.fuels.gas_price
    co2_cost = data_received.fuels.co2_cost
    
    for plant in data_received.powerplants:
        ## costo marginal
        CM = 0.0
        max_available_p = plant.pmax

        if plant.type == "gasfired":
            cm_base = gas_price / plant.efficiency
            co2_cost_per_mwh = co2_cost * 0.3
            CM = cm_base + co2_cost_per_mwh
            
        elif plant.type == "turbojet":
            kerosine_price = data_received.fuels.kerosine_price
            CM = kerosine_price / plant.efficiency

        elif plant.type == "windturbine":
            CM = 0.0
            max_available_p = plant.pmax * (data_received.fuels.wind_speed / 100)

        dispatch_list.append({
            "name": plant.name,
            "cost": CM,
            "pmin": plant.pmin,
            "pmax_available": max_available_p,
            "assigned_p": 0.0 
        })
    dispatch_list.sort(key=lambda item: item['cost'])

    load_remaining = data_received.load
    total_data=[]

    for plant_data in dispatch_list:
        if load_remaining <= 0: 
            break
        if plant_data["cost"] >= 0.0:
            p_assigned = min(plant_data["pmax_available"], load_remaining)
            plant_data["assigned_p"] = p_assigned
            load_remaining -= p_assigned

    for plant_data in dispatch_list:
        total_data.append({
            "name": plant_data["name"],
            "p": round(plant_data["assigned_p"], 1) 
        })
        
    return total_data

        

                    


