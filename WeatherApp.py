from customtkinter import *
import customtkinter
import time
import requests 
import tkinter as tk
import json
from tkinter import messagebox,PhotoImage
from requests.exceptions import ConnectionError

def center_window(root, width, height):
    # Calculate screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate window position to center it on the screen
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window position
    root.geometry(f"{width}x{height}+{x}+{y}")


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Weather App")

window_width = 800
window_height = 600

# Create the window with initial dimensions
root.geometry(f"{window_width}x{window_height}")
# Center the window on the screen
center_window(root, window_width, window_height)
background_image = PhotoImage(file="bg.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def check_weather():
    city_name = city_entry.get()   
    url = f"https://api.weatherapi.com/v1/current.json?key=2a759d8a1458497d8bc190846231407&q={city_name}"

    for _ in range(3):  # Try 3 times
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
            break  # Exit the loop if the request is successful
        except ConnectionError as e:
            print(f"Connection error: {e}")
            time.sleep(2)  # Wait for 2 seconds before retrying

    data = json.loads(response.text)
    temp=data['current']['temp_c']
     # Update the label to display the temperature
    temp_label.configure(text=f"Temperature: {temp}°C")

def clear_temp():
    temp_label.configure(text="")
    city_entry.delete(0, 'end') 


frame =customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx =60,fill="both",expand=True)


heading = CTkLabel(frame,text="Weather App", font=("Microsoft yehei UI Light",55,"bold"))
heading.pack(pady=15, padx=25)

city_entry = customtkinter.CTkEntry(master=frame,placeholder_text="Enter City Name",width=200)
city_entry.pack(pady =15,padx=10)


check_button = customtkinter.CTkButton(master=frame,text="Check Weather",command=check_weather)
check_button.pack(pady =12,padx=10)

clear_button = customtkinter.CTkButton(master=frame,text="Clear",command=clear_temp)
clear_button.pack(pady =12,padx=15)

checkbox = customtkinter.CTkCheckBox(master=frame,text="Remember me")
checkbox.pack(pady =12,padx=10)

temp_label = customtkinter.CTkLabel(master=frame,text="",fg_color="black")
temp_label.pack(pady =18,padx=10)

root.mainloop()