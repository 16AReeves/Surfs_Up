# Surfs_Up
---
## Module 9: Analysis on Oahu Temperature Data from 2010-2017 using Flask, SQLite, SQLAlchemy, and MongoDB.
---
### Background
---
#### This analysis was done on Oahu temperature data from 2010-2017. This analysis was apart of data from the area to analyze if opening a surf shop and ice cream palor is sustainable year-round. This analysis focuses on June and December months, basically the start of summer and in winter, to check for differences in temperatures around this time of year. 
---
### Results
---
#### Here is summary statistics for the June and December months in Oahu during the 2010-2017 years.
June Temperature Data: | December Temperature Data:
--- | --- |
![june_temp_stats](https://user-images.githubusercontent.com/98365963/166395757-51182046-3da7-4b34-aacf-1ffd3387a7a0.PNG) | ![dec_temp_stats](https://user-images.githubusercontent.com/98365963/166395760-7df5128c-a43f-40b5-8301-4c91a4ac71ff.PNG)
* ##### The key difference in the average temperature for both months is about 4 degrees. June has an average of 75 degrees and December has an average of 71 degrees.
* ##### The key difference in the lower range of temperatures is roughly 8 degrees. June has an average low of 64 degrees and December has an average low of 56 degrees. 
* ##### The key difference in the max temperature range is 2 degrees. June has an average high of 84 degrees while December has an average high of 82 degrees. 
* ##### The standard deviation for both data sets is about 3. Considering December has 200 fewer data points, this is relatively even between the two data sets. 
* ##### Looking at the quartile ranges, both data sets have a gap between the max and minimum temperatures. June has a high of 85 with a low of 64 degrees. December has a high of 82 and a lot of 56 degrees. Meaning June has a wide range of temperatures varying 21 degrees while December has a wide range of temperatures varying 26 degrees. 
---
### Summary
---
#### The above results from the June and December data points across the 2010-2017 years is fairly similar. June is slightly hotter than December but only by a few degrees. The major difference in temperature is the average low for both months. December is colder than June by 8 degrees. Overall, the temperature differences between the months is small meaning opening a Surf-n-Shake shop seems to be worthwhile. Even if the shop is open year round, the temperatures seem to be even enough for the business to thrive. 
#### Adding to this data set, two additional queries should be looked at to help with making the decision of opening a shop in Oahu. One query should be to look at ranges of temperatures and how often they occur during the June and December months. This would be beneficial in making this decision, because if it's always significantly colder in December then business might hurt during that time of year; also considering if 82 degrees is a rarity in December then less people might want to surf and get ice cream. A second query should be to look at other temperature monitoring stations in the area on Oahu. This analysis focused on the popular station only when there were more stations that took temperature readings. Only using one stations readings could have influenced the data, or it could have little to no impact when more data points are added. It still should be looked at and considered before going forward with creating a business. 
