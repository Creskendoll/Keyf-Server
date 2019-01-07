# Keyf-Server
## Pre-Req
You need a file named *connection_string.txt* where you'll store your mongoDB connection string such as,
"mongodb+srv://{USER}:{PASSWORD}@{CLUSTER}-dwn2y.mongodb.net/".
The application will read this file to access the DB.

## Setup
Packages can be installed using setuptools.
Run ```python setup.py sdist``` in order to install the necessary packages.
The program mainly utilizes [Flask](https://flask-restful.readthedocs.io/en/latest/) where additional information can be found.

To start the server you have to set the flask enironment variable as follows:  
```FLASK_APP=Keyf```  
And optionally development mode where flask watches for changes on the code can be set as:  
```FLASK_ENV=development```  

## Start
After setting the variables the program can be started by running either:  
```flask run```  
Or if that doesn't work:  
```python -m flask run```

## Additional Info
Edit and run *populateDB.py* to test out the program
