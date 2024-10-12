# config/parameters.py

# Tire degradation (non-linear model based on wear stages)
DEGRADATION_SOFT = [0.1, 0.2, 0.3]  # Different wear rates at different stages (non-linear)
DEGRADATION_MEDIUM = [0.07, 0.15, 0.25]
DEGRADATION_HARD = [0.05, 0.10, 0.18]

# Tire overheating performance penalties (performance drops drastically with heat)
HEAT_THRESHOLD_SOFT = 120  # Degrees Celsius
HEAT_THRESHOLD_MEDIUM = 110
HEAT_THRESHOLD_HARD = 100

# Temperature effect on degradation (race temperature range)
TEMPERATURE_RACE = 80.0  # Race temperature in degrees Celsius
TEMPERATURE_EFFECT = 0.001  # Percentage increase in degradation per degree over 30°C

# Race parameters
TOTAL_LAPS = 70  # Total race laps
TRACK_LENGTH = 5.0  # Length of the track in kilometers
LAP_TIME_BASE = 90.0  # Base lap time in seconds for ideal conditions

# Pit stop parameters
PIT_STOP_TIME = 25  # Time in seconds for a pit stop
FUEL_LOAD_EFFECT = 0.05  # Seconds per lap slower for every 10kg of fuel

# Weather conditions and effect on grip
WEATHER_CONDITIONS = {
    "sunny": 1,    # Full grip
    "rain": 0.8,   # Reduced grip
    "wet": 0.6     # Significantly reduced grip
}

# Tire degradation rates for different compounds (linear rates)
TIRE_DEGRADATION_RATE = {
    'soft': 0.02,   # Fastest degradation
    'medium': 0.015,
    'hard': 0.01    # Slowest degradation
}

# Initial lap times for different tire compounds (in seconds)
INITIAL_LAP_TIME = {
    'soft': 90.0,   # Soft tires provide the fastest initial lap
    'medium': 91.0,
    'hard': 92.0
}

# Performance drop per lap for different tire compounds
PERFORMANCE_DROP_SOFT = 0.05  # Soft tire performance drop per lap
PERFORMANCE_DROP_MEDIUM = 0.03  # Medium tire performance drop per lap
PERFORMANCE_DROP_HARD = 0.02  # Hard tire performance drop per lap

# Driver parameters
DRIVER_CONSISTENCY = 0.05  # Variability in lap times due to driver skill
NUM_CARS = 5  # Define the number of cars in the race simulation

# Additional constants (if required)
FUEL_LOAD_INITIAL = 100  # Initial fuel load in kg