# visualization/plot_results.py

import matplotlib.pyplot as plt

def plot_lap_times(lap_times):
    plt.figure(figsize=(10, 6))
    for car_id, times in lap_times.items():
        plt.plot(times, label=f"Car {car_id}")

    plt.title("Lap Times")
    plt.xlabel("Lap")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_tire_wear(tire_wear):
    plt.figure(figsize=(10, 6))
    for car_id, wear in tire_wear.items():
        plt.plot(wear, label=f"Car {car_id}")

    plt.title("Tire Wear Over Time")
    plt.xlabel("Lap")
    plt.ylabel("Tire Wear")
    plt.legend()
    plt.grid(True)
    plt.show()