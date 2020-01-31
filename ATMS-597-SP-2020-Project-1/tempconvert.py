# ATMS 597 Project 1 Group D
# Author: Yang LU

# Import library
import numpy as np


class tempconvert():
    '''
    A python module that converts temperatures interchangeably between degrees
    Celsius, Fahrenheit, and Kelvin.
    '''

    def __init__(self, temp, regularized=True):
        # Record the type and data type of temperatures
        self.type = type(temp)
        self.dtype = type(temp[0])
        self.temp = np.array(temp)
        # With the constraint of absolute zero as default
        self.regularized = regularized

    # Convert Celsius to Fahrenheit
    def C2F(self):
        self.temp = self.temp*1.8 + 32.
        if self.regularized:
            self.temp = np.clip(self.temp, -459.67, None)
        return self.output()

    # Convert Fahrenheit to Celsius
    def F2C(self):
        self.temp = (self.temp - 32.)/1.8
        if self.regularized:
            self.temp = np.clip(self.temp, -273.15, None)
        return self.output()

    # Convert Celsius to Kelvin
    def C2K(self):
        self.temp = self.temp + 273.15
        if self.regularized:
            self.temp = np.clip(self.temp, 0., None)
        return self.output()

    # Convert Kelvin to Celsius
    def K2C(self):
        self.temp = self.temp - 273.15
        if self.regularized:
            self.temp = np.clip(self.temp, -273.15, None)
        return self.output()

    # Convert Fahrenheit to Kelvin
    def F2K(self):
        self.F2C()
        self.C2K()
        return self.output()

    # Convert Kelvin to Fahrenheit
    def K2F(self):
        self.K2C()
        self.C2F()
        return self.output()

    # Output the origional data type
    def output(self):
        self.temp = np.array(self.temp, dtype=self.dtype)
        if self.type == list:
            return self.temp.tolist()
        else:
            return self.temp

# Tests
input_0 = [2, 30, 400, 5000]
input_1 = np.array([-280., 0., 1000], dtype=np.float32)
input_2 = np.array([-1., 200, 30000])

output_0 = tempconvert(input_0).F2K()
output_1 = tempconvert(input_1).C2F()
output_2 = tempconvert(input_2).K2F()

print("Input F", input_0, ", output K", output_0)
print("Input C", input_1, ", output F", output_1)
print("Input K", input_2, ", output F", output_2)
assert type(input_0) == type(output_0), "wrong type"
assert type(input_1) == type(output_1), "wrong type"
assert type(input_2) == type(output_2), "wrong type"
assert isinstance(output_0[0], type(input_0[0])), "wrong type"
assert isinstance(output_1[0], type(input_1[0])), "wrong type"
assert isinstance(output_2[0], type(input_2[0])), "wrong type"
