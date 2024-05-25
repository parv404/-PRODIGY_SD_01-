def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature(value, unit):
    if unit == "C":
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        return fahrenheit, kelvin
    elif unit == "F":
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        return celsius, kelvin
    elif unit == "K":
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        return celsius, fahrenheit
    else:
        raise ValueError("Unknown temperature unit")

def main():
    print("Temperature Conversion Program")
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
        if unit not in ['C', 'F', 'K']:
            raise ValueError("Invalid unit")
        
        if unit == "C":
            fahrenheit, kelvin = convert_temperature(value, unit)
            print(f"{value} degrees Celsius is equivalent to {fahrenheit:.2f} degrees Fahrenheit and {kelvin:.2f} Kelvin.")
        elif unit == "F":
            celsius, kelvin = convert_temperature(value, unit)
            print(f"{value} degrees Fahrenheit is equivalent to {celsius:.2f} degrees Celsius and {kelvin:.2f} Kelvin.")
        elif unit == "K":
            celsius, fahrenheit = convert_temperature(value, unit)
            print(f"{value} Kelvin is equivalent to {celsius:.2f} degrees Celsius and {fahrenheit:.2f} degrees Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
