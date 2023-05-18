from tkinter import *
from tkinter import ttk

lis = ["first", "second"]
def print_temp():
    print(temperature_degrees.get(), "/", temperature_fahrenheit.get())


def create_output_box():
    output_window = Toplevel(root)
    output_window.title("Output Window")

    f1 = Frame(output_window)
    f1.grid(row=0, column=0)
    label = Label(f1, text="Degrees Logs")
    label.grid(row=0, column=0)

    check = Listbox(f1)
    check.insert(0, *lis)
    check.bindtags(check)
    check.grid(row=1, column=0)
    output_window.resizable(False, False)
    output_window.grab_set()


# the title of the program
root = Tk()
root.title("Temperature Converter")
# the main frame of the programs hold everything from text frame and temperature frame
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0)

# a frame for the program only holds the text UI elements
text_frame = ttk.Frame(main_frame)
text_frame.grid(row=0, column=0)

# a frame for the program only hold the temperature UI elements
temperature_frame = ttk.Frame(main_frame)
temperature_frame.grid(row=1, column=0)

# name of the program
name_label = ttk.Label(text_frame, text="Temperature Converter")
name_label.grid(row=0, column=0)

output_label = ttk.Label(temperature_frame, text="Output")
output_label.grid(row=2, column=0)
output_label_2 = ttk.Label(temperature_frame, text="Output")
output_label_2.grid(row=2, column=2)

# variables that hold values for temperature either in degrees or fahrenheit
temperature_degrees = IntVar()
temperature_fahrenheit = IntVar()
temperature_degrees_output = IntVar()
temperature_fahrenheit_output = IntVar()

# hold the inputted that is going to be used to convert either into degrees or fahrenheit
temperature_degrees_input_entry = ttk.Entry(temperature_frame, textvariable=temperature_degrees)
temperature_degrees_input_entry.grid(row=0, column=0, padx=10, pady=10)
temperature_fahrenheit_entry = ttk.Entry(temperature_frame, textvariable=temperature_fahrenheit)
temperature_fahrenheit_entry.grid(row=0, column=2, padx=10, pady=10)

# outputted the converted value either in degrees or fahrenheit that was taken from the above entry box
temperature_degrees_output_entry = ttk.Entry(temperature_frame, textvariable=temperature_degrees_output,
                                             state="disabled")
temperature_degrees_output_entry.grid(row=3, column=0, padx=5, pady=5)
temperature_fahrenheit_entry = ttk.Entry(temperature_frame, textvariable=temperature_fahrenheit_output,
                                         state="disabled")
temperature_fahrenheit_entry.grid(row=3, column=2, padx=5, pady=5)

# buttons that when press will convert the inputted temperature to either degrees or fahrenheit
temperature_converter_degrees_button = ttk.Button(temperature_frame, text="Convert to degrees")
temperature_converter_degrees_button.grid(row=1, column=0, sticky="WE", padx=10, pady=5)
temperature_converter_fahrenheit_button = ttk.Button(temperature_frame, text="Convert to fahrenheit")
temperature_converter_fahrenheit_button.grid(row=1, column=2, sticky="WE", padx=10, pady=5)

save_degrees_log_button = ttk.Button(temperature_frame, text="Save degree log")
save_degrees_log_button.grid(row=4, column=0, sticky="NSEW", padx=10, pady=5)
save_fahrenheit_log_button = ttk.Button(temperature_frame, text="Save fahrenheit log")
save_fahrenheit_log_button.grid(row=4, column=2, sticky="NSEW", padx=10, pady=5)

output_logs_button = ttk.Button(temperature_frame, text="Output logs", command=create_output_box)
output_logs_button.grid(row=4, column=1, sticky="NSEW", padx=10, pady=5)

help_button = ttk.Button(temperature_frame, text="Help!")
help_button.grid(row=3, column=1, sticky="NSEW", padx=10, pady=5)
# run the mainloop
root.resizable(False, False)
root.mainloop()
