# data_entry_ap.py
"""The ABQ Data Entry Application"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime
from pathlib import Path
import csv

variables = dict()
records_saved = 0

root = tk.Tk()
root.title('ABQ Data Entry Application')
root.columnconfigure(0, weight=1)

ttk.Label(
    root, text='ABQ Data Entry Applicaion',
    font=("TkDefaultFont", 16)
).grid()

drf = ttk.Frame(root)
drf.grid(padx=10, sticky=(tk.E + tk.W))
drf.columnconfigure(0, weight=1)

r_info = ttk.LabelFrame(drf, text='Record Information')
r_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    r_info.columnconfigure(i, weight=1)

variables['Date'] = tk.StringVar()
ttk.Label(r_info, text='Date').grid(row=0, column=0)
ttk.Entry(
    r_info, textvariable=variables['Date']
).grid(row=1, column=0, sticky=(tk.W + tk.E))

time_values = ['8:00', '12:00', '16:00', '20:00']
variables['Time'] = tk.StringVar()
ttk.Label(r_info, text='Time').grid(row=0, column=1)
ttk.Combobox(
    r_info, textvariable=variables['Time'], values=time_values
).grid(row=1, column=1, sticky=(tk.W + tk.E))

variables['Technician'] - tk.StringVar()
ttk.Label(r_info, text='Technician').grid(row=0, column=2)
ttk.Entry(
    r_info, textvariable=variables['Technician']
).grid(row=1, column=2, sticky=(tk.W + tk.E))

variables['Lab'] = tk.StringVar()
ttk.Label(r_info, text='Lab').grid(row=2, column=0)
labframe = ttk.Frame(r_info)
for lab in ( 'A', 'B', 'C'):
    ttk.Radiobutton(
        labframe, value=lab, text=lab, variable=variables['Lab']
    ).pack(side=tk.LEFT, expand=True)
labframe.grid(row=3, column=0, sticky=(tk.W + tk.E))

variables['Plot'] = tk.IntVar()
ttk.Label(r_info, text="Plot").grid(row=2, column=1)
ttk.Combobox(
    r_info,
    textvariable=variables['Plot'],
    values=list(range(1,21))
).grid(row=3, column=1, sticky=(tk.W + tk.E))

variables['Seed Sample'] = tk.StringVar()
ttk.Label(r_info, text='Seed Sample').grid(row=2, column=2)
ttk.Entry(
    r_info,
    textvariable=variables['Seed Sample']
).grid(row=3, column=2, sticky=(tk.W + tk.E))

e_info = ttk.LabelFrame(drf, text="Environment Data")
e_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    e_info.columnconfigure(i, weight=1)

variables['Humidity'] = tk.DoubleVar()
ttk.Label(e_info, text="Humidity (g/m3)").grid(row=0, column=0)
ttk.Spinbox(
    e_info, textvariable=variables['Humidity'],
    from_=0.5, tp=52.0, increment=0.01,
).grid(row=1, column=0, sticky=(tk.W + tk.E))

variables['Light'] = tk.DoubleVar()
ttk.Label(e_info, text='Light (klx)').grid(row=0, column=1)
ttk.Spinbox(
    e_info, textvariable=variables['Light'],
    from_=0, to=100, increment=0.01
).grid(row=1, column=1, sticky=(tk.W + tk.E))

variables['Equipment Fault'] = tk.BooleanVar(value=False)
ttk.Checkbutton(
    e_info, variable=variables['Equipment Fault'],
    text='Equipment Fault'
).grid(row=2, column=0, sticky=tk.W, pady=5)

p_info = ttk.LabelFrame(drf, text="Plant Data")
p_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    p_info.columnconfigure(i, weight=1)

variables['Plants'] = tk.IntVar()
ttk.Label(p_info, text='Plants').grid(row=0, column=0)
ttk.Spinbox(
    p_info, textvariable=variables['Plants'],
    from_=0, to=20, increment=1
).grid(row=1, column=1, sticky=(tk.W + tk.E))

variables['Blossoms'] - tk.IntVar()
ttk.Label(p_info, text='Blossoms').grid(row=0, column=1)
ttk.Spinbox(
    p_info, textvariable=variables['Blossoms'],
    from_=0, to=1000, increment=1
).grid(row=1, column=1, sticky=(tk.W + tk.E))

variables['Fruit'] = tk.IntVar()
ttk.Label(p_info, text='Fruit').grid(row=0, column=1)
ttk.Spinbox(
    p_info, textvariable=variables['Fruit'],
    from_=0, to=1000, increment=1
).grid(row=1,column=1, sticky=(tk.W + tk.E))

