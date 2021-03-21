# Overwatch Performance Tracker

## Table of Contents

1. Data Collection
2. Data Storage and Access

## 1. Data Collection

### Premise

The first part of the project will be Data Collection. Here all data needed to perform analysis will be collected.

The actual match data collection is intended to be done using an api. Currently I am looking into what sets are available, but the hope is to find one directly through Blizzard.

Once the data has been collected I intend to put it directly into some not yet specified DTO. This DTO will then be sent to the Data Storage and Access class for cleaning and insertion into the database.

### Assumptions

This is a very uncertain part of the project so early on, the following is subject to change upon discovery of new information

1. We will be using an api to collect match data
2. Data will be parsed in the Data Storage and Access portion of the project
