import tkinter as tk
from tkinter import ttk

# Temperature Conversion Functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Function to perform temperature conversion
def convert_temperature():
    try:
        temp = float(entry_temperature.get())
        input_unit = combo_input_unit.get()
        output_unit = combo_output_unit.get()

        if input_unit == "Celsius":
            if output_unit == "Fahrenheit":
                result = celsius_to_fahrenheit(temp)
            elif output_unit == "Kelvin":
                result = celsius_to_kelvin(temp)
            else:
                result = temp  # No conversion needed
        elif input_unit == "Fahrenheit":
            if output_unit == "Celsius":
                result = fahrenheit_to_celsius(temp)
            elif output_unit == "Kelvin":
                result = fahrenheit_to_kelvin(temp)
            else:
                result = temp
        elif input_unit == "Kelvin":
            if output_unit == "Celsius":
                result = kelvin_to_celsius(temp)
            elif output_unit == "Fahrenheit":
                result = kelvin_to_fahrenheit(temp)
            else:
                result = temp
        else:
            result = "Invalid unit"

        label_result.config(text=f"Converted Temperature: {result:.2f} {output_unit}")
    except ValueError:
        label_result.config(text="Please enter a valid temperature.")

# Create the main window
root = tk.Tk()
root.title("Temperature Conversion")
root.geometry("400x300")

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))
style.configure("TCombobox", font=("Arial", 12))

# Header Frame
header_frame = ttk.Frame(root)
header_frame.pack(pady=10)

label_title = ttk.Label(header_frame, text="Temperature Conversion", font=("Arial", 16, "bold"))
label_title.pack()

# Input Frame
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

# Temperature Label and Entry
label_temperature = ttk.Label(input_frame, text="Temperature:", font=("Arial", 12))
label_temperature.grid(row=0, column=0, padx=5, pady=5, sticky="w")  # Align left

entry_temperature = ttk.Entry(input_frame, width=10)
entry_temperature.grid(row=0, column=1, padx=5, pady=5)

# Input Unit Label and Dropdown
label_input_unit = ttk.Label(input_frame, text="Input Unit:", font=("Arial", 12))
label_input_unit.grid(row=1, column=0, padx=5, pady=5, sticky="w")  # Align left

combo_input_unit = ttk.Combobox(input_frame, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", width=10)
combo_input_unit.set("Celsius")
combo_input_unit.grid(row=1, column=1, padx=5, pady=5)

# Output Unit Label and Dropdown
label_output_unit = ttk.Label(input_frame, text="Output Unit:", font=("Arial", 12))
label_output_unit.grid(row=2, column=0, padx=5, pady=5, sticky="w")  # Align left

combo_output_unit = ttk.Combobox(input_frame, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", width=10)
combo_output_unit.set("Fahrenheit")
combo_output_unit.grid(row=2, column=1, padx=5, pady=5)

# Convert Button
button_convert = ttk.Button(input_frame, text="Convert", command=convert_temperature)
button_convert.grid(row=3, columnspan=2, pady=10)

# Result Label
label_result = ttk.Label(root, text="Converted Temperature:", font=("Arial", 14, "bold"), foreground="blue")
label_result.pack(pady=10)

# Run the application
root.mainloop()
