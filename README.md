# Overwatch Performance Tracker

## Table of Contents

1. Data Collection
2. Data Storage and Access

## 1. Data Collection

### Premise

The first part of the project will be Data Collection. Here all data needed to perform analysis will be collected.

The match data collection is done using a refactored version of my web scraper from the old OverwatchDSApp project. That project was based off an outdated python webscraper developed by Alex Botello. From what I can tell the component used the requests-html library to import html from the playoverwatch website. From there Alex found a pattern for parsing out hero stat data. All this logic and code can be found at the path DataCollection/web_scraper/deprecated/python-overwatch. 

The refactored web scraper contains 3 major components:
- overwatch_user
- - a class to denote an overwatch player whose data we wish to scrape
- overwatch_statistic_generator
- - a class to collect all statistics for a specific hero for a specific overwatch player
- overwatch_data_collector
- - a class to collect all data for all heroes for a specific overwatch player

Once the data has been collected I intend to put it directly into a json string. This json data will then be sent to the Data Storage and Access class for cleaning and insertion into the database.

## 2. Data Storage and Access

The next portion of the project is Data Storage and Access. In this section we go over everything related to how the data will be stored and accessed.

First and foremost the data will be stored in a MySql database. This decision was made with the idea that it will work nicely with Java for database insertion and with C# for data retrieval. In addition to that hosting the server will be significantly easier than with MS SQL Server.
