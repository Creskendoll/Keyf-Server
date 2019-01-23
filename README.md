# Keyf-Server
## Pre-Req
You need a file named *connection_string.txt* where you'll store your mongoDB connection string such as,
"*mongodb+srv://{USER}:{PASSWORD}@{CLUSTER}-dwn2y.mongodb.net/*".
The application will read this file to access the DB.

Before running you need to [install via pip](https://packaging.python.org/tutorials/installing-packages/) the following packages:
- flask
- flask_pymongo
- flask_restful

## Setup
Packages can be installed using setuptools.
Run ```python setup.py sdist``` in order to install the necessary packages.
The program mainly utilizes [Flask](https://flask-restful.readthedocs.io/en/latest/) where additional information can be found.

Then you have to set the flask enironment variable as follows:  
- ```FLASK_APP=Keyf```    
And optionally development mode where the changes on the code are watched:  
- ```FLASK_ENV=development```    

## Start
Finally the program can be started by running either:  
```flask run```  
Or if that doesn't work:  
```python -m flask run```  
In order to run the server on local lan you can pass the option ```--host=0.0.0.0```  

There might be additional packages required by the project so install them as well. 

## Additional Info
```populateDB.py``` writes the .json files to the DB. Edit those files to save placeholder data to the DB.

## Project Overview
### Entities
The models of the objects in the DB are defined as Entities under the Entities folder. Every model has a serialize function derived from the BaseEntity.
### Services
Service classes derive from [flask_restful Resource](https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html).Classes have methods named as HTTP requests.
### ```__init__``` files 
The root ```__init__.py``` file can be run individually in order to start the flask app. The files inside sub folders are required for packaging purposes so that classes can be directly imported.
### Front End 
Currently the index.html file is served upon a get request to the root domain. 
