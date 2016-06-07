#!/bin/bash
LOC=$( cd $(dirname $0) ; pwd -P )

source $LOC/bin/activate
export FLASK_APP=app.py
flask run --port=8877
