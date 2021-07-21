# SQLAlchemy Homework - Surfs Up!

## Step 1 - Climate Analysis and Exploration
To begin, used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. All of the analysis is completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

## Precipitation Analysis

    Started by finding the most recent date in the data set.
    Using this date, retrieved the last 12 months of precipitation data by querying the 12 preceding months of data.
    Selected only the date and prcp values.
    Loaded the query results into a Pandas DataFrame and set the index to the date column.
    Sorted the DataFrame values by date.
    Plotted the results using the DataFrame plot method.
    Used Pandas to print the summary statistics for the precipitation data.

## Station Analysis

    Designed a query to calculate the total number of stations in the dataset.
    Designed a query to find the most active stations (i.e. which stations have the most rows?).
    Listed the stations and observation counts in descending order.
    Found which station id has the highest number of observations?
    Used the most active station id, to calculate the lowest, highest, and average temperature.
    Designed a query to retrieve the last 12 months of temperature observation data (TOBS).
    Filtered by the station with the highest number of observations.
    Queried the last 12 months of temperature observation data for this station.
    Plotted the results as a histogram with bins=12.
    Close out your session.

## Step 2 - Climate App
  Designed a Flask API based on the queries developed.

Use Flask to create your routes.

Routes

     / 
    Home page.
    List all routes that are available.
        
    /api/v1.0/precipitation
    Convert the query results to a dictionary using date as the key and prcp as the value.
    Return the JSON representation of your dictionary.
    
    /api/v1.0/stations
    Return a JSON list of stations from the dataset.
    
    /api/v1.0/tobs
    Query the dates and temperature observations of the most active station for the last year of data.
    Return a JSON list of temperature observations (TOBS) for the previous year.
    
    /api/v1.0/<start> and /api/v1.0/<start>/<end>
    Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.


## Temperature Analysis I

    Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

    Used pandas to perform this portion.

    Converted the date column format from string to datetime.

    Set the date column as the DataFrame index

    Dropped the date column

    Identified the average temperature in June at all stations across all available years in the dataset. Did the same for December temperature.

    Used the t-test to determine whether the difference in the means, if any, is statistically significant. Useda paired t-test



## Temperature Analysis II

    Looking to take a trip from August first to August seventh of this year, but worried that the weather will be less than ideal. Using historical data in the dataset find out what the temperature has previously looked like.

    Plot the min, avg, and max temperature from your previous query as a bar chart.
    Use "Trip Avg Temp" as the title.
    Use the average temperature as the bar height (y value).
    Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

Daily Rainfall Average

    Now that you have an idea of the temperature lets check to see what the rainfall has been, you don't want a when it rains the whole time!
    Calculate the rainfall per weather station using the previous year's matching dates.
    Sort this in descending order by precipitation.
