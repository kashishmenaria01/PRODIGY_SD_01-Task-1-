Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> temp = float(input("Enter temperature value: "))
... unit = input("Enter unit (C/F/K): ").upper()
... 
... if unit == "C":
...     f = (temp * 9/5) + 32
...     k = temp + 273.15
...     print("Fahrenheit =", round(f, 2), "F")
...     print("Kelvin =", round(k, 2), "K")
... 
... elif unit == "F":
...     c = (temp - 32) * 5/9
...     k = c + 273.15
...     print("Celsius =", round(c, 2), "C")
...     print("Kelvin =", round(k, 2), "K")
... 
... elif unit == "K":
...     c = temp - 273.15
...     f = (c * 9/5) + 32
...     print("Celsius =", round(c, 2), "C")
...     print("Fahrenheit =", round(f, 2), "F")
... 
... else:
