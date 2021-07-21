# 1. import Flask
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
from markupsafe import escape
from flask import Flask, jsonify
from flask import g as flask_global

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Routes
@app.route("/")
def home():
    return (
        f"Welcome to the Home Page!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/{escape('<start>')}<br/>"
        f"/api/v1.0/{escape('<start>/<end>')}<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    results = flask_global.session.query(Measurement.date, Measurement.prcp).all()
    return_dict = dict()

    for date, prcp in results:
        return_dict[date] = prcp

    return jsonify(return_dict)


@app.route("/api/v1.0/stations")
def stations():
    results = flask_global.session.query(Station.name).all()
    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


@app.route("/api/v1.0/tobs")
def tobs():
    results = flask_global.session.query(Measurement.tobs).filter(
        Measurement.station == "USC00519281", Measurement.date > "2016-08-18"
    )
    result_data = [row[0] for row in results]
    return jsonify(result_data)


@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def startdate(start, end=None):

    if end is None:
        nl = "<br/>"
        mint = calc_temps2(start)[0][0]
        avg = round(calc_temps2(start)[0][1], 1)
        maxt = calc_temps2(start)[0][2]
        return f" Start Date: {start} {nl}{nl}TMin: {mint} {nl} TAvg: {avg} {nl} TMax: {maxt}"
    else:
        nl = "<br/>"
        mint = calc_temps(start, end)[0][0]
        avg = round(calc_temps(start, end)[0][1], 1)
        maxt = calc_temps(start, end)[0][2]

        return f" Start Date: {start} {nl}End Date: {end} {nl}{nl}TMin: {mint} {nl} TAvg: {avg} {nl} TMax: {maxt}"


def calc_temps(start_date, end_date):
    return (
        flask_global.session.query(
            func.min(Measurement.tobs),
            func.avg(Measurement.tobs),
            func.max(Measurement.tobs),
        )
        .filter(Measurement.date >= start_date)
        .filter(Measurement.date <= end_date)
        .all()
    )


def calc_temps2(start_date):
    return (
        flask_global.session.query(
            func.min(Measurement.tobs),
            func.avg(Measurement.tobs),
            func.max(Measurement.tobs),
        )
        .filter(Measurement.date >= start_date)
        .all()
    )


@app.before_request
def opensession():
    flask_global.session = Session(engine)


@app.after_request
def closesession(response):
    flask_global.session.close()
    return response


if __name__ == "__main__":
    app.run(debug=True)
