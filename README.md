# Overwatch Performance Tracker

## Table of Contents

1. Data Collection
2. Data Storage and Access

## 1. Data Collection

The first part of the project will be Data Collection. Here all data needed to perform analysis will be collected.

### Web Scraper

The match data collection is done using a refactored version of my web scraper from the old OverwatchDSApp project. The project itself is done in Python3 and is based off an outdated webscraper developed by Alex Botello. From what I can tell the component used the requests-html library to import html from the playoverwatch website. From there Alex found a pattern for parsing out hero stat data. All this logic and code can be found at the path DataCollection/web_scraper/deprecated/python-overwatch.

The refactored web scraper is still Python3 based and contains 3 major components:
- overwatch_user
- - a class to denote an overwatch player whose data we wish to scrape
- overwatch_statistic_generator
- - a class to collect all statistics for a specific hero for a specific overwatch player
- overwatch_data_collector
- - a class to collect all data for all heroes for a specific overwatch player

Once the data has been collected it is put directly into a json string. This json data will then be sent to the Data Storage and Access class for cleaning and insertion into the database.

## 2. Data Storage and Access

The next portion of the project is Data Storage and Access. Everything related to how the data will be stored and accessed can be found in this section.

### Data Cleaning

The cleaning and insertion of data into the database will be done using Java.

In order to obtain the match data we must be able to call the web scraper from the Java application and pipe data in. My research for calling python scripts in Java led me to a few different potential solutions. The easiest one seemed to be using the Jython 3rd party library, as it contained a specific function for executing scripts, in addition to not requiring a local install of python. The other solution would be to use Java's built in ProcessBuilder API for creating and running external processes. While this method appeared to require more coding and documentation research, it required no additional download or setup. Due to those setup benifits and Jython only being able to run Python2, this application uses the ProcessBuilder approach.

### Data Storage and Database Schema

The database will be a MySQL database.
