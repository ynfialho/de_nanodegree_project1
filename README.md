# Project 1: Data Modeling with Postgres

This project aims to create a database that enables dimensional analysis of music played on a music streaming platform. This platform belongs to a fictional starup, Sparkify, whose data comes from log files and datasets of songs.

To provide this analytical data a dimensional modeling was created in a PostgreSQL database. This modeling will be powered by an ETL process written in Python 3.6 that can be run on demand or on a scheduled basis.

With this database we can obtain answers to several questions, among them:
* Visions on the volumetry of songs listened to in different temporalities
* Frequency of use of the platform by state
* Most Popular Artists and Songs

## How to Use

1. Run create_tables.py from terminal.
2. Run etl.py from terminal.

## Test

An interactive test of the ETL process load can be done through the notebook Jupyter test.ipynb