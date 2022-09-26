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

## 2. Install requirements

* We install requirements using requirements.txt file.

  ```bash
  pip install -r requirements.txt
  ````

## 3. Run

* To run the application.

  ```bash
  python app.py
  ````
* To run _mypy_.

  ```bash
  mypy app.py --check-untyped-defs --ignore-missing-imports
  ````
