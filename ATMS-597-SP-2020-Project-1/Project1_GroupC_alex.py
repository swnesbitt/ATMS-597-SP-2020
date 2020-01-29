import numpy as np

class tempConvert:
    """
    
        A class to convert temperatures between Celsius, Fahrenheit, and Kelvin
        
        Takes lists or numpy arrays as input. Outputs as the same type.
    
    
    """
    
    def __init__(self,temp):
        self.temp = temp
        self.dtype = type(self.temp)
        
    
    def FtoC(self):
        """Converting Fahrenheit to Celsius"""
                
        temp = self.temp
        
        templist = []
        
        for i in temp:
            templist.append(round(((i - 32.) * (5./9.)), 2))
        
        if self.dtype == list:
            self.temp = templist
        
        else:  
            self.temp = np.asarray(templist)
    
    def CtoF(self):
        """"Converting Celsius to Fahrenheit"""
        
        temp = self.temp
        
        templist = []
        
        for i in temp:
            templist.append(round((i * (9./5.) + 32.), 2))
            
        if self.dtype == list:
            self.temp = templist
        
        else:  
            self.temp = np.asarray(templist)
    
    def CtoK(self):
        """Converting Celsius to Kelvin"""
        
        temp = self.temp
        
        templist = []
        
        for i in temp:
            templist.append(round((i + 273.15), 2))
            
        if self.dtype == list:
            self.temp = templist
        
        else:  
            self.temp = np.asarray(templist)
    
    def KtoC(self):
        """Converting Kelvin to Celsius"""
        
        temp = self.temp
        
        templist = []
        
        for i in temp:
            templist.append(round((i - 273.15), 2))
            
        if self.dtype == list:
            self.temp = templist
        
        else:  
            self.temp = np.asarray(templist)
    
    def FtoK(self):
        """Converting Fahrenheit to Kelvin"""
        
        temp = self.temp
        
        templist = []
        
        for i in temp:
            templist.append(round(((i - 32.) * (5./9.) + 273.15), 2))
            
        if self.dtype == list:
            self.temp = templist
        
        else:  
            self.temp = np.asarray(templist)
    
    def KtoF(self):
        """Converting Kelvin to Fahrenheit"""
        
        temp = self.temp
        
        templist = []
        
        for i in temp:
            templist.append(round(((i - 273.15) * (9./5.) + 32.), 2))
            
        if self.dtype == list:
            self.temp = templist
        
        else:  
            self.temp = np.asarray(templist)
    

#testing
temp1 = [30, 35, 50, 70]
temp2 = np.array([200, 300, 400, 500])

test1 = tempConvert(temp1)
test2 = tempConvert(temp2)

test1.temp
test2.temp

test1.dtype
test2.dtype

test1.CtoF()
print(test1.temp)

test2.KtoF()
print(test2.temp)
