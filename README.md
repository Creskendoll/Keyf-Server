# Keyf-Server
## Pre-Req
You need a file named *connection_string.txt* where you'll store your mongoDB connection string such as,
"mongodb+srv://{USER}:{PASSWORD}@{CLUSTER}-dwn2y.mongodb.net/".
The application will read this file to access the DB.

## How to run
Packages can be installed using setuptools.
Run ```python setup.py sdist``` in order to install the necessary packages.
The program mainly utilizes [Flask](https://flask-restful.readthedocs.io/en/latest/) where additional information can be found.

## Additional Info
Edit and run *populateDB.py* to test out the program
