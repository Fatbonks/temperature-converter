from tkinter import *
from tkinter import ttk


def print_temp():
    print(temperature_degrees.get(), "/", temperature_fahrenheit.get())


root = Tk()
root.title("Temperature Converter")

main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0)

text_frame = ttk.Frame(main_frame)
text_frame.grid(row=0, column=0)

temperature_frame = ttk.Frame(main_frame)
temperature_frame.grid(row=1, column=0)

name_label = ttk.Label(text_frame, text="Temperature Converter")
name_label.grid(row=0, column=0)

temperature_degrees = IntVar()
temperature_fahrenheit = IntVar()
temperature_degrees_output = IntVar()
temperature_fahrenheit_output = IntVar()

temperature_degrees_input_entry = ttk.Entry(temperature_frame, textvariable=temperature_degrees)
temperature_degrees_input_entry.grid(row=0, column=0, padx=10, pady=10)
temperature_fahrenheit_input_entry = ttk.Entry(temperature_frame, textvariable=temperature_fahrenheit)
temperature_fahrenheit_input_entry.grid(row=0, column=1, padx=10, pady=10)

temperature_converter_degrees_button = ttk.Button(temperature_frame, text="Convert to degrees", command=print_temp)
temperature_converter_degrees_button.grid(row=1, column=0, sticky="WE", padx=10, pady=5)
temperature_converter_degrees_button = ttk.Button(temperature_frame, text="Convert to fahrenheit", command=print_temp)
temperature_converter_degrees_button.grid(row=1, column=1, sticky="WE", padx=10, pady=5)

# run the mainloop
root.mainloop()
