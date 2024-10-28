#!/usr/bin/env python3

import json
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Define the file path
filepath = "/0.myfiles/notify.array"

# Load the data from the file
with open(filepath, 'r') as file:
    main_array = json.load(file)

# Function to parse 2D array and check for time match
def parse_and_notify(array):
    for sub_array in array:
        time_value = None
        desc_value = None

        # Search for pairs with specified keys
        for pair in sub_array:
            if pair[0] == "time":
                time_value = pair[1]
            elif pair[0] == "desc":
                desc_value = pair[1]

        # Check if current time matches the time_value and show notification
        if time_value and desc_value:
            current_time = datetime.now().strftime("%Y.%m.%d.%H.%M")
            if current_time == time_value:
                show_notification(time_value, desc_value)

# Function to show a pop-up message and log the message to the terminal on close
def show_notification(time_value, desc_value):
    # Display the pop-up message
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Notification", f"Time: {time_value}\nDescription: {desc_value}")
    root.destroy()
    
    # Log the message in the terminal
    drop_off_time = datetime.now().strftime("%Y.%m.%d.%H.%M")
    print(f"{time_value}.{desc_value}.{drop_off_time}.close")

# Run the function once
parse_and_notify(main_array)
