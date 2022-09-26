# Airline Ticket Sales App :airplane:

## Team 

- Cristian Jesus Quispe Quispe
- Sharon Rossely Chullunquia Rosas
- Sheyla Acosta

## 1. Create virtual environment

* We create the virtual environment for our project.

  On Linux:

  ``` 
  python -m venv venv
  ````

  On Windows:

  ``` 
  py -m venv venv
  ````
  
* We activate our virtual environment.

  On Linux:

  ```bash
  source venv/bin/activate
  ````

  On Windows:

  ```bash
  source venv/Scripts/activate
  ````

## 2. Install mypy

* We install _mypy_ using _pip_.

  ```bash
  pip install mypy
  ````

* To run _mypy_, we execute the following command.

  ```bash
  mypy app.py --check-untyped-defs --ignore-missing-imports
  ````

## 3. Run
  
  ```bash
  python app.py
  ````
