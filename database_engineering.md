

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


