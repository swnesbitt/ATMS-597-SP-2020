from tqdm import tqdm
import xarray as xr
import numpy as np
import wget
import os 
from bs4 import BeautifulSoup
import re
import urllib.request
import pandas as pd

def download_par(item):
  ff=wget.download(item,'./raw_data/'+item[-40:])
  return

class Rainy():
  """
  A Class to analyze the Global Precipitation Climatology Project (https://www.esrl.noaa.gov/psd/data/gridded/data.gpcp.html). 
  """

  def __init__(self): 
    pass


  def getLinks(self,BASE_URL=None,TIME1=None,TIME2=None,verbose=True,begin_month = 6,end_month = 8):
    
    """
    This method uses webscraping (and Beautiful soup) to grab the links for the precip data. 
    By default, it will create the links for 1996 to current. Also this defaults 
    to NH summer. Currently any months greater than 10 are unsupported... 
    """

    if BASE_URL is None: 
      BASE_URL = 'https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/'

    if TIME1 is None:
      TIME1 = '1996-01-01'
    
    if TIME2 is None: 
      TIME2 = '2019-11-30'

    time_range=pd.date_range(start=TIME1,end=TIME2,freq='Y')
    links = []
    if verbose:
      for item in time_range.year:
          url=BASE_URL+str(item)
          print('year = ',item)
          print('Getting links from '+url)
          html_page = urllib.request.urlopen(url)
          soup = BeautifulSoup(html_page.read())
          for link in soup.findAll('a', attrs={'href': re.compile("^gpcp_v01r03_daily_d\d\d\d\d0(["+str(begin_month)+"-"+str(end_month)+"])")}):
              links.append(url+'/'+link.get('href'))
    else:
      for item in tqdm(time_range.year):
          url=BASE_URL+str(item)
          html_page = urllib.request.urlopen(url)
          soup = BeautifulSoup(html_page.read())
          for link in soup.findAll('a', attrs={'href': re.compile("^gpcp_v01r03_daily_d\d\d\d\d0(["+str(begin_month)+"-"+str(end_month)+"])")}):
              links.append(url+'/'+link.get('href'))

    self.links = links

  def download_links(self,parallel=True):
    """ 
    Download all files that are found in self.links, which should be created by the self.getLinks() method.
    
    If parallel is True it will do it in parallel with the number of cpus avail. for your machine. 
    
    """
    
    if os.path.isdir('./raw_data/') is False:
      os.mkdir('./raw_data/')

    if parallel:
      import multiprocessing as mp
      n_cpu = mp.cpu_count()
      pool = mp.Pool(processes=n_cpu)
      for _ in tqdm(pool.imap_unordered(download_par, self.links), total=len(self.links)):
          pass
      pool.close()
      pool.join()
    else:
      # Download all these files to this Google Drive folder
      for item in tqdm(self.links):
        ff=wget.download(item,'./raw_data/'+item[-40:])
    
  
  def get_loc(self,lon=None,lat=None,method='nearest'):
    """ 
    This will select the closest grid point to your lat lon of interest. If lat lon is None, it will default to Champaign,IL
    """
    
    if lon is None:
      lon = (360.-88.2434)
    if lat is None:
      lat = 40.1164
    data=xr.open_mfdataset('./raw_data/gp*.nc',combine='by_coords',concat_dim='time')
    data_champaign_jja=data.precip.sel(latitude=lat,longitude=lon,method=method)
    data_final=data_champaign_jja.to_series()   #Convert DataArray to Pandas Series for more flexibility 
    data_final[data_final==data_final.max()]=np.nan #Set unphysical values (O(1e36)) to NaNs 

    self.data = data_final

  def plot_cdf(self):
    """ This makes the CDF plot to help visualize the distribution of data at your desired location""" 

    import matplotlib 
    import matplotlib.pylab as plt

    matplotlib.rcParams.update({'font.size': 16.0})
    fig=plt.figure(figsize=(11,8))
    self.data.hist(cumulative=True, density=1,bins=500)
    perc95=self.data.quantile(q=0.95)
    plt.axvline(perc95,color='r')
    plt.title('CDF of JJA daily precip over Champaign, IL')
    plt.xlabel('Daily precipitation (mm)')
    plt.text(20.2,0.8,'95th percentile = '+str(perc95))


  def split_on_quantile(self,quantile=0.95):
    """ 
    This will split the data and save some files so you dont have to keep re-downloading things later on
    """
    if os.path.isdir('./subset_data/') is False:
      os.mkdir('./subset_data/')
    percentile=self.data.quantile(q=quantile)
    dates_lt_percentile=pd.Series(self.data[self.data<percentile].index)   #Dates for data less than the percentile
    dates_gte_percentile=pd.Series(self.data[self.data>=percentile].index) #greater than or equal to the  percentile

    dates_gte_percentile.to_csv('./subset_data/precip_gte'+str(int(quantile*100))+'quant.csv')
    dates_lt_percentile.to_csv('./subset_data/precip_lt'+str(int(quantile*100))+'quant.csv')

