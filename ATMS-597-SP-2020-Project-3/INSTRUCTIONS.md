# ATMS 597 SN Weather and Climate Data Science
## Project 3: xarray - Use for reducing data (version 1.0)
### Due: Friday, 28 February at midnight to Learn@Illinois

You will work in groups of 3 to complete this assignment, which are assigned on Learn@Illinois.  Students who are not taking the course for credit may join to form their own groups, however their assignment will not be graded.

Task:
Create code using python `xarray` to organize and reduce climate data.

You will work in groups of 3 to complete this assignment, which are assigned on Learn@Illinois.  Students who are not taking the course for credit may join to form their own groups, however their assignment will not be graded.

Task:
Create code using python `xarray` to organize and reduce climate data.  The goal of this analysis will be to detect global atmospheric circulation patterns (or teleconnections) associated with extreme daily precipitation in a certain part of the globe. You will 

(1) Aggregate daily rainfall data from the Global Precipitaiton Climatology Project 1 degree daily precipitation data over the period 1996 - 2019 into a single file from daily files, available here: [https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/].

(2) Determine the 95% values of daily precipitation during a selected particular 3-month period (given in the table below by group) over the grid box closest to the city you are examining.  Plot a *cumulative distribution function* of all values daily precipitation values and illustrate the 95% value of daily precipitation in millimeters.

(3) Using output from the NCEP Reanalysis [https://journals.ametsoc.org/doi/pdf/10.1175/1520-0477(1996)077%3C0437%3ATNYRP%3E2.0.CO%3B2](Kalnay et al. 1996), compute the global mean fields and seasonal anomaly fields for days meeting and exceeding the threshold of precipitation calculated in the previous step (using the 1981-2010 as a base period for anomalies) of 
- 250 hPa wind vectors and wind speed, 
- 500 hPa winds and geopotential height,
- 850 hPa temperature, specific humidity, and winds,
- skin temperature, and surface winds, and
- total atmospheric column water vapor.  

(4) Create maps showing the mean fields for the extreme precipitation day composites, long term mean composites for the selected months, and the anomaly fields for each variable.  Use contours and vectors when appropriate.

NCEP reanalysis data is available from the NOAA Physical Sciences Division THREDDS server here: [https://www.esrl.noaa.gov/psd/thredds/catalog/Datasets/catalog.html].  `xarray` can access these files directly.  For example, to get the long term mean for u-wind by month, you can access
```
data = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/uwnd.mon.ltm.nc',engine='netcdf4')
```
Aggregations of the 6-hourly data are available like this:
```
data = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Aggregations/ncep.reanalysis/pressure/uwnd.nc', engine='netcdf4')
```

Here are the group location assignments:

| Group   | Location (months to consider)            |
|---------|----------------------|
| Group 1 | Champaign, USA (JJA)      |
| Group 2 | Mumbai, India (JJA)       |
| Group 3 | Shanghai, China (JJA)     |
| Group 4 | Hilo, USA (OND)   |
| Group 5 | Jakarta, Indonesia (DJF)  |
| Group 6 | Cordoba, Argentina (DJF)  |
| Group 7 | Kinshasa, Congo (OND)     |
| Group 8 | Melbourne, Australia (DJF) |

You will gain experience using remote datasets to reduce datasets and using THREDDS calls to a data server at the National Centers for Environmental Information (NCEI).

Functionality Requirements:
* The code must use `xarray` for the data reduction, and `matplotlib` to plot the required visualizations.
* You can develop the code using Colab Notebooks, or any other way, but the repository should be submitted to GitHub as a python script (i.e., .py, not a notebook!), and include a descriptive README.md.

Code demo presentation: Each group will have a 5 minute live code demo on 13 February.  The code demo should also discuss the group's code structure, challenges and solutions, and other 

Formatting and Documentation Requirements:
* The appropriate references for the data, including DOI numbers, for the datasets used.  Also, appropriate references to the Climate Stripes creator/technique should be included.
* The code must contain docstrings and comments where appropriate.
* The code must be formatted in PEP8.

GitHub usage requirements:
* The code must be originally forked from the repository [swnesbitt/ATMS-597-SP-2020](https://github.com/swnesbitt/ATMS-597-SP-2020/) by a group member *or* you can create a new repository.
* The code must be submitted as a link to a GitHub repository in Learn@Illinois by the end of the day on the due date.  
* Each project member must have contributed to the code at least once either through branching or through forking, making a commit, with acceptance of a pull request.

Reflection:
* Each individual group member is required to submit a reflection, which can be between 100-250 words. This reflection should contain their experience in developing the homework, a discussion of challenges and how they were overcome (or not), suggestions for improving the exercise, and any issues with partners.  This reflection is submitted in the Project 3 - Reflection assignment on Learn@Illinois.

