# ATMS 597 SN Weather and Climate Data Science
## Project 2: Pandas - Use for reducing data (version 1.0)
### Due: 13 February at midnight to Learn@Illinois

You will work in groups of 3 to complete this assignment, which are assigned on Learn@Illinois.  Students who are not taking the course for credit may join to form their own groups, however their assignment will not be graded.

Task:
Create code using python `pandas` to organize and reduce climate data.  You will gain experience using an API call to a data server at the National Centers for Environmental Information (NCEI) to produce a visualization of so-called *climate stripes*, created by [Ed Hawkins at the University of Reading](https://showyourstripes.info/).  Our version of climate stripes will optionally add a quantitative plot over top of the plot so you can plot with axis labels to see the values of temperature and time corresponding to the plot.  This new version will add axes and a line graph showing the time and value axes on the x- and y-axes, respectively.

Here is an example of one vision of the code functionality, without labels:
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/20190705_Warming_stripes_BEHIND_line_graph_-_Berkeley_Earth_%28world%29.png/2560px-20190705_Warming_stripes_BEHIND_line_graph_-_Berkeley_Earth_%28world%29.png">
By <a href="//commons.wikimedia.org/wiki/User:RCraig09" title="User:RCraig09">RCraig09</a> - <span class="int-own-work" lang="en">Own work</span>, <a href="https://creativecommons.org/licenses/by-sa/4.0" title="Creative Commons Attribution-Share Alike 4.0">CC BY-SA 4.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=80170965">Link</a>

Some of the functionality of this assignment can be adapted from Chapter 4 of the following repository that accompanies the text [Hands on Data Analysis with Pandas](https://github.com/stefmolin/Hands-On-Data-Analysis-with-Pandas/tree/master/ch_04) by Stefanie Moline.

Functionality Requirements:
* The code must be called with a GHCN site id, a date range, a flag whether to plot the data over the stripes, and a time period to average over for each stripe (i.e. annual, monthly, weekly, etc.).  The code should download the data automatically from NCEI using the [API version 2](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) and use `pandas` for the data reduction, and `matplotlib` to plot the visualization.
* You can develop the code using Colab Notebooks, or any other way, but the repository should be submitted to GitHub as a python script (i.e., .py, not a notebook!), and include a descriptive README.md.

Code demo presentation: Each group will have a 5 minute live code demo on 13 February.  The code demo should also discuss the group's code structure, challenges and solutions, and other 

Formatting and Documentation Requirements:
* The appropriate references for the data, including DOI numbers, for the datasets used.  Also, appropriate references to the Climate Stripes creator/technique should be included.
* The code must contain docstrings and comments where appropriate.
* The code must be formatted in PEP8.

GitHub usage requirements:
* The code must be originally forked from the repository [swnesbitt/ATMS-597-SP-2020](https://github.com/swnesbitt/ATMS-597-SP-2020/) by a group member.
* The code must be submitted as a link to a GitHub repository in Learn@Illinois by the end of the day on the due date.  
* Each project member must have contributed to the code at least once either through branching or through forking, making a commit, with acceptance of a pull request.

Reflection:
* Each individual group member is required to submit a reflection, which can be between 100-250 words. This reflection should contain their experience in developing the homework, a discussion of challenges and how they were overcome (or not), suggestions for improving the exercise, and any issues with partners.  This reflection is submitted in the Project 1 - Reflection assignment on Learn@Illinois.

