import tkinter as tk
from tkinter import ttk
import time

# Create window
root = tk.Tk()
root.title("Progress Bar Clock")
root.geometry("400x200")

# Clock label
time_label = tk.Label(root, font=("Arial", 30))
time_label.pack(pady=20)

# Progress bar for seconds
progress = ttk.Progressbar(root, orient="horizontal",
                           length=300, mode="determinate",
                           maximum=60)
progress.pack(pady=20)

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    seconds = int(time.strftime("%S"))

    # Update label
    time_label.config(text=current_time)

    # Update progress bar
    progress["value"] = seconds

    # Refresh every second
    root.after(1000, update_clock)

update_clock()

root.mainloop()
