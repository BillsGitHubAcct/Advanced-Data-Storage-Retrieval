## Advanced-Data-Storage-Retrieval
# This document shows all three steps coded in jupyter notebook 
1. Data_Engineering
2. Database Engineering
3. Analysis of the Data

# First is Data Engineering:

```python
!rm clean_hawaii_measurements.csv clean_hawaii_stations.csv
```


```python
# Dependencies
import pandas as pd
import numpy as np
```


```python
# Read data for data engineering
measures = pd.read_csv('hawaii_measurements.csv')
stations = pd.read_csv('hawaii_stations.csv')
```


```python
measures.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>date</th>
      <th>prcp</th>
      <th>tobs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>2010-01-01</td>
      <td>0.08</td>
      <td>65</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00519397</td>
      <td>2010-01-02</td>
      <td>0.00</td>
      <td>63</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00519397</td>
      <td>2010-01-03</td>
      <td>0.00</td>
      <td>74</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00519397</td>
      <td>2010-01-04</td>
      <td>0.00</td>
      <td>76</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00519397</td>
      <td>2010-01-06</td>
      <td>NaN</td>
      <td>73</td>
    </tr>
  </tbody>
</table>
</div>




```python
measures['prcp'].max()
```




    11.529999999999999




```python
measures['prcp'].min()
```




    0.0




```python
measures['tobs'].max()
```




    87




```python
measures['tobs'].min()
```




    53




```python
stations.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>name</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>elevation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>WAIKIKI 717.2, HI US</td>
      <td>21.2716</td>
      <td>-157.8168</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00513117</td>
      <td>KANEOHE 838.1, HI US</td>
      <td>21.4234</td>
      <td>-157.8015</td>
      <td>14.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00514830</td>
      <td>KUALOA RANCH HEADQUARTERS 886.9, HI US</td>
      <td>21.5213</td>
      <td>-157.8374</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00517948</td>
      <td>PEARL CITY, HI US</td>
      <td>21.3934</td>
      <td>-157.9751</td>
      <td>11.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00518838</td>
      <td>UPPER WAHIAWA 874.3, HI US</td>
      <td>21.4992</td>
      <td>-158.0111</td>
      <td>306.6</td>
    </tr>
  </tbody>
</table>
</div>




```python
stations['latitude'].max()
```




    21.5213




```python
stations['latitude'].min()
```




    21.271599999999999




```python
stations['longitude'].max()
```




    -157.71138999999999




```python
stations['longitude'].min()
```




    -158.0111




```python
stations['elevation'].max()
```




    306.60000000000002




```python
stations['elevation'].min()
```




    0.90000000000000002




```python
stations['elevation'].median()
```




    14.6




```python
# hmm seems to be a couple of outliers based on elevation
outlier_stations_by_elevation = stations.loc[stations['elevation'] > 40]
outlier_stations_by_elevation
# Validated using google maps and coordinates that these elevations are valid
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>name</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>elevation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>USC00518838</td>
      <td>UPPER WAHIAWA 874.3, HI US</td>
      <td>21.4992</td>
      <td>-158.0111</td>
      <td>306.6</td>
    </tr>
    <tr>
      <th>8</th>
      <td>USC00516128</td>
      <td>MANOA LYON ARBO 785.2, HI US</td>
      <td>21.3331</td>
      <td>-157.8025</td>
      <td>152.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
majority_stations_by_elevation = stations.loc[stations['elevation'] <= 40]
majority_stations_by_elevation
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>name</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>elevation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>WAIKIKI 717.2, HI US</td>
      <td>21.27160</td>
      <td>-157.81680</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00513117</td>
      <td>KANEOHE 838.1, HI US</td>
      <td>21.42340</td>
      <td>-157.80150</td>
      <td>14.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00514830</td>
      <td>KUALOA RANCH HEADQUARTERS 886.9, HI US</td>
      <td>21.52130</td>
      <td>-157.83740</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00517948</td>
      <td>PEARL CITY, HI US</td>
      <td>21.39340</td>
      <td>-157.97510</td>
      <td>11.9</td>
    </tr>
    <tr>
      <th>5</th>
      <td>USC00519523</td>
      <td>WAIMANALO EXPERIMENTAL FARM, HI US</td>
      <td>21.33556</td>
      <td>-157.71139</td>
      <td>19.5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>USC00519281</td>
      <td>WAIHEE 837.5, HI US</td>
      <td>21.45167</td>
      <td>-157.84889</td>
      <td>32.9</td>
    </tr>
    <tr>
      <th>7</th>
      <td>USC00511918</td>
      <td>HONOLULU OBSERVATORY 702.2, HI US</td>
      <td>21.31520</td>
      <td>-157.99920</td>
      <td>0.9</td>
    </tr>
  </tbody>
</table>
</div>




```python
def find_columns_with_missing_values(df):
    missing_data_columns = []
    if df.isnull().values.any():
        missing_data_columns = [x for x in df.columns.values if df[df[x].isnull()].shape[0] > 0]
    return missing_data_columns
```


```python
# if stations has any missing values find columns where missing values are found
find_columns_with_missing_values(stations)
# None found
```




    []




```python
# No missing data for stations so save to "clean" csv 
stations.to_csv('clean_hawaii_stations.csv', index = False)
```


```python
# if measures has any missing values find columns where missing values are found
find_columns_with_missing_values(measures)
# 'prcp' column has missing values
```




    ['prcp']




```python
# Evaluate missing measures prcp values
# See if they look like duplicate data or data entered in error
rows_with_missing_prcp = measures[measures['prcp'].isnull()]
rows_with_missing_prcp.head()
# Data looks valid except for 'prcp' = NaN
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>date</th>
      <th>prcp</th>
      <th>tobs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>USC00519397</td>
      <td>2010-01-06</td>
      <td>NaN</td>
      <td>73</td>
    </tr>
    <tr>
      <th>26</th>
      <td>USC00519397</td>
      <td>2010-01-30</td>
      <td>NaN</td>
      <td>70</td>
    </tr>
    <tr>
      <th>29</th>
      <td>USC00519397</td>
      <td>2010-02-03</td>
      <td>NaN</td>
      <td>67</td>
    </tr>
    <tr>
      <th>43</th>
      <td>USC00519397</td>
      <td>2010-02-19</td>
      <td>NaN</td>
      <td>63</td>
    </tr>
    <tr>
      <th>61</th>
      <td>USC00519397</td>
      <td>2010-03-11</td>
      <td>NaN</td>
      <td>73</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Check Distribution by station for missing 'prcp' rows (see if concentrated in one station)
groupbystations = measures[measures['prcp'].isnull()].groupby(['station']).size()
groupbystations
# Missing prcp values for stations are pretty much spread out like all data (see next)
```




    station
    USC00511918     47
    USC00513117     13
    USC00514830    265
    USC00516128    128
    USC00517948    689
    USC00518838    169
    USC00519397     39
    USC00519523     97
    dtype: int64




```python
# Distribution by station for all data: 
groupbystations = measures.groupby(['station']).size()
groupbystations
```




    station
    USC00511918    1979
    USC00513117    2709
    USC00514830    2202
    USC00516128    2612
    USC00517948    1372
    USC00518838     511
    USC00519281    2772
    USC00519397    2724
    USC00519523    2669
    dtype: int64




```python
# Check Distribution by year for missing 'prcp' data (see if concentrated in one year)
m = measures
m['year'] = m.date.str[:4]
groupbyyear = m[m['prcp'].isnull()].groupby(['year']).size()
groupbyyear
# Missing prcp values are pretty much spread out over several years similar to years for all data (see next)
```




    year
    2010    103
    2011    168
    2012    170
    2013    196
    2014    195
    2015    245
    2016    240
    2017    130
    dtype: int64




```python
# Distribution by year for all data:
m['year'] = m.date.str[:4]
groupbyyear = m.groupby(['year']).size()
groupbyyear
```




    year
    2010    2784
    2011    2733
    2012    2640
    2013    2670
    2014    2597
    2015    2420
    2016    2309
    2017    1397
    dtype: int64




```python
# Check Distribution by year and month (see if concentrated in one month)
m['month'] = m.date.str[5:7]
groupbyyearmonth = m[m['prcp'].isnull()].groupby(['year'] + ['month']).size()
groupbyyearmonth
# Missing prcp vallues are pretty much spread out over 'year' and 'month' simlar to 'year' and 'month' for all data (see Next)
```




    year  month
    2010  01        5
          02        9
          03       11
          04        9
          05       12
          06       10
          07        9
          08        7
          09        7
          10        6
          11       13
          12        5
    2011  01        7
          02       23
          03       17
          04        8
          05       18
          06       15
          07       19
          08       16
          09       10
          10       14
          11       13
          12        8
    2012  01        8
          02       17
          03       13
          04       20
          05       13
          06       17
                   ..
    2015  03       20
          04       14
          05        8
          06       15
          07       25
          08       29
          09       21
          10       28
          11       25
          12       22
    2016  01       14
          02       25
          03       23
          04       16
          05       23
          06       21
          07       24
          08       21
          09       17
          10       19
          11       15
          12       22
    2017  01       21
          02       15
          03       20
          04       19
          05        7
          06       20
          07       18
          08       10
    Length: 92, dtype: int64




```python
groupbyyearmonth = m.groupby(['year'] + ['month']).size()
groupbyyearmonth
```




    year  month
    2010  01       201
          02       178
          03       227
          04       226
          05       246
          06       242
          07       235
          08       259
          09       248
          10       252
          11       235
          12       235
    2011  01       245
          02       221
          03       231
          04       238
          05       246
          06       227
          07       223
          08       223
          09       208
          10       227
          11       221
          12       223
    2012  01       241
          02       226
          03       222
          04       226
          05       214
          06       211
                  ... 
    2015  03       205
          04       192
          05       209
          06       203
          07       184
          08       205
          09       205
          10       217
          11       197
          12       184
    2016  01       184
          02       187
          03       196
          04       192
          05       194
          06       194
          07       187
          08       201
          09       190
          10       198
          11       186
          12       200
    2017  01       191
          02       177
          03       189
          04       190
          05       174
          06       191
          07       194
          08        91
    Length: 92, dtype: int64




```python
#Evaluate percentage of Rows with missing 'prcp' to All Rows
# Count of rows with missing prcp data
rows_with_missing_prcp = measures[measures['prcp'].isnull()].shape[0]
rows_with_missing_prcp
# 1447
# Count of rows having prcp values
rows_with_prcp = measures.dropna()
rows_with_prcp.shape[0]
# 18103
# get % of measures rows with missing prcp data to all measures rows
rows_with_missing_prcp/(rows_with_prcp.shape[0] + rows_with_missing_prcp)*100
# 7.4%
```




    7.40153452685422




```python
# Since the % of rows with missing prcp values is fairly substantial and spread evenly throughout the data... instead of 
# removing missing rows or replacing with 0, I replaced measures missing prcp values with the overall prcp mean value... This 
# retains the tob average and maintains the same prcp overall average.
measures = measures.fillna(measures['prcp'].mean())
measures.to_csv('clean_hawaii_measurements.csv', index=False)
```
# Next is Database Engineering:



```python
# Definitions
import pandas as pd
from time import time
from datetime import datetime
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, Integer, Float, Text
```


```python
# Create a connection to a SQLite database called hawaii.db
engine = create_engine('sqlite:///hawaii.db')
```


```python
# Create a connection to the engine
conn = engine.connect()
```


```python
# Use declarative base from SQLAlchemy to model the tables as an ORM class
Base = declarative_base()
```


```python
# Create the Stations class
class Station(Base):
    __tablename__ = 'stations'
    id = Column(Integer, primary_key = True)
    station = Column(Text)
    name = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
    
#Create the Measures class
class measure(Base):
    __tablename__ = 'measures'
    id = Column(Integer, primary_key=True, autoincrement=True)
    station = Column(Text)
    date = Column(Text)
    prcp = Column(Float)
    tobs = Column(Integer)
    year = Column(Text)
    month = Column(Text)
def __repr__(self):
    return f"id={self.id}, name={self.name}"
```


```python
# Create the Stations and Measures tables within the database
Base.metadata.create_all(engine)
```


```python
#load the cleaned csv files into dataframes
measures = pd.read_csv('clean_hawaii_measurements.csv')
stations = pd.read_csv('clean_hawaii_stations.csv')
```


```python
# create lists of data to write to_dict() and clean out df metadata
m_data = measures.to_dict(orient='records')
s_data = stations.to_dict(orient='records')
```


```python
metadata = MetaData(bind=engine)
metadata.reflect()
```


```python
import sqlalchemy
m_table = sqlalchemy.Table('measures', metadata, autoload=True)
s_table = sqlalchemy.Table('stations', metadata, autoload=True)
```


```python
conn.execute(m_table.delete())
conn.execute(s_table.delete())
```




    <sqlalchemy.engine.result.ResultProxy at 0x1c97d4fb438>




```python
conn.execute(m_table.insert(), m_data)
```




    <sqlalchemy.engine.result.ResultProxy at 0x1c97dd9f9e8>




```python
conn.execute(s_table.insert(), s_data)
```




    <sqlalchemy.engine.result.ResultProxy at 0x1c97dd9fe80>




```python
# Test inserts in m
conn.execute("select * from measures limit 5").fetchall()
```




    [(1, 'USC00519397', '2010-01-01', 0.08, 65, '2010', '1'),
     (2, 'USC00519397', '2010-01-02', 0.0, 63, '2010', '1'),
     (3, 'USC00519397', '2010-01-03', 0.0, 74, '2010', '1'),
     (4, 'USC00519397', '2010-01-04', 0.0, 76, '2010', '1'),
     (5, 'USC00519397', '2010-01-06', 0.16064353974479206, 73, '2010', '1')]




```python
# Test inserts in s
conn.execute("select station, longitude, latitude from stations limit 5").fetchall()
```




    [('USC00519397', -157.8168, 21.2716),
     ('USC00513117', -157.8015, 21.4234),
     ('USC00514830', -157.8374, 21.5213),
     ('USC00517948', -157.9751, 21.3934),
     ('USC00518838', -158.0111, 21.4992)]


# And Finally the Data Analysis Part:



```python
# Python SQL toolkit and Object Relational Mapper
import pandas as pd
import numpy as np
import datetime
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from datetime import date
from dateutil.relativedelta import relativedelta
from sqlalchemy import create_engine, inspect, func, desc
import matplotlib
matplotlib.use('nbagg')
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import pyplot as plt
```


```python
engine = create_engine("sqlite:///hawaii.db")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
Measures = Base.classes.measures
Stations = Base.classes.stations
session = Session(engine)
```


```python
def get_prior_years_date (string_date, yrs, format_date='%Y-%m-%d'):
    '''
    From string date return last year's same date in string format. 
    '''
    try:
        months_back = yrs * -12
        converted_date = datetime.datetime.strptime(string_date, format_date) # to datetime for math
        temp_date = converted_date + relativedelta(months = months_back) # do math
        prior_date = (temp_date.strftime('%Y-%m-%d')) # back to string
        return(prior_date)
    except exception as e:
        print(e)    
```


```python
# Query for most recent date in Measures
recent_date = session.query(Measures.date).order_by('Measures.date desc').first()
# Get string value of recent date from tuple return by query
recent_date = recent_date[0]
# Get string value of 1 year prior to recent date
prior_date = get_prior_years_date(recent_date,1)
```

    C:\Users\billw\Anaconda3\lib\site-packages\sqlalchemy\sql\compiler.py:643: SAWarning: Can't resolve label reference 'Measures.date desc'; converting to text() (this warning may be suppressed after 10 occurrences)
      util.ellipses_string(element.element))
    


```python
# Select date and precipitation from Measures for 12 months prior to most recent measurement  
sel = [Measures.date, Measures.prcp]
last_twelve_mths_measures = session.query(*sel).\
    filter(Measures.date >= prior_date[1]).\
    filter(Measures.date <= recent_date).\
    order_by(Measures.date).all()
```


```python
# Use Pandas plot to create chart for precipitation
df = pd.DataFrame(last_twelve_mths_measures, columns=['date', 'precipitation'])
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df.set_index('date',inplace=True)
df.plot(x_compat=True).legend(loc='best',fontsize='small')
plt.title('Hawaii Precipitation: %s to %s' % (prior_date, recent_date),fontsize='medium')
plt.tight_layout()
plt.show()
```


    <IPython.core.display.Javascript object>



<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA18AAAKHCAYAAAB+XPKfAAAgAElEQVR4XuydB9QmRZn972SYAB95hhmJSlIRRMm4Ys6rS04GzK5x14T5v+oququrq5gjCKKCIurqqisoIkEUJOfgMDAzhAFmmGES/3Nfuof+3unuququru56+9Y5c5TvrdS/5+mqupV6AhREQAREQAREQAREQAREQAREQAQaJzCh8RJUgAiIgAiIgAiIgAiIgAiIgAiIACS+5AQiIAIiIAIiIAIiIAIiIAIiEICAxFcAyCpCBERABERABERABERABERABCS+5AMiIAIiIAIiIAIiIAIiIAIiEICAxFcAyCpCBERABERABERABERABERABCS+5AMiIAIiIAIiIAIiIAIiIAIiEICAxFcAyCpCBERABERABERABERABERABCS+5AMiIAIiIAIiIAIiIAIiIAIiEICAxFcAyCpCBERABERABERABERABERABCS+5AMiIAIiIAIiIAIiIAIiIAIiEICAxFcAyCpCBERABERABERABERABERABCS+5AMiIAIiIAIiIAIiIAIiIAIiEICAxFcAyCpCBERABERABERABERABERABCS+5AMiIAIiIAIiIAIiIAIiIAIiEICAxFcAyCpCBERABERABERABERABERABCS+5AMiIAIiIAIiIAIiIAIiIAIiEICAxFcAyCpCBERABERABERABERABERABCS+5AMiIAIiIAIiIAIiIAIiIAIiEICAxFcAyCpCBERABERABERABERABERABCS+5AMiIAIiIAIiIAIiIAIiIAIiEICAxFcAyCpCBERABERABERABERABERABCS+5AMiIAIiIAIiIAIiIAIiIAIiEICAxFcAyCpCBERABERABERABERABERABCS+5AMiIAIiIAIiIAIiIAIiIAIiEICAxFcAyCpCBERABERABERABERABERABCS+5AMiIAIiIAIiIAIiIAIiIAIiEICAxFcAyCpCBERABERABERABERABERABCS+5AOuBF4J4FtJooMBnGPIwDW+a326Gv8WANsC+H8APjJUSf73hwHcCmC7Cg/wbQCvyEm3CsC9AC4H8BMA3wTwYIX8u5Ak6zdNtFNN5++bIf3kZof3znf5ofLbBsA/AmDb8iQAWycF3wHgfABfBfB7y8o8EcDbATwLwFbJu3EJ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Tz8dN998MzbffHNcfvnl6+IvW7YMX//61/GTn/xkkO+qVauw3Xbb4R//8R/xlre8BTNn5t/yedFFF+ErX/kKLrjgAixevBizZs0apHvuc5+LN7zhDdhoo40GZRRtO8z+/aijjsLHP/5xnHPOOYNVLeZz3HHHgcJn0qRJ454tTwyljPJ4Zs+aMf+f/exn+NOf/oQFCxaAz77lllti//33xzve8Q7suuuu47Kwzbds2+Ftt92Gz372s/jtb38LrtpNnz4du+++O44//ni89KUvXa/K2efbd999B1zOPfdcLF26FDvssANe+9rXDtK6BNM7JvHlQtNzXIkvz0Ajy04D1LAGE+9wvMVarG0ISHzZUPIfxzQw/MRf78eJlz7gv+CGcnzPHrNwwp6PCA8fIR3Y//M//zO+9KUvYZ999hkIhksvvRQUWRQ5Z511Fvbcc891xaXia968eYOB/m9+85tBuk022QT33nsvzj777EHc22+/HYcccgiuueYabLrppnjiE5+IadOmDQQbBdXjH/94/PznP8ewCPnUpz41EFX8PAMFC7fbUTRdf/31oD1///vfD8q1EV8UXr/61a8wZcoU7L333oN8zj///IEIPOyww/C1r33NKL5e97rXgWLwlltuGeRB8ZaGF73oRXjJS14y+E8youjaeeedMWfOnMHfrr76alAgbbjhhvjRj36EAw44YF1a23yLxNfFF1+MQw89FPfdd99ACD/5yU/GXXfdNRCsa9asGYioz3zmM7nPRwH7ve99b7C18glPeMJg6ybzY/jIRz6Ct7/97dbuZXrHJL6sUfqPKPHln2lMOWqAGtZa4h2Ot1iLtQ0BiS8bSv7jmAaGEl+P3KTHFZMf/OAHOPDAAwf/zcH7e9/73oE4eexjH4sLL7xw3SpRKr4Yb+7cuQNxxjjZQOH0nOc8ZzCgf/WrX41/+7d/w4wZMwZRuCL0tre9bSBGjj76aJx00knrkjKvV7ziFQPRx1W4Zz/72ePyPe+88wZijAKRwbTyxTgUR1/96lcHq3kMFH8Uhffcc89gde2II45YV0bRNkCb7YFc9SK/rJgkBz7HO9/5zkG9yXHChEevgrDJN098cevkU57ylIEYZR4f+9jH1tmHz/eyl71scDsiVx0p0NKQlsf//pd/+Re8//3vX5eOq5evf/3rB6uM11577cAnbILpHZP4sqHY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" width="767.1111111111111">



```python
print('precipitation statistic:')
df.describe(include='all')
```

    precipitation statistic:
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>precipitation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>19550.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.160644</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.451064</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.020000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.160644</td>
    </tr>
    <tr>
      <th>max</th>
      <td>11.530000</td>
    </tr>
  </tbody>
</table>
</div>




```python
sel = [func.count(Stations.station)]
count_of_stations_query = session.query(*sel).all()
station_count, = count_of_stations_query
print('Total number of stations: %s' % (station_count))
```

    Total number of stations: 9
    


```python
sel = [Measures.station, func.count(Measures.station)]
station_activity_query = session.query(*sel).group_by(Measures.station).\
order_by(desc(func.count(Measures.station))).all()
print('List of stations in descending activity order:')
station_activity_query
```

    List of stations in descending activity order:
    




    [('USC00519281', 2772),
     ('USC00519397', 2724),
     ('USC00513117', 2709),
     ('USC00519523', 2669),
     ('USC00516128', 2612),
     ('USC00514830', 2202),
     ('USC00511918', 1979),
     ('USC00517948', 1372),
     ('USC00518838', 511)]




```python
# set up list of selected values from Stations and Measures
sel = [Stations.station, Stations.name, func.count(Measures.station)]
# Join Station with Measures on station and return the station_no and name having
# the highest count of associated Measures records.
station_activity_query = session.query(*sel).\
    filter(Stations.station == Measures.station).\
group_by(Stations.station).\
order_by(desc(func.count(Measures.station))).first()

ma_station_no = station_activity_query[0]
ma_station_name = station_activity_query[1]

print('Station with most activity: %s (%s)' % (ma_station_name, ma_station_no))
```

    Station with most activity: WAIHEE 837.5, HI US (USC00519281)
    


```python
# Select date and tobs from Measures for 12 months prior to most recent measurement  
sel = [Measures.date, Measures.tobs]
last_twelve_mths_tobs = session.query(*sel).\
    filter(Measures.date >= prior_date).\
    filter(Measures.date <= recent_date).\
    filter(Measures.station == ma_station_no).\
    order_by(Measures.tobs).all()
# Convert from tuple temp list to list of temps
last_twelve_mths_tobs
tobs = last_twelve_mths_tobs
tobs_list = [i[1] for i in tobs]
```


```python
# Plot histogram of temp observations for most active station
#create legend
handles = [Rectangle((0,0),1,1,color="blue",ec="k")]
labels= ["tobs"]
plt.legend(handles, labels)
plt.hist(tobs_list, bins=12, color="blue")
plt.xlabel('Temperatures', fontsize='small')
plt.ylabel('Activity', fontsize='small')
plt.title('Station: %s (%s)' % (ma_station_name, ma_station_no),fontsize='medium')
plt.tight_layout()
plt.show()
```


    <IPython.core.display.Javascript object>



<img src="data:image/png;base64,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" width="640">



```python
# USC00511918 Honolulu from 7-2-2018 to 7-16-2018()
def calc_temps (start_date, end_date, yrs, station='USC00511918'):
    """ 
        From  station (default UC00511918), start_date, and end_date
        Return avg, max and min tobs from same date range for the previous year
        If data not found then select again for the next previous year range... repeat until
        data is found or user specified years have been searched.
        *** Note USC00511918 didn't have data until 7-2-2015 t0 7-16-2015
    """ 
    # prior_start = datetime.datetime.strptime(start_date,'%Y-%m-%d')
    # Get string value of 1 year prior to start date
    prior_start_date = get_prior_years_date(start_date,1) 
    prior_end_date = get_prior_years_date(end_date,1)
    counter = 0
    while (counter < yrs):
        try:
            sel = [ 
               func.avg(Measures.tobs), 
               func.max(Measures.tobs), 
               func.min(Measures.tobs)
                   ]
            prior_year_calcs = session.query(*sel).\
                filter(Stations.station == station).\
                filter(Stations.station == Measures.station).\
                filter(Measures.date >= prior_start_date).\
                filter(Measures.date <= prior_end_date).\
            group_by(Stations.station).all()
            if len(prior_year_calcs) == 0:
                prior_start_date = get_prior_years_date(prior_start_date,1)
                prior_end_date = get_prior_years_date(prior_end_date,1)
            else:
                return prior_year_calcs
                break
            counter +=1
        except exception as e:
            print(e)
```


```python
years = input('Number of years to search back for data --> ')
print('Analyze dates (from future Honolulu Vacation dates) for %s years back' % (years)) 
results = calc_temps('2018-07-02','2018-07-16',int(years))
results = list(np.ravel(results))
results
```

    Number of years to search back for data --> 3
    Analyze dates (from future Honolulu Vacation dates) for 3 years back
    




    [74.375, 77.0, 71.0]




```python
# Plot single bar for trip avg temp and include terr of tmax-tmin
average = results[0]
tmax = results[1]
tmin = results[2]
terr = tmax - tmin
plt.bar(1, average, color='r', yerr=terr)
# add some text for labels, title and axes ticks
plt.ylabel('Temp (f)')
plt.title('Trip Avg Temp')
plt.xlim([0, 2])
#plt.axis('off')
plt.tight_layout()
plt.show()

```


    <IPython.core.display.Javascript object>



<img src="data:image/png;base64,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3QwuucJmya1OrAorlfyzl9RkFHW4c5goMOFlAePrK8rRBrJP4cyzCHRD2F3lenN2UemLjr7TIDbZO05fed9IDnSvn6zeKwIiIAIiIAIiIAIiMCQBOdBDfjY1WgREQAREQAREQAREoBcBOdC9yOu9IiACIiACIiACIiACQxKQAz3kZ1OjRUAEREAEREAEREAEehGQA92LvN4rAiIgAiIgAiIgAiIwJAE50EN+NjVaBERABERABERABESgFwE50L3I670iIAIiIAIiIAIiIAJDEpADPeRnU6NFQAREQAREQAREQAR6EZAD3Yu83isCIiACIiACIiACIjAkATnQQ342NVoEREAEREAEREAERKAXATnQvcjrvSIgAiIgAiIgAiIgAkMSkAM95GdTo0VABERABERABERABHoRkAPdi7zeKwIiIAIiIAIiIAIiMCQBOdBDfjY1WgREQAREQAREQAREoBcBOdC9yOu9IiACIiACIiACIiACQxKQAz3kZ1OjRUAEREAEREAEREAEehGQA92LvN4rAiIgAiIgAiIgAiIwJAE50EN+NjVaBERABERABERABESgFwE50L3I670iIAIiIAIiIAIiIAJDEpADPeRnU6NFQAREQAREQAREQAR6EZAD3Yu83isCIiACIiACIiACIjAkATnQQ342NVoEREAEREAEREAERKAXATnQvcjrvSIgAiIgAiIgAiIgAkMSkAM95GdTo0VABERABERABERABHoRkAPdi7zeKwIiIAIiIAIiIAIiMCQBOdBDfjY1WgREQAREQAREQAREoBcBOdC9yOu9IiACIiACIiACIiACQxKQAz3kZ1OjRUAEREAEREAEREAEehGQA92LvN4rAiIgAiIgAiIgAiIwJIH/A7eqrAthbVxzAAAAAElFTkSuQmCC" width="640">



```python
def rainfall_per_weather_station (start_date, end_date):
    """ 
        From probable vacation 2018 start_date, and end_dates
        return rainfall per weatherstation from same date range for the previous year
    """ 
    # prior_start = datetime.datetime.strptime(start_date,'%Y-%m-%d')
    # Get string value of 1 year prior to start date
    prior_start_date = get_prior_years_date(start_date,1) 
    prior_end_date = get_prior_years_date(end_date,1)
    sel = [ 
       Stations.station, 
       Stations.name, 
       func.sum(Measures.tobs)
           ]
    results = session.query(*sel).\
        filter(Stations.station == Measures.station).\
        filter(Measures.date >= prior_start_date).\
        filter(Measures.date <= prior_end_date).\
    group_by(Stations.station).all()
    return results
results = rainfall_per_weather_station('2018-07-02','2018-07-16')
results
```




    [('USC00513117', 'KANEOHE 838.1, HI US', 1157),
     ('USC00514830', 'KUALOA RANCH HEADQUARTERS 886.9, HI US', 964),
     ('USC00516128', 'MANOA LYON ARBO 785.2, HI US', 1133),
     ('USC00517948', 'PEARL CITY, HI US', 645),
     ('USC00519281', 'WAIHEE 837.5, HI US', 1142),
     ('USC00519397', 'WAIKIKI 717.2, HI US', 1195),
     ('USC00519523', 'WAIMANALO EXPERIMENTAL FARM, HI US', 1124)]



