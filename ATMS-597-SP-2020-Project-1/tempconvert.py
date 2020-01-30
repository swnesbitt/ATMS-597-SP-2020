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
        if self.regularized == True:
            self.temp = np.clip(self.temp, -459.67, None)
        return self.output()
    
    # Convert Fahrenheit to Celsius
    def F2C(self):
        self.temp = (self.temp - 32.)/1.8
        if self.regularized == True:
            self.temp = np.clip(self.temp, -273.15, None)
        return self.output()
    
    # Convert Celsius to Kelvin
    def C2K(self):
        self.temp = self.temp + 273.15
        if self.regularized == True:
            self.temp = np.clip(self.temp, 0., None)
        return self.output()
    
    # Convert Kelvin to Celsius
    def K2C(self):
        self.temp = self.temp - 273.15
        if self.regularized == True:
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