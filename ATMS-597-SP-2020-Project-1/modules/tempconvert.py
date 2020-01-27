"""Temperature convertor between Celcius, Fahrenheit and Kelvin"""
# This code is part of a class assignment for ATMS 597, Spring 2020,
# at the University of Illinois at Urbana Champaign.
# Use this class function to convert temperature data from already
# known units to different units.
# It supports conversion to Celcius, Fahrenheit and Kelvin.
import numpy as np

class tempconvert:
    """Temperature convertor for numpy arrays and lists"""

    # mem attribute will keep memory of the input data type
    # Initialized as 0, it will become 1 if list is input
    mem = 0

    def __init__(self,in_temp):
        """Create a temperature object.
        The input is assigned to the object as class instance. Method calls 
        are used to convert to desired units and retrieve output.

        **Arguments:** 

        *in_temp*
            Input temperature. This can be numpy ndarray, or a list. Missing
            values are not permitted. The units of temperature must be known,
            and appropriate method be used to convert to desired units.
          
        **Returns:**

        *temp*
            A temperature convertor instance

        **Example:**
        
        If in_temp is a numpy ndarray or a list:
            from tempconvert import tempconvert
            temperature = tempconvert(in_temp)

        """
        # check if the input is a list or numpy array
        if isinstance(in_temp, list):
            # store as a numpy array in an instance variable
            self.__temp = np.asarray(in_temp)
            # change mem to 1
            self.mem = 1
        elif isinstance(in_temp, np.ndarray):
            # store numpy array in an instance variable
            self.__temp = in_temp
        else:
            raise Exception('Input not recognized')
        
    def C2F(self):
        """Convert temperature from Celcius to Fahrenheit.

        **Returns:**

        *temp*
            A temperature convertor instance, in degrees Fahrenheit.
        
        **Example:**
        
        If in_temp is in degrees Celcius:
            from tempconvert import tempconvert
            output = tempconvert(in_temp).C2F()

        """
        # modify the .__temp attribute of object directly 
        self.__temp = (self.__temp*9/5) + 32
        # return the same numerical type as the input
        if self.mem > 0:
            return self.__temp.tolist()
        else:
            return self.__temp

    def F2C(self):
        """Convert temperature from Fahrenheit to Celcius.

        **Returns:**

        *temp*
            A temperature convertor instance, in degrees Celcius.

        **Example:**
        
        If in_temp is in degrees Fahrenheit:
            from tempconvert import tempconvert
            output = tempconvert(in_temp).F2C()

        """
        # modify the .__temp attribute of object directly
        self.__temp = (self.__temp-32) * (5/9)
        # return the same numerical type as the input
        if self.mem > 0:
            return self.__temp.tolist()
        else:
            return self.__temp

    def C2K(self):
        """Convert temperature from Celcius to Kelvin.

        **Returns:**

        *temp*
            A temperature convertor instance, in degrees Kelvin.
        
        **Example:**
        
        If in_temp is in degrees Celcius:
            from tempconvert import tempconvert
            output = tempconvert(in_temp).C2K()

        """
        # modify the .__temp attribute of object directly
        self.__temp = self.__temp + 273.15
        # return the same numerical type as the input
        if self.mem > 0:
            return self.__temp.tolist()
        else:
            return self.__temp

    def K2C(self):
        """Convert temperature from Kelvin to Celcius.

        **Returns:**

        *temp*
            A temperature convertor instance, in degrees Celcius.
        
        **Example:**
        
        If in_temp is in degrees Kelvin:
            from tempconvert import tempconvert
            output = tempconvert(in_temp).K2C()

        """
        # modify the .__temp attribute of object directly
        self.__temp = self.__temp - 273.15
        # return the same numerical type as the input
        if self.mem > 0:
            return self.__temp.tolist()
        else:
            return self.__temp

    def F2K(self):
        """Convert temperature from Fahrenheit to Kelvin.

        **Returns:**

        *temp*
            A temperature convertor instance, in degrees Kelvin.
        
        **Example:**
        
        If in_temp is in degrees Fahrenheit:
            from tempconvert import tempconvert
            output = tempconvert(in_temp).F2K()

        """
        # modify the .__temp attribute of object directly
        self.__temp = (self.__temp-32) * (5/9) + 273.15
        # return the same numerical type as the input
        if self.mem > 0:
            return self.__temp.tolist()
        else:
            return self.__temp

    def K2F(self):
        """Convert temperature from Kelvin to Fahrenheit.

        **Returns:**

        *temp*
            A temperature convertor instance, in degrees Fahrenheit.
        
        **Example:**
        
        If in_temp is in degrees Kelvin:
            from tempconvert import tempconvert
            output = tempconvert(in_temp).K2F()

        """
        # modify the .__temp attribute of object directly
        self.__temp = (self.__temp - 273.15) * (9/5) + 32
        # return the same numerical type as the input
        if self.mem > 0:
            return self.__temp.tolist()
        else:
            return self.__temp
