# Keyf-Server
## Dependencies
Make sure you have [Python3]([https://link](https://www.python.org/downloads/)) and [pip](https://pypi.org/) installed.

## Pre-Req
If doesn't exist create a file named *connection_string.txt* in the root folder where you'll store your mongoDB connection string in the following form:

- *mongodb+srv://{USER}:{PASSWORD}@keyfcluster-dwn2y.mongodb.net/keyf?retryWrites=true*

Where {USER} and {PASSWORD} are your credentials.
The application will read this file to access the DB.

Before running you need to [install packages via pip](https://packaging.python.org/tutorials/installing-packages/). Run the following command in the root folder:
- `pip install -r requirements.txt`

This will install all the necessary modules.

## Setup
The program mainly utilizes [Flask](https://flask-restful.readthedocs.io/en/latest/) where additional information can be found.

Then you have to set the flask environment variable as follows:
- ```FLASK_APP=Keyf```  
And optionally development mode where the changes on the code are watched:
- ```FLASK_ENV=development```

## Start
The program can be started by running:  
- `python main.py`  

There might be additional packages required by the project so install them as well. 

## Additional Info
```populateDB.py``` writes the .json files to the DB. Edit those files to save placeholder data to the DB.


## Project Overview
### Entities
The models of the objects in the DB are defined as Entities under the Entities folder. Every model has a serialize function derived from the BaseEntity.
### Services
Service classes derive from [flask_restful Resource](https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html).Classes have methods named as HTTP requests.
### `__init__` files 
The `__init__.py` files inside sub folders are required for packaging purposes so that classes can be directly imported.
### Front End
Files relevant to front end can be found inside `public/site`. 
Currently the index.html file is served upon a get request to the root domain.

# Testing
## Basics
All the tests should be placed under the `tests/` folder and be named as `test_foo.py`. Pytest will automatically look for those files and run them. You can run all the tests by running:
- `pytest -v`

If that doesn't work, you can try:
- `python -m pytest -v`

To display system out, append `s` to the argument; `pytest -vs`. 