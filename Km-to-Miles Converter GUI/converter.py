import tkinter as tk
from tkinter import ttk


'''Desktop program that converts kilometers to miles'''


def convert():
    try:
        kms = float(kms_entry.get())
        miles = kms * 0.621371192
        result_label.config(text=f'Distance in miles: {miles:.2f}')
    except ValueError:
        result_label.config(text='Please enter a valid number.')


window = tk.Tk()
window.title('Km to Miles Converter')

frame = ttk.Frame(window, padding='10')
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

kms_label = ttk.Label(frame, text='Enter distance in kilometers:')
kms_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=2)

kms_entry = ttk.Entry(frame, width=15)
kms_entry.grid(row=0, column=1, sticky=tk.W, pady=2)
kms_entry.focus()

convert_button = ttk.Button(frame, text='Convert', command=convert)
convert_button.grid(row=1, column=0, columnspan=2, pady=2)

result_label = ttk.Label(frame, text='Distance in miles: ')
result_label.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=2)

window.mainloop()
