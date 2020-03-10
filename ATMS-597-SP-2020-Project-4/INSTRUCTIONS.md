# ATMS 597 SP 2020
## Project 4 - Using regression for prediction (version 1.0)

### Due Friday, March 26, at midnight

You will work in groups of 3 to complete this assignment, which are assigned on Learn@Illinois. Students who are not taking the course for credit may join to form their own groups, however their assignment will not be graded.

Tasks: (1) Use multiple linear regression to predict a WxChallenge-like forecast using past Global Forecast System (GFS) forecast data. (2) Repeat (1) with random forest regression.

Your prediction with each task:
Using the 12 UTC forecast and observations up to but not including the following 00 UTC, predict the following variables for the period 6 UTC to 6 UTC the following day:
- Maximum Temperature (°C)
- Minimum Temperature (°C)
- Maximum Wind Speed (m/s)
- Total precipitation accumulation (mm)

The following files are provided:

`KCMI_hourly.csv` Hourly observations from KCMI that can be used for training and validation.

`KCMI_daily_obs.csv` Daily extrema values (precip is often missing in these files), so use the file above to compute daily precip.  Contains maximum temperature, minimum temperature, and maximum wind speed (which are different than hourly observations)

Tar files of the following:

`daily.tar.gz` Files (in csv format) containing the GFS 12 UTC initialization forecasts (initialized at the date in the file name and csv index), with the GFS values of maximum temperature, minimum temperature, maximum winds speed and precipitation accumulation for the period 6 UTC to 6 UTC the following day.

`sfc.tar.gz` Files (in csv format) containing the GFS 12 UTC initialization forecasts (initialized at the date in the file name and csv index), with the 3 hourly time series of surface forecast parameters from 0 to 72 hour forecast.

`prof.tar.gz` Files (in csv format) containing the GFS 12 UTC initialization forecasts (initialized at the date in the file name and csv index), with the 3 hourly time series of forecast upper air parameters from 0 to 72 hour forecast.  Data has been interpolated to pressure levels indicated in the file.

---

Use the data from 2010-2018 as training data and 2019 as a validation set.

The groups with the best values of (a) multiple linear regression and (2) random forest regression root mean squared error summed across all variables will be given a prize.

You may not use any other data other than the data given or synthetic data created from the data itself (i.e., persistence) or values implicit with time (i.e., sun angle, day of year, etc.).

Good luck!
