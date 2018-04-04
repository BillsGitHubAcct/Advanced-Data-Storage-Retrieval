import datetime
from datetime import date
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from dateutil.relativedelta import relativedelta
from sqlalchemy import create_engine, inspect, func, desc

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measures = Base.classes.measures
Stations = Base.classes.stations

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

def get_prior_years_date (string_date, yrs, format_date='%Y-%m-%d'):
    '''
    From a string date use datetime to calculate a prior date
    based on yrs parameter and default format of 'YYYY-MM-DD'
	'''
    try:
        months_back = yrs * -12
        converted_date = datetime.datetime.strptime(string_date, format_date) # to datetime for math
        temp_date = converted_date + relativedelta(months = months_back) # do math
        prior_date = (temp_date.strftime('%Y-%m-%d')) # back to string
        return(prior_date)
    except exception as e:
        print(e)

def calc_temps (start_date, end_date):
    """
        Return avg, max and min tobs from date >= start and <= end
        or if end is null then from date >= start
    """
    if end_date != '':
        sel = [
           func.avg(Measures.tobs),
           func.max(Measures.tobs),
           func.min(Measures.tobs)
               ]
        calcs = session.query(*sel).\
            filter(Stations.station == Measures.station).\
            filter(Measures.date >= start_date).\
            filter(Measures.date <= end_date).all()
    else:
        sel = [
           func.avg(Measures.tobs),
           func.max(Measures.tobs),
           func.min(Measures.tobs)
               ]
        calcs = session.query(*sel).\
            filter(Stations.station == Measures.station).\
            filter(Measures.date >= start_date).all()

    return calcs

		
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a><br/>"
        f"<a href='/api/v1.0/stations'>/api/v1.0/stations<br/>"
        f"<a href='/api/v1.0/tobs'>/api/v1.0/tobs</a><br/>"
		f"/api/v1.0/<start><br/>"
		f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """
		Return a json representation of dates 
		and precipitation observations from last year
	"""
    # Query for most recent date in Measures
    recent_date = session.query(Measures.date).order_by('Measures.date desc').first()
    # Get string value of recent date from tuple return by query
    recent_date = recent_date[0]
    # Get string value of 1 year prior to recent date
    prior_date = get_prior_years_date(recent_date,1)
    # Select date and precipitation from Measures for 12 months prior to most recent measurement
    sel = [Measures.date, Measures.prcp]
    results = session.query(*sel).\
            filter(Measures.date >= prior_date).\
            filter(Measures.date <= recent_date).\
            order_by(Measures.date).all()

        # Create a dictionary from the row data
    precip_dict = dict(results)
    return jsonify(precip_dict)

@app.route("/api/v1.0/stations")
def stations():
    """
		Return a json representation of stations list
	"""
    sel = [Measures.station, func.count(Measures.station)]
    station_activity_query = session.query(*sel).group_by(Measures.station). \
        order_by(desc(func.count(Measures.station))).all()
    print('List of stations in descending activity order:')
    stations_list = [i[0] for i in station_activity_query]
    # return a jsonified list of stations
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """
		Return a json representation of tobs list from last year
	"""
    # Query for most recent date in Measures
    recent_date = session.query(Measures.date).order_by('Measures.date desc').first()
    # Get string value of recent date from tuple return by query
    recent_date = recent_date[0]
    # Get string value of 1 year prior to recent date
    prior_date = get_prior_years_date(recent_date, 1)
    # Select date and precipitation from Measures for 12 months prior to most recent measurement
    sel = [Measures.tobs]
    results = session.query(*sel). \
        filter(Measures.date >= prior_date). \
        filter(Measures.date <= recent_date). \
        order_by(Measures.date).all()

    # Create a dictionary from the row data
    tobs_list = [i[0] for i in results]
    return jsonify(tobs_list)

@app.route('/api/v1.0/<start>', methods=['GET'])
def start_only(start):
    end_date = ''
    start_date = datetime.datetime.strptime(start, "%Y-%m-%d").date()
    results = calc_temps(start_date, end_date)
    return jsonify(results[0])

@app.route('/api/v1.0/<start>/<end>', methods=['GET'])
def start_and_end(start, end):
    start_date = datetime.datetime.strptime(start, "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(end, "%Y-%m-%d").date()
    results = calc_temps(start_date, end_date)
    return jsonify(results[0])

if __name__ == '__main__':
    app.run(debug=True)

