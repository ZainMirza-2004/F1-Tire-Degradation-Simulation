# strategy/pit_strategy_ml.py

from config.parameters import PIT_STOP_TIME, TOTAL_LAPS

# Simplified ML pit strategy (could be replaced with actual ML model)
def decide_pit_strategy(car, current_lap):
    # Simple rule-based strategy: pit once between lap 30 and 40
    if 30 <= current_lap <= 40:
        # Example: pit if the car is on soft tires and it's worn out
        if car.tire.degradation > 0.5:  # Threshold for wear
            print(f"Car {car.car_id} is pitting on lap {current_lap}")
            return True
    return False