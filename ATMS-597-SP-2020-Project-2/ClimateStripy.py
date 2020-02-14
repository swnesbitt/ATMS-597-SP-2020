import requests
import pandas as pd
import time
import tqdm
import numpy as np
import matplotlib.pylab as plt

class ClimateStripy:
  """ 
  Authors: Randy J. Chase, ENTER YOUR NAME HERE, ENTER YOUR NAME HERE

  Welcome to ClimateStripy! This class is designed to help users create their 
  own "Climate Stripes". See this page for the original idea: 
  https://showyourstripes.info/

  This is the submission to University of Illinois' ATMS 597, Project 2

  What this class can do is:
  1) Find your closest station with TMAX and TMIN long enough to do the stripes 
  (need 1970 - 2000). 

  2) It will go get the daily data and then compute the anomalies, with the 
  choice of timescale (currently supported is Monthly and Yearly, Weekly is a 
  pain because of leap years, and is going to be noisy anyway)
  
  3)Plot the stripes using matplotlib with option to overlay timeseries ontop

  What you will need: 
  1) Token from NCEI;
  https://www.ncdc.noaa.gov/cdo-web/token 

  Python Packages: 
  1) requests
  2) pandas 
  3) time 
  4) tqdm 
  5) pyproj << 2.0 (I use !pip install pyproj==1.9.5.1)
  6) cartopy,metpy *if you want a map 

  """

  def __init__(self,token=None): 
        self.request = None
        self.station = None
        self.station_df = None
        if token is None:
          self.token= None
        if token is not None:
          self.token=token
      
  def find_my_station(self,extent=None,limit=1000,reference_point=None,verbose=True):
    """
    This method will isolate a list of stations within some lat lon box if 
    extent is given. If a reference point is given it will choose the closest, 
    but also return a dataframe with all the stations in a 1by1 degree box.It 
    will make sure there is the required range of data to make the stripes
    (1971 - 2000)

    Inputs: 
    reference_point: list, [lat, lon]
    extent: list, [min_lat,min_lon,max_lat,max_lon]
    verbose: book, spit out the station chosen 

    """

    self.reference_point=reference_point
    if reference_point is None:
      if extent is None:
        print('ERROR: no extent given')
      else:
        request = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?datasetid=GHCND&datatypeid=TMIN&datatypeid=TMAX&limit=1000&extent='+str(extent[0])+','+str(extent[1])+','+str(extent[2])+','+str(extent[3]), headers={'token':self.token})
        self.request = request
        list_of_stations = self.request.json()
        df = pd.DataFrame(list_of_stations['results'])
        self.station_df = df
    else:
      extent = [reference_point[0] - 1,reference_point[1]-1,reference_point[0] + 1,reference_point[1]+1]

      extent = [reference_point[0] - 1,reference_point[1]-1,reference_point[0] + 1,reference_point[1]+1]
      request = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?datasetid=GHCND&datatypeid=TMIN&datatypeid=TMAX&limit=1000&extent='+str(extent[0])+','+str(extent[1])+','+str(extent[2])+','+str(extent[3]),headers={'token':CS.token})
      self.request = request

      # self.make_request(endpoint='stations',payload={'extent':extent,'limit': limit,'datatypeid': 'TMIN'},token=self.token)
      list_of_stations = self.request.json()
      df = pd.DataFrame(list_of_stations['results'])
      self.station_df = df
      #this is envoke the pyproj package. Please note this must be an old version** < 2.0 
      from pyproj import Proj
      p = Proj(proj='aeqd', ellps='WGS84', datum='WGS84', lat_0=reference_point[0], lon_0=reference_point[1])
      x,y = p(self.station_df.longitude.values,self.station_df.latitude.values)
      self.station_df.insert(len(self.station_df.keys()),'distance',np.sqrt(x**2 + y**2)/1000)

      #required time range 1971 - 2000 needed for the mean...
      self.station_df = self.station_df.astype({'mindate': np.datetime64})
      self.station_df = self.station_df.astype({'maxdate': np.datetime64})
      length = (self.station_df.maxdate.values - self.station_df.mindate.values)
      self.station_df.insert(len(self.station_df.keys()),'length_of_record',length)     
      self.station_df = self.station_df.where((self.station_df.mindate < np.datetime64('1971-01-01')))
      self.station_df = self.station_df.where((self.station_df.maxdate > np.datetime64('2000-12-31')))
      #make sure there is good data coverage
      self.station_df = self.station_df.where((self.station_df.datacoverage > 0.8))
      self.station_df = self.station_df.dropna()

      self.reference_point=reference_point
      self.station = self.station_df.loc[pd.Series.idxmin(self.station_df['distance'])]
      self.stationid = self.station.id

      if verbose:
        print('The closes station to your reference point is {} km away'.format(np.round(self.station.distance,2)))
        print('Here is all the station meta data:')
        print(self.station)

  def select_station(self,id=None):
    """ 
    In case you dont like the closest station, you can select a station from the 
    returned station_df
    """

    if id is None: 
      pass
    else:
      temp_df = self.station_df.set_index("id")
      self.station = temp_df.loc[id]
      self.station_id = id

  def mapper(self,zoom=None):
    """ 
    This method will map all the points found in the find_my_station method. It
    uses cartopy, so make sure you have that if you want a map. 
    
    zoom: int, how far you wish to zoom out (if positive). In degrees
    """
    if self.station_df is None: 
      print('ERROR: Please run find_my_station method first')
    else:
      ###import cartopy stuff
      import cartopy
      import cartopy.crs as ccrs
      import cartopy.feature as cfeature
      import matplotlib.ticker as mticker
      from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
      import cartopy.io.shapereader as shpreader
      from cartopy.mpl.geoaxes import GeoAxes
      from mpl_toolkits.axes_grid1 import AxesGrid
      from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
      from metpy.plots import USCOUNTIES
      ###

      #make figure
      fig = plt.figure(figsize=(10, 10))
      #add the map
      ax = fig.add_subplot(1, 1, 1,projection=ccrs.PlateCarree())

      #draw map things 
      ax.add_feature(cfeature.STATES.with_scale('10m'),lw=0.5)
      ax.add_feature(cartopy.feature.OCEAN.with_scale('50m'))
      ax.add_feature(cartopy.feature.LAND.with_scale('50m'), edgecolor='black',lw=0.5,facecolor=[0.95,0.95,0.95])
      ax.add_feature(cartopy.feature.LAKES.with_scale('50m'), edgecolor='black')
      ax.add_feature(cartopy.feature.RIVERS.with_scale('50m'))
      ax.add_feature(USCOUNTIES.with_scale('5m'))

      if zoom is None:
        zoom = 1
      #set corners of the map. 
      corners = [CS.reference_point[1] - zoom,CS.reference_point[1] + zoom,CS.reference_point[0]- zoom,CS.reference_point[0]+ zoom]

      #this set_extent crashes the python session. Not sure why... 
      # ax.set_extent((CS.reference_point[1] - 5,CS.reference_point[1] + 5,CS.reference_point[0]- 2,CS.reference_point[0]+ 2),crs=ccrs.PlateCarree())

      #draw ticks
      ax.set_xticks(np.arange(corners[0], corners[1], 1), crs=ccrs.PlateCarree())
      ax.set_yticks(np.linspace(corners[2], corners[3], 5), crs=ccrs.PlateCarree())
      lon_formatter = LongitudeFormatter(zero_direction_label=True)
      lat_formatter = LatitudeFormatter()
      ax.xaxis.set_major_formatter(lon_formatter)
      ax.yaxis.set_major_formatter(lat_formatter)

      #force bounds
      ax.set_xlim([corners[0],corners[1]])
      ax.set_ylim([corners[2],corners[3]])

      #plot stations colored by distance 
      pm = ax.scatter(self.station_df.longitude,self.station_df.latitude,c=self.station_df.distance,s=(self.station_df.length_of_record.values.astype(int)/3.154e+16)/2,zorder=2)
      plt.colorbar(pm,ax=ax,label='Distance')

      ax.plot(self.reference_point[1],self.reference_point[0],'*k',ms=15,markerfacecolor='w',markeredgewidth=2,zorder=10,label='Reference_point')
      ax.plot(self.station.longitude,self.station.latitude,'sk',ms=10,markerfacecolor='w',markeredgewidth=2,label='Closest_Station')
      ax.legend()
