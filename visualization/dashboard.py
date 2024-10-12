# visualization/dashboard.py

import tkinter as tk
from tkinter import ttk

# Real-time dashboard using Tkinter
def create_dashboard():
    root = tk.Tk()
    root.title("Race Monitoring Dashboard")

    # Frame for showing lap times
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Example table
    tree = ttk.Treeview(frame, columns=("Car", "Lap", "Lap Time"))
    tree.heading('#0', text="ID")
    tree.heading('#1', text="Car")
    tree.heading('#2', text="Lap")
    tree.heading('#3', text="Lap Time")

    tree.grid(row=0, column=0)

    # Populate with sample data (this would come from the simulation)
    for i in range(5):
        tree.insert("", tk.END, text=f"{i}", values=(f"Car {i}", "Lap 1", "90.5 sec"))

    root.mainloop()

if __name__ == "__main__":
    create_dashboard()