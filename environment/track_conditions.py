# environment/track_conditions.py

from config.parameters import WEATHER_CONDITIONS, TEMPERATURE_RACE
import random

def get_weather_condition():
    return random.choice(list(WEATHER_CONDITIONS.keys()))

def get_track_temperature():
    weather = get_weather_condition()
    # Adjust track temperature based on weather condition
    if weather == "sunny":
        return TEMPERATURE_RACE + 5  # Hotter track
    elif weather == "rain":
        return TEMPERATURE_RACE - 5  # Cooler track
    else:
        return TEMPERATURE_RACE - 10  # Wet track, much cooler