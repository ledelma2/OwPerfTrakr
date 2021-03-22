# Overwatch Performance Tracker

## Table of Contents

1. Data Collection
2. Data Storage and Access

## 1. Data Collection

### Premise

The first part of the project will be Data Collection. Here all data needed to perform analysis will be collected.

The actual match data collection is intended to be done using a refactored version of my scraper from the old OverwatchDSApp project. To be completely honest I don't remember how it 100% works anymore, but I do know it uses some weird api from the 1000th page of google and a beautiful soup 4 web scraper. From there it puts everything into a collection, but I currently need to look further into what that collection makeup is. Regardless, this should suffice for the initial collection portion of the project.

Once the data has been collected I intend to put it directly into some not yet specified DTO. This DTO will then be sent to the Data Storage and Access class for cleaning and insertion into the database.

### Assumptions

This is a very uncertain part of the project so early on, the following is subject to change upon discovery of new information

1. Data will be parsed in the Data Storage and Access portion of the project


## 2. Data Storage and Access

The next portion of the project is Data Storage and Access. In this section we go over everything related to how the data will be stored and accessed.

First and foremost the data will be stored in a MySql database. This decision was made with the idea that it will work nicely with Java for database insertion and with C# for data retrieval. In addition to that hosting the server will be significantly easier than with MS SQL Server.
