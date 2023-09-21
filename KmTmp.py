import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk 
import datetime
from datetime import date
import json
import os

def convert():
    global pace 
    # get data
    dist_input = entry_dist.get()
    dist_time = entry_time.get()

    # calculate time to seconds
    input_time = datetime.datetime.strptime(dist_time, "%M:%S")
    seconds = (input_time.minute * 60) + input_time.second

    try:
        time = (float(seconds) / dist_input)
        pace = str(datetime.timedelta(seconds = round(time)))
        output_string.set(pace + " per Kilometre")
        return pace
    except:
        output_string.set("Please input the distance \nand time of your run")

def check_json():
    checkData = os.path.exists("data.json")

    if(checkData != True):
        file = 'data.json'
        f = open(file, 'a+')  # open file in append mode
        f.close()
        print("File created")
    else:
        print("File already exists")

def write_json():
    today = str(date.today())
    #print(today)   # '2017-12-26'

    try:
        info = {"date": today,
                "distance":  entry_dist.get(),
                "time": entry_time.get(),
                "pace": pace}
        
        filename = "data.json"
        with open(filename,'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["Run_Information"].append(info)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

    except:
        output_string.set("Please convert your time \nfirst before saving the data")

# window
window = ttk.Window(themename = "darkly")
window.title("Kilometers Morales (Temporales)")
window.geometry("400x200")

# Set icon for window
window.tk.call("wm", "iconphoto", window._w, tk.PhotoImage(file="Assets/lauf.png"))

# title
title_label = ttk.Label(master = window, text = "Pace Calculator", font = "Fira 24")
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_dist = tk.DoubleVar()
entry_time = tk.StringVar(value = "00:00")
entry1 = ttk.Entry(master = input_frame,
                  textvariable  = entry_dist)

button_calc = ttk.Button(master = input_frame, text = "Convert", command = convert)

button_sav = ttk.Button(master = window, text = "Save Data", command = write_json)

entry2 = ttk.Entry(master = input_frame,
                   textvariable = entry_time)

entry1.pack(side = "left", padx = 10)
entry2.pack(side = "left", padx = 10)
button_calc.pack(side = "right", padx = 10)
button_sav.pack()
input_frame.pack(pady = 10)

# output 
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window,
    text = "Output",
    font = "Fira 24",
    textvariable = output_string)
output_label.pack(pady= 5)

# check for data
check_json()

# run 
window.mainloop()