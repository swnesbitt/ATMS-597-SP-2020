# -*- coding: utf-8 -*-
"""Project1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/JRLoveridge/ATMS-597-SP-2020/blob/master/ATMS-597-SP-2020-Project-1/Project1.ipynb

# **ATMS 597 SN Weather and Climate Data Sciencet**

<h1>Module 1: Project</h1>

<h2>Part A: Convert temperatures interchangeably between degree Celsius, Farenheit and Kelvin </h2>
<h3>Group H: Jesse Loveridge, Lina Rivelli-Zea, Xinchang Li</h3>
"""

# Mount your Google Drive folder

from google.colab import drive

drive.mount('/content/drive')

import numpy as np

class TemperatureConverter(object):
    """
    Method to convert temperature interchangeably between 
    Farenheit, Celsius, and Kelvin. 

    Works with lists or numpy arrays as inputs, and returns 
    the same numerical type.
    
    J.Loveridge/L.RZ/X.Li 01.29.20
    """

    def __init__(self, temperature, units='Kelvin'):
        """Stores a temperature and its type.
      
        Arguments:
        temperature: #type float, list, int, np.ndarray
        units: in Farenheit, Celsius or Kelvin #type: str
        """
        assert units in ['Fahrenheit', 'Celsius', 'Kelvin'], 'Units must be valid.'
        self._temperature = np.atleast_1d(temperature) #internally store numpy array.
        self._units = units
        if type(temperature) == int:         #convert int to float
            temperature = float(temperature)
        self._input_type = type(temperature) #preserve old input type/dtype

    def set_temperature(self, temperature, units='Kelvin'):
        """Overwrites the stored temperature and its type.
        
        Arguments:
        temperature:  #type float, list, int, np.ndarray
        units: in Farenheit, Celsius or Kelvin #type: str
        """
        
        assert units in ['Fahrenheit', 'Celsius', 'Kelvin'], 'Units must be valid.'
        self._temperature = np.atleast_1d(temperature)
        self._units = units
        if type(temperature) == int:
            temperature = float(temperature)
        self._input_type = type(temperature) #preserve old input type/dtype

    def get_temperature(self, units='Kelvin'):
        """Converts the _temperature attribute to new units.
        
        Arguments:
        units: in Farenheit, Celsius or Kelvin  #type: str
        
        Outputs:
        final_temp: in Farenheit, Celsius or Kelvin  #type: float, list, np.ndarray
        """
        assert units in ['Fahrenheit', 'Celsius', 'Kelvin'], 'Units must be valid.'     

        if units == 'Fahrenheit':

            converted_temp =  self.to_fahrenheit()
        elif units == 'Celsius':
            converted_temp =  self.to_celsius()
        elif units == 'Kelvin':
            converted_temp =  self.to_kelvin()

        if self._input_type != type(converted_temp):
            final_temp = self._input_type(converted_temp)
        else:
            final_temp = converted_temp
            
        return final_temp

    def to_kelvin(self):
        """Internal function to convert a temperature of any units to Kelvin.
        
        Outputs:
        returned_temperature= in  Kelvin #type: float, int, or list
        """

        if self._units == 'Fahrenheit':
            returned_temperature = (self._temperature + 459.67)*(5/9)
        elif self._units == 'Celsius':
            returned_temperature = self._temperature + 273.15
        else:
            returned_temperature = self._temperature


        return returned_temperature
  
    def to_celsius(self):
        """Internal function to convert a temperature of any units to Celsius.
        
        Outputs:
        returned_temperature= in  Celsius #type: float, int, or list
        """

        if self._units == 'Fahrenheit':
            returned_temperature = (self._temperature - 32) * (5/9)
        elif self._units == 'Kelvin':
            returned_temperature = self._temperature - 273.15

        else:
            returned_temperature = self._temperature

        return returned_temperature

    def to_fahrenheit(self):
        """Internal function to convert a temperature of any units to Farenheit.
        
        Outputs:
        returned_temperature= in  Farenheit #type: float, int, or list
        """

        if self._units == 'Celsius':
            returned_temperature = self._temperature*(9/5) + 32
        elif self._units == 'Kelvin':
            returned_temperature = self._temperature*(9/5) - 459.67
        else:    
            returned_temperature = self._temperature

        return returned_temperature
    
# define a 'TemperatureConverter' object with temperature data and its units
temp_conv = TemperatureConverter([50,60.0,12830.0],units='Kelvin')

# get temperature in new units using the 'get_temperature' method.
new_temp = temp_conv.get_temperature(units='Kelvin')

print(new_temp)

