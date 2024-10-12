# simulation/tire_model.py

from config.parameters import (DEGRADATION_SOFT, DEGRADATION_MEDIUM, DEGRADATION_HARD,
                               HEAT_THRESHOLD_SOFT, HEAT_THRESHOLD_MEDIUM, HEAT_THRESHOLD_HARD, TEMPERATURE_EFFECT, TEMPERATURE_RACE)

# Tire class to handle degradation and temperature effects
class Tire:
    def __init__(self, compound):
        self.compound = compound
        self.degradation = 0.0  # Initial degradation
        self.temperature = TEMPERATURE_RACE  # Start at race temperature
        
        # Assign degradation stages and heat thresholds based on tire compound
        if compound == 'soft':
            self.degradation_stages = DEGRADATION_SOFT
            self.heat_threshold = HEAT_THRESHOLD_SOFT
        elif compound == 'medium':
            self.degradation_stages = DEGRADATION_MEDIUM
            self.heat_threshold = HEAT_THRESHOLD_MEDIUM
        else:
            self.degradation_stages = DEGRADATION_HARD
            self.heat_threshold = HEAT_THRESHOLD_HARD

    def update_tire_condition(self, lap, track_temperature):
        # Calculate temperature effect
        if track_temperature > self.heat_threshold:
            temperature_penalty = (track_temperature - self.heat_threshold) * TEMPERATURE_EFFECT
            self.degradation += temperature_penalty

        # Non-linear degradation model (based on wear stage)
        if lap < len(self.degradation_stages):
            self.degradation += self.degradation_stages[lap]
        else:
            # Final stage degradation (continue wearing at the last rate)
            self.degradation += self.degradation_stages[-1]

        return self.degradation

    def get_performance(self):
        # Performance drop as degradation increases
        return max(0, 1 - self.degradation)  # Performance between 0 and 1