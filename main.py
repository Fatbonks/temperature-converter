from tkinter import *
from tkinter import ttk, filedialog
import os
from tkinter import filedialog as fd


def save_log(temp_type):
    if temp_type == "degrees":
        try:
            degrees = float(temperature_degrees.get())
            if temp_type == "degrees":
                var = (degrees - 32) * 5 / 9
                temperature_degrees_output.set(str(var))
                new_input = float(temperature_degrees_input_entry.get())
                new_output = float(temperature_degrees_output.get())
                output_temp_in_list = "{:1f}°F to {:1f}°C".format(new_input, new_output)
                try:
                    if lis[1] != output_temp_in_list:
                        lis.insert(1, output_temp_in_list)
                except IndexError:
                    lis.insert(1, output_temp_in_list)
        except ValueError:
            temperature_degrees_output.set("please input a number")

    if temp_type == "fahrenheit":
        try:
            fahrenheit = float(temperature_fahrenheit.get())
            var = (fahrenheit * 9 / 5) + 32
            temperature_fahrenheit_output.set(str(var))

        except ValueError:
            pass


def temp_convert(temp_type):
    if temp_type == "degrees":
        try:
            degrees = float(temperature_degrees.get())
            if temp_type == "degrees":
                var = (degrees - 32) * 5 / 9
                temperature_degrees_output.set(str(var))
        except ValueError:
            temperature_degrees_output.set("please input a number")

    if temp_type == "fahrenheit":
        try:
            fahrenheit = float(temperature_fahrenheit.get())
            var = (fahrenheit * 9 / 5) + 32
            temperature_fahrenheit_output.set(str(var))

        except ValueError:
            temperature_fahrenheit_output.set("please input a number")


def clear_logs():
    fahrenheit_list.delete(0, END)
    degrees_list.delete(0, END)


def create_output_box():
    global fahrenheit_list
    global degrees_list
    output_window = Toplevel(root)
    output_window.title("Output Window")
    f1 = Frame(output_window)
    f1.grid(row=0, column=0)
    degrees_label = Label(f1, text="Degrees Logs")
    degrees_label.grid(row=0, column=0)

    fahrenheit_label = Label(f1, text="Fahrenheit Logs")
    fahrenheit_label.grid(row=0, column=3)

    degrees_list = Listbox(f1)
    degrees_list.grid(row=1, column=0, sticky="NSEW", padx=10, pady=5)
    degrees_list.insert(0, *lis)
    fahrenheit_list = Listbox(f1)
    fahrenheit_list.grid(row=1, column=3, sticky="NSEW", padx=10, pady=5)

    degrees_output_log = ttk.Button(f1, text="Output logs", command=create_file_location_box)
    degrees_output_log.grid(row=2, column=1, sticky="NSEW", padx=10, pady=5)

    degrees_output_log = ttk.Button(f1, text="Clear", command=clear_logs)
    degrees_output_log.grid(row=1, column=1, sticky="SEW", padx=10, pady=5)

    output_window.resizable(False, False)
    output_window.grab_set()


def create_file_location_box():
    output_window = Toplevel(root)
    output_window.title("File Location")

    f1 = Frame(output_window)
    f1.grid(row=0, column=0)

    file_location = os.path.dirname(os.path.realpath(__file__))
    file_label = ttk.Label(f1,
                           text="Your outputted logs are saved here!, \n" + file_location + "\n, press the X button "
                                                                                            "on the top right to "
                                                                                            "leave window")
    file_label.grid(row=0, column=0)
    output_window.grab_set()


# the title of the program
root = Tk()
root.title("Temperature Converter")
# the main frame of the programs hold everything from text frame and temperature frame
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0)

lis = ["Outputs:"]
fahrenheit_list = Listbox()
degrees_list = Listbox()

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
temperature_degrees = StringVar()
temperature_degrees.set("0°F")
temperature_fahrenheit = StringVar()
temperature_fahrenheit.set("0°C")
temperature_degrees_output = StringVar()
temperature_fahrenheit_output = StringVar()

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
temperature_converter_degrees_button = ttk.Button(temperature_frame, text="Convert to degrees",
                                                  command=lambda: temp_convert("degrees"))
temperature_converter_degrees_button.grid(row=1, column=0, sticky="WE", padx=10, pady=5)
temperature_converter_fahrenheit_button = ttk.Button(temperature_frame, text="Convert to fahrenheit",
                                                     command=lambda: temp_convert("fahrenheit"))
temperature_converter_fahrenheit_button.grid(row=1, column=2, sticky="WE", padx=10, pady=5)

save_degrees_log_button = ttk.Button(temperature_frame, text="Save degree log", command=lambda: save_log("degrees"))
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
