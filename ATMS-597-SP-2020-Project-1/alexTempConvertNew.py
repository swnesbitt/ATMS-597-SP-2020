#!/usr/bin/env python
# coding: utf-8

# In[44]:


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
    


# In[73]:


#testing
temp1 = [30,35,50,70]
temp2 = np.array([200,300,400,500])


# In[74]:


test1 = tempConvert(temp1)
test2 = tempConvert(temp2)


# In[75]:


test1.temp


# In[76]:


test2.temp


# In[77]:


test1.dtype


# In[78]:


test2.dtype


# In[79]:


test1.CtoF()


# In[80]:


print(test1.temp)


# In[81]:


test2.KtoF()


# In[82]:


print(test2.temp)


# In[ ]:




