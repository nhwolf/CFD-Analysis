# CFD-Analysis
A Python application designed to display Computational Fluid Dynamics (CFD) simulations for a mock aircraft.

## Running the app locally
#### 1 - Clone this repo

#### 2 - *(Recommended)* Create a Python Virtual Environment (venv)
From the terminal in the workspace directory (i.e., "CFD-Analysis") create a new python virtual environment using Python 3.12.
```bash
$ python3.12 -m venv .venv
```
Activate the virtual environment
```bash
$ source .venv/bin/activate
```

#### 3 - Install Required Dependencies
Use the provided requirements.txt file to install project dependencies: `pip install -r requirements.txt`.

#### 4 - Run the Data Pipeline
From the terminal in the workspace directory (i.e., "CFD-Analysis") run `data_pipeline.py`
```bash
$ python src/data_pipeline/data_pipeline.py
```
This reads in data from the source json, creates a SQLite3 database in `src/database/`,
and populates a database table with the data from the source json.
__Note__: The data pipeline on needs to be run once for the initial setup. It is only
necessary to run again if the source data has changed.

#### 5 - Start the Dashboard App
From the terminal in the workspace directory (i.e., "CFD-Analysis") run `dashboard_main.py`
```bash
$ python src/dashboard/dashboard_main.py
```
This reads in data from the source json, creates a SQLite3 database in `src/database/`,
and populates a database table with the data from the source json.

## Setting up a Development Environment
#### 1 - Install Python 3.12
Official website: (https://www.python.org/downloads/release/python-3129/)

#### 2 - Clone this repo

#### 3 - Create a Python Virtual Environment (venv)
From the terminal in the workspace directory (i.e., "CFD-Analysis") create a new python virtual environment using Python 3.12.
```bash
$ python3.12 -m venv .venv
```
Activate the virtual environment
```bash
$ source .venv/bin/activate
```

#### 4 - Install Required Dependencies
Use the provided requirements.txt file to install project dependencies: `pip install -r requirements.txt`.

## Running tests with pytest
The `pytest.ini` configures pytest such that users can run the test files in the `test/` directory from
the root directory of the project.

#### Troubleshooting
If you have multiple python versions on your system, you may encounter errors when running tests
from the virtual environment after initial activation. Deactivating and Reactivating the virual
environment usually fixes this issue.

From the terminal in the workspace directory:
```bash
$ deactivate && source venv/bin/activate
```