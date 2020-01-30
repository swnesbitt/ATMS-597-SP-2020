import numpy as np

class MrT:

  """
  Authors: Randy J. Chase, David Laferty and Alex Adams 
  
  MrT is a temperature conversion module. It can convert to any of the 4 major
  temperature units (F,C,K and R). 
  Supported datatypes: 
    1) float 
    2) int 
    3) list of floats/ints
    4) np.array of floats/ints 
  """

  def __init__(self,data=[],unit='Unknown. Please enter unit'): 
    self.unit = unit
    self.data = data
    self.datatype = type(self.data)

  def toC(self):
    """ Convert self.data to Celcius """
    #if data are a list, convert to an array. if not, leave it alone
    if self.datatype == list:
      self.data = np.asarray(self.data,dtype=float)
    elif self.datatype == str: 
      print('ERROR: data type is a string. This is not supported')

    if self.unit == 'F':
      self.data = (self.data - 32) * (5/9.)
    elif self.unit == 'K':
      self.data = self.data - 273.15
    elif self.unit =='R':
      self.data = (self.data - 32 - 459.67) / (1.8)
    elif self.unit == 'C':
      print('WARNING: unit was already C, nothing was done')
    else:
      print('ERROR, check spelling of unit')

    #set new unit and make sure you return the orginal data format
    self.unit = 'C'
    if self.datatype == list:
        self.data = list(self.data)

  def toF(self):
    """ Convert self.data to Fahrenheit """
    
    #if data are a list, convert to an array. if not, leave it alone
    if self.datatype == list:
      self.data = np.asarray(self.data,dtype=float)
    elif self.datatype == str: 
      print('ERROR: data type is a string. This is not supported')

    if self.unit == 'F':
      print('WARNING: unit was already F, nothing was done')
    elif self.unit == 'K':
      self.data = (9/5.)*(self.data - 273.15) + 32
    elif self.unit =='R':
      self.data = self.data - 459.67
    elif self.unit == 'C':
      self.data = (self.data*(9/5.)) + 32
    else:
      print('ERROR, check spelling of unit')

    #set new unit and make sure you return the orginal data format
    self.unit = 'F'
    if self.datatype == list:
        self.data = list(self.data)


  def toK(self):
    """ Convert self.data to Kelvin """
    
    #if data are a list, convert to an array. if not, leave it alone
    if self.datatype == list:
      self.data = np.asarray(self.data,dtype=float)
    elif self.datatype == str: 
      print('ERROR: data type is a string. This is not supported')

    if self.unit == 'F':
      self.data = ((self.data - 32) * (5/9.)) + 273.15
    elif self.unit == 'K':
      print('WARNING: unit was already K, nothing was done')
    elif self.unit =='R':
      self.data =  self.data * (5/9.)
    elif self.unit == 'C':
      self.data = (self.data + 273.15)
    else:
      print('ERROR, check spelling of unit')

    #set new unit and make sure you return the orginal data format
    self.unit = 'K'
    if self.datatype == list:
        self.data = list(self.data)


  def toR(self):
    """ Convert self.data to Rankine"""
    
    #if data are a list, convert to an array. if not, leave it alone
    if self.datatype == list:
      self.data = np.asarray(self.data,dtype=float)
    elif self.datatype == str: 
      print('ERROR: data type is a string. This is not supported')

    if self.unit == 'F':
      self.data = self.data + 459.67
    elif self.unit == 'K':
      self.data = self.data * (9/5.)
    elif self.unit =='R':
      print('WARNING: unit was already R, nothing was done')
    elif self.unit == 'C':
      self.data = (self.data + 273.15) *(9/5.)
    else:
      print('ERROR, check spelling of unit')

    #set new unit and make sure you return the orginal data format
    self.unit = 'R'
    if self.datatype == list:
        self.data = list(self.data)

  def tester(self):

    """ 
    Function to make sure we can go to different units properly. 
    I am using freezing to check this.
    """
    
    temp_obj = MrT(data=32.,unit='F')
    flag1 = 0
    temp_obj.toC()
    if np.round(temp_obj.data,2) != 0.:
      flag1 = 1
      print('ERROR: issue in FtoC')
    
    temp_obj.toK()
    if np.round(temp_obj.data,2) != 273.15:
      flag1 = 1
      print('ERROR: issue in CtoK')
      print(temp_obj.data)
    
    temp_obj.toR()
    if np.round(temp_obj.data,2) != 491.67:
      flag1 = 1
      print('ERROR: issue in KtoR')
      print(temp_obj.data)
    
    temp_obj.toF()
    if np.round(temp_obj.data,2) != 32.:
      flag1 = 1
      print('ERROR: issue in RtoF')
      print(temp_obj.data)

    if flag1 == 0:
      print('Tests OK')
