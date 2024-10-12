# simulation/race_simulation.py

from config.parameters import (NUM_CARS, INITIAL_LAP_TIME, DRIVER_CONSISTENCY, TOTAL_LAPS, PIT_STOP_TIME, FUEL_LOAD_EFFECT)
from environment.track_conditions import get_track_temperature
from strategy.pit_strategy_ml import decide_pit_strategy
from simulation.tire_model import Tire

import random

class Car:
    def __init__(self, car_id, tire_compound):
        self.car_id = car_id
        self.tire = Tire(tire_compound)
        self.lap_time = INITIAL_LAP_TIME[tire_compound]
        self.fuel_load = 100  # Starting with 100kg of fuel
    
    def simulate_lap(self, lap, track_temperature):
        # Simulate tire degradation and update performance
        degradation = self.tire.update_tire_condition(lap, track_temperature)
        performance = self.tire.get_performance()

        # Adjust lap time based on fuel load, degradation, and driver variability
        fuel_effect = (self.fuel_load / 10) * FUEL_LOAD_EFFECT
        driver_variability = random.uniform(-DRIVER_CONSISTENCY, DRIVER_CONSISTENCY)
        
        self.lap_time = INITIAL_LAP_TIME[self.tire.compound] + fuel_effect + (1 - performance) * degradation + driver_variability

        # Burn fuel per lap (simplified)
        self.fuel_load -= 2  # Burn 2 kg of fuel per lap

        return self.lap_time

class RaceSimulation:
    def __init__(self):
        self.cars = [Car(i, random.choice(['soft', 'medium', 'hard'])) for i in range(NUM_CARS)]
        self.track_temperature = get_track_temperature()

    def run_race(self, lap_times):
        for lap in range(TOTAL_LAPS):
            for car in self.cars:
                lap_time = car.simulate_lap(lap, self.track_temperature)
                pit_stop = decide_pit_strategy(car, lap)
                
                if pit_stop:
                    lap_time += PIT_STOP_TIME

                lap_times[car.car_id].append(lap_time)

                print(f"Car {car.car_id} completed lap {lap} with lap time {lap_time:.2f} seconds")

    def plot_results(self, lap_times):
        # Visualization of the race results using the lap times
        print("Plotting results... (implement the plotting logic here)")