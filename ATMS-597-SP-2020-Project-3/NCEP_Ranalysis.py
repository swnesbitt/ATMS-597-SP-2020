'''
This part of code has two purposes:
1) to take an array of dates with extreme precipitation (defined as 
above 95% values of daily precipitation during season JJA) in Champaign,
IL and fetch following daily average data from NCEP/NCAR Reanalysis 
dataset for these days:
    (1) wind vectors [surface, 250, 500, 850hPa] 
    (2) wind speed [250hPa] 
    (3) temperature [850hPa, skin] 
    (4) geopotential height [500hPa] 
    (5) specific humidity [850hPa]
    (6) total atm column water vapor.

2) fetch daily long term mean data (1981-2010) for above indices, 
average to seasonal mean for JJA, and calculate seasonal anomaly for
the extreme precipitation days.

The code returns two netCDF files:
1) daily Reanalysis data for the selected extreme precipitation days,
which is 101 days and 14 single-level variables, global.

2) seasonal long term mean climate, 1 day, 14 single-level variables, 
global.

A different version of code, which has less documentation but is 
integrated in a class, is attached at the end of the file (ln 251).

ACKNOLEDGEMENT:
NCEP Reanalysis data provided by the NOAA/OAR/ESRL PSD, Boulder, Colorado, 
USA, from their Web site at https://www.esrl.noaa.gov/psd/
'''



%pylab inline
!pip install netCDF4 
!pip install pydap
import xarray as xr
import pandas as pd
import numpy as np

!apt-get -qq install libproj-dev proj-data proj-bin libgeos-dev
!pip install Cython
!pip install --upgrade --force-reinstall shapely --no-binary shapely
!pip install cartopy

import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature

### Import data:
# 'Champaign_precip_gte95quant.csv' file 
# contains dates with extreme precipitation in Champaign, IL
date_url = 'https://drive.google.com/uc?export=download&id=16wV8WP9NaEYfaLHjzIWPqZAExRKJ9ywX'
dates_gte_95 = pd.read_csv(date_url, header=None, parse_dates=[1], index_col=[1]).index

# Daily composite for extreme precipitation days:
# daily_select_data = 'https://drive.google.com/uc?export=download&id=1EGUjs0s6GzdgGw07Xn78t9ORUJdVt2CY'
# Long term mean daily data for base period (1981-2010, JJA):
# ltm_jja_mean_data = 'https://drive.google.com/uc?export=download&id=1-PyxlJH00ySZXly0AXeQ04R0fzUDE604'
# Can download and upload to colab to avoid running the code below (~5 min)

# If .nc files already in directory, run
# daily_select = xr.open_dataset('daily_select.nc', engine='netcdf4')
# ltm_JJA_mean = xr.open_dataset('ltm_JJA_mean.nc', engine='netcdf4')

### Fetch Daily and Long Term Mean Reanalysis Data
## Define a dictionary for file locations on NOAA thredds server
baseurl = 'https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/'
dailyurl = baseurl + 'ncep.reanalysis.dailyavgs/'
ltmurl = baseurl + 'ncep.reanalysis.derived/'
data_loc = {'uwnd_250' : ['pressure/uwnd.',
                        '.sel(level = 250).drop(\'level\')'],
            'uwnd_500' : ['pressure/uwnd.',
                        '.sel(level = 500).drop(\'level\')'],
            'uwnd_850' : ['pressure/uwnd.',
                        '.sel(level = 850).drop(\'level\')'],
            'vwnd_250' : ['pressure/vwnd.', 
                        '.sel(level = 250).drop(\'level\')'],
            'vwnd_500' : ['pressure/vwnd.', 
                        '.sel(level = 500).drop(\'level\')'],
            'vwnd_850' : ['pressure/vwnd.', 
                        '.sel(level = 850).drop(\'level\')'],
            'hgt_500'  : ['pressure/hgt.', 
                        '.sel(level = 500).drop(\'level\')'],
            'temp_skin': ['surface_gauss/skt.sfc.gauss.', ''],
            'temp_500' : ['pressure/air.', 
                        '.sel(level = 500).drop(\'level\')'],
            'shum_850' : ['pressure/shum.', 
                        '.sel(level = 850).drop(\'level\')'],
            'uwnd_surf': ['surface/uwnd.sig995.', ''],
            'vwnd_surf': ['surface/vwnd.sig995.', ''],
            't_col_aq' : ['surface/pr_wtr.eatm.', '']} 
# Dictionary `data_loc`:
  # Key: variable name to be stored in final `.nc` file
  # Value: [0] final part of data url
  #        [1] additional processing: select and dropping 
  #            unused levels, etc


## Download daily average data
'''
The following code was adapted from Prof. Nesbitt, available at
https://colab.research.google.com/drive/1rAXpUlTdcUvCu4goKOYPwEtxB-fuk5CU
'''
# Define range of years from `dates_gte_95`
years = pd.date_range(start=dates_gte_95[0], end=dates_gte_95[-1], freq='AS')
years

# default resolution: 2.5 deg * 2.5 deg
lat_grid = np.linspace(90, -90, 73)
lon_grid = np.linspace(0, 360, 144, False)

# Initialize empty list for datasets
datasets = []

# Loop through years. For each year, merge all data variables into one dataset.
for iyr in years.year:
    print('working on '+str(iyr))
    dates = dates_gte_95[dates_gte_95.year == iyr]
    # Initialize empty list for datasets, for all variable during this year `iyr`
    year_dataset = []
    for key in data_loc.keys():
        url = dailyurl + data_loc.get(key)[0]
        # Open dataset with Xarray, select dates and assign to temporary dateset
        data = xr.open_dataset(url + str(iyr)+'.nc',engine='netcdf4').sel(time=dates)
        # Execuate optional data processing defined in `data_loc` and rename variable
        exec('data = data' + data_loc.get(key)[1] +
             '.rename({\'' + url.split('/')[-1].split('.')[0] + '\':\'' + key + '\'})')
        # Check resolution (grid) mismatch. Interpolate to default grid.
        if size(data.lon) != size(lon_grid):
            data = data.interp(lat=lat_grid, lon=lon_grid)
        # Add temporary dateset to list of this year
        year_dataset.append(data)
    # Merge all variables of this year to one single dataset
    ds = xr.merge(year_dataset)
    # Append this year's dataset to grand list
    datasets.append(ds)
    
## Postprrocessing and save daily data
# Concat datasets of years to one dataset 
daily_select = xr.concat(datasets, dim='time')
# Calculate Wind Speed Scalar at 250 hPa.
daily_select = daily_select.assign(wspd_250 = np.sqrt(daily_select.uwnd_250**2 + 
                                                      daily_select.vwnd_250**2))
# Check dataset
# daily_select

# Check if there is the `.nc` file in the dir, if not save it. 
names = !ls daily*
if not 'daily_select.nc' in str(names):
    daily_select.to_netcdf('daily_select.nc')

## Download daily long term mean data
# Initialize empty list for datasets
ltm_dataset = []

# Loop through variables and merge all data variables into one dataset.
for key in data_loc.keys():
    url = ltmurl + data_loc.get(key)[0].replace('gauss.','')
    # Open dataset, drop unused variables
    # `xr.open_dataset`: long term mean data has dates defined in year 0001, so
    #                    specify `use_cftime = True`  
    data = xr.open_dataset(url + 'day.1981-2010.ltm.nc',
                           engine='netcdf4',
                           use_cftime = True,
                           drop_variables = ['climatology_bounds', 'valid_yr_count'])
                           #.sel(time=slice('0001-06', '0001-08'))
    # Select time (days in JJA season)
    data = data.isel(time = data.time.dt.season == 'JJA')
    # Execuate optional data processing defined in `data_loc` and rename variable 
    exec('data = data' + data_loc.get(key)[1] +
         '.rename({\'' + url.split('/')[-1].split('.')[0] + '\':\'' + key + '\'})')
    # Check resolution (grid) mismatch. Interpolate to default grid.
    if size(data.lon) != size(lon_grid):
        data = data.interp(lat=lat_grid, lon=lon_grid)
    # Append single-variable datasets to a list
    ltm_dataset.append(data)

# Merge list of variables     
ltm = xr.merge(ltm_dataset)
# Calculate Wind Speed Scalar at 250 hPa.
ltm = ltm.assign(wspd_250 = np.sqrt(ltm.uwnd_250**2 + 
                                    ltm.vwnd_250**2))
# Check dataset
# ltm

# Calculate the average LTM daily data for JJA season ('global mean fields')
ltm_JJA_mean = ltm.mean(dim='time')

# Check if there is the `.nc` file in the dir, if not save it. 
names = !ls
if not 'ltm_JJA_mean.nc' in str(names):
    ltm_JJA_mean.to_netcdf('ltm_JJA_mean.nc')
    
## Calculate mean seasonal anomaly for extreme precipitation days (1 `time`)
daily_select_mean = daily_select.mean(dim='time')
seasonal_anomaly = daily_select_mean - ltm_JJA_mean

## Calculate daily anomaly for extreme precipitation days (101 `time`)
# Daily data for animation
seasonal_anomaly_daily = daily_select - ltm_JJA_mean

### Plotting (simplified demo code for required plots)

## Sample code for calling and plotting different variables in the 
## mean fields for the extreme precipitation day composite
# var_names = []
# for data_var in daily_select_mean.data_vars:
#     var_names.append(data_var)

# fig = plt.figure()#subplots(ncols=2,nrows=7,figsize=(12,32)) # doesn't work yet

# for i in range(13):
#     fig.add_subplot(7,2,i+1) # doesn't work yet
#     ax = plt.axes(projection=ccrs.PlateCarree())
#     ax.add_feature(cfeature.COASTLINE.with_scale('110m'))
#     seasonal_anomaly.get(var_names[i]).plot()
#     plt.show()

## Sample code for calling and plotting different variables in the 
## long term mean composites for the selected months
# var_names = []
# for data_var in ltm_JJA_mean.data_vars:
#     var_names.append(data_var)

# fig = plt.figure()#subplots(ncols=2,nrows=7,figsize=(12,32)) # doesn't work yet

# for i in range(13):
#     fig.add_subplot(7,2,i+1) # doesn't work yet
#     ax = plt.axes(projection=ccrs.PlateCarree())
#     ax.add_feature(cfeature.COASTLINE.with_scale('110m'))
#     seasonal_anomaly.get(var_names[i]).plot()
#     plt.show()

## Sample code for calling and plotting different anomaly variables
# var_names = []
# for data_var in seasonal_anomaly.data_vars:
#     var_names.append(data_var)

# fig = plt.figure()#subplots(ncols=2,nrows=7,figsize=(12,32)) # doesn't work yet

# for i in range(13):
#     fig.add_subplot(7,2,i+1) # doesn't work yet
#     ax = plt.axes(projection=ccrs.PlateCarree())
#     ax.add_feature(cfeature.COASTLINE.with_scale('110m'))
#     seasonal_anomaly.get(var_names[i]).plot()
#     plt.show()

### Code above, built as methods of a class.

def grab_reanalysis(self):
    """ warning... this code takes some time. Please save the data after running"""

    
    dates_gte_95 = pd.read_csv('./subset_data/precip_gte95quant.csv', 
                               header=None, parse_dates=[1], index_col=[1]).index
    self.dates_gte_95 = dates_gte_95
    baseurl = 'https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/'
    dailyurl = baseurl + 'ncep.reanalysis.dailyavgs/'
    ltmurl = baseurl + 'ncep.reanalysis.derived/'
    data_loc = {'uwnd_250' : ['pressure/uwnd.',
                            '.sel(level = 250).drop(\'level\')'],
                'uwnd_500' : ['pressure/uwnd.',
                            '.sel(level = 500).drop(\'level\')'],
                'uwnd_850' : ['pressure/uwnd.',
                            '.sel(level = 850).drop(\'level\')'],
                'vwnd_250' : ['pressure/vwnd.', 
                            '.sel(level = 250).drop(\'level\')'],
                'vwnd_500' : ['pressure/vwnd.', 
                            '.sel(level = 500).drop(\'level\')'],
                'vwnd_850' : ['pressure/vwnd.', 
                            '.sel(level = 850).drop(\'level\')'],
                'hgt_500'  : ['pressure/hgt.', 
                            '.sel(level = 500).drop(\'level\')'],
                'temp_skin': ['surface_gauss/skt.sfc.gauss.', ''],
                'temp_500' : ['pressure/air.', 
                            '.sel(level = 500).drop(\'level\')'],
                'shum_850' : ['pressure/shum.', 
                            '.sel(level = 850).drop(\'level\')'],
                'uwnd_surf': ['surface/uwnd.sig995.', ''],
                'vwnd_surf': ['surface/vwnd.sig995.', ''],
                't_col_aq' : ['surface/pr_wtr.eatm.', '']} 

    years = pd.date_range(start=dates_gte_95[0], end=dates_gte_95[-1], freq='AS')
    # default resolution: 2.5 deg * 2.5 deg
    lat_grid = np.linspace(90, -90, 73)
    lon_grid = np.linspace(0, 360, 144, False)

    datasets = []
    for iyr in years.year:
        print('working on '+str(iyr))
        dates = dates_gte_95[dates_gte_95.year == iyr]
        year_dataset = []
        for key in data_loc.keys():
            url = dailyurl + data_loc.get(key)[0]
            data = xr.open_dataset(url + str(iyr)+'.nc',engine='netcdf4').sel(time=dates)
            exec('data = data' + data_loc.get(key)[1] +
                '.rename({\'' + url.split('/')[-1].split('.')[0] + '\':\'' + key + '\'})')
            if size(data.lon) != size(lon_grid):
                data = data.interp(lat=lat_grid, lon=lon_grid)
            year_dataset.append(data)
        ds = xr.merge(year_dataset)
        datasets.append(ds)
    daily_select = xr.concat(datasets, dim='time')
    daily_select = daily_select.assign(wspd_250 = np.sqrt(daily_select.uwnd_250**2 + daily_select.vwnd_250**2))

    self.daily_select = daily_select
    #check if there is the file in the dir, if not save it. 
    names = !ls daily*
    if not 'daily_select.nc' in str(names):
        daily_select.to_netcdf('daily_select.nc')

def grab_longtermmean(self):

    ltm_dataset = []
    for key in data_loc.keys():
        url = ltmurl + data_loc.get(key)[0].replace('gauss.','')
        data = xr.open_dataset(url + 'day.1981-2010.ltm.nc',
                              engine='netcdf4',
                              use_cftime = True,
                              drop_variables = ['climatology_bounds', 'valid_yr_count'])
                              #.sel(time=slice('0001-06', '0001-08'))
        data = data.isel(time = data.time.dt.season == 'JJA')
        exec('data = data' + data_loc.get(key)[1] +
            '.rename({\'' + url.split('/')[-1].split('.')[0] + '\':\'' + key + '\'})')
        if size(data.lon) != size(lon_grid):
            data = data.interp(lat=lat_grid, lon=lon_grid)
        ltm_dataset.append(data)

    # global mean fields
    ltm_JJA_mean = ltm.mean(dim='time')
    names = !ls
    if not 'ltm_JJA_mean.nc' in str(names):
        ltm_JJA_mean.to_netcdf('ltm_JJA_mean.nc')

    self.ltm_JJA_mean = ltm_JJA_mean
