# TwitterMiningBack
 Backend for test of twitter data mining using Python

# Aplication
 The main idea is to study and use python in a regular application, with a project structure made for a back end API for mining data from Twitter

# Requires
- Python
- MYQSL

# Packages
- mysql-connector-python
- mysqlclient
- flask
- connexion

# How to Install
 Run the script.sql file from the root folder to create the MYQSL databse, install the packages.

# How to Use
 Run the script from the _init_.py to create the API, calls should be adressed to the route "/search" with the 'term' parameter on the request body, this 'term' will be used to search the twitts, the response is the ID of the search.

# How it works !
 The aplication takes the term given by the request and mines twitter data to see what people are talking about it! The project packages are:
 - Data: Connection with the database, aswell as requests
 - Reader: Does the request and returns only the valid content 
 - Filter: Loop through the data, filtering to get only text and structure it.
 - Runner: Main file, called by the API, manages the operations betwen packages.

# Possible changes
 If you want, you can change the Runner.py script to return all the data instead of the ID.