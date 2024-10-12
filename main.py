from config.parameters import NUM_CARS, TOTAL_LAPS  # Import TOTAL_LAPS from parameters
from simulation.race_simulation import RaceSimulation
from visualization.plot_results import plot_lap_times, plot_tire_wear

def main():
    race = RaceSimulation()  # Create an instance of RaceSimulation
    
    lap_times = {i: [] for i in range(NUM_CARS)}
    tire_wear = {i: [] for i in range(NUM_CARS)}
    
    for lap in range(TOTAL_LAPS):  # Use TOTAL_LAPS from parameters
        print(f"\n--- Starting lap {lap + 1}/{TOTAL_LAPS} ---")  # Indicate which lap is running
        
        for car in race.cars:
            lap_time = car.simulate_lap(lap, race.track_temperature)
            
            # Store results
            lap_times[car.car_id].append(lap_time)
            tire_wear[car.car_id].append(car.tire.degradation)
            
            # Print the car's lap time and tire degradation for debugging
            print(f"Car {car.car_id}: Lap time: {lap_time:.2f} seconds, Tire wear: {car.tire.degradation:.2f}%")
    
    # After the race, plot the results
    plot_lap_times(lap_times)
    plot_tire_wear(tire_wear)

if __name__ == "__main__":
    main()