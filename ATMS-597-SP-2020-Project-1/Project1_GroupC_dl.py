import numpy as np

class TempConvert:
    """A simple class that converts freely among Kelvin, degrees Celsius, and degrees Fahrenheit"""
    def __init__(self, value, unit):
        self.value = np.asarray(value)
        self.unit = unit
        self.type = type(value)

    def toF(self):
        if self.unit == "C":
            self.value = self.value * 9/5 + 32
        elif self.unit == "K":
            self.value = self.value * 9/5 - 459.67
        elif self.unit == "F":
            self.value = self.value * 1

    def toK(self):
        if self.unit == "C":
            self.value = self.value + 273.15
        elif self.unit == "F":
            self.value = (self.value + 459.67) * 5/9
        elif self.unit == "K":
            self.value = self.value * 1

    def toC(self):
        if self.unit == "K":
            self.value = self.value - 273.15
        elif self.unit == "F":
            self.value = (self.value - 32) * 5/9
        elif self.unit == "C":
            self.value = self.value * 1

# # Input values as list
# temps_list = [10, -50.5, 123, -0.1]
# unit_list = "C"

# print("Input values selected as data type: " + str(type(temps_list)))
# print(str(temps_list) + " " + unit_list)

# print("\nConverting now... Results:")
# temps = TempConvert(temps_list, unit_list)
# print(str(temps.toC()) + " " + "C")
# print(str(temps.toF()) + " " + "F")
# print(str(temps.toK()) + " " + "K\n\n")


# # Input values as numpy array
# temps_np = np.array([-18.5, 0.0, 29, 100])
# unit_np = "F"

# print("Input values selected as data type: " + str(type(temps_np)))
# print(str(temps_np) + " " + unit_np)

# print("\nConverting now... Results:")
# temps = TempConvert(temps_list, unit_np)
# print(str(temps.toC()) + " " + "C")
# print(str(temps.toF()) + " " + "F")
# print(str(temps.toK()) + " " + "K")
