# CFD-Analysis
A Python application designed to display Computational Fluid Dynamics (CFD) simulations for a mock aircraft.

## Setting up a Development Environment
### 1 - Install Python 3.12
Official website: (https://www.python.org/downloads/release/python-3129/)

### 2 - Clone this repo

### 3 - Create a Python Virtual Environment (venv)
From the terminal in the workspace directory (i.e., "CFD-Analysis") create a new python virtual environment using Python 3.12.
```bash
$ python3.12 -m venv .venv
```
Activate the virtual environment
```bash
$ source .venv/bin/activate
```

### 4 - Install Required Dependencies
Use the provided requirements.txt file to install project dependencies: `pip install -r requirements.txt`.

## Running tests with pytest
The `pytest.ini` configures pytest such that users can run the test files in the `test/` directory from
the root directory of the project.

### Troubleshooting
If you have multiple python versions on your system, you may encounter errors when running tests
from the virtual environment after initial activation. Deactivating and Reactivating the virual
environment usually fixes this issue.

From the terminal in the workspace directory:
```bash
$ deactivate && source venv/bin/activate
```