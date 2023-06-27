# ETL-HCP-Data-Collector


This directory stores automated scripts meant to build postgres database with one table,
collect data from swiss website with HCPs information by communicating with its API,
clean the data, save it into pandas dataframe and load everything into postgres table. 


## How to use

1. Fill in `config.yaml` with your data.
2. run main.py


## Config explanation

### api_key ###

API KEY for https://www.medregom.admin.ch/api/medreg/public/person/search

### input_data ###

IDs and configuration of the search we want to send in payload

### input_website ###

Link to the website which we will send requests to

### database_credentials ###

Credentials to postgres database we will create

### default_database_credentials ###

Credentials to default postgres database which will allow us to repeat script (drop previously created database)
