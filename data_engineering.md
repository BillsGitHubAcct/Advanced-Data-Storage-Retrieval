

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
