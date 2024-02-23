# PV3 - SonnJA pvlib model
## (Adaptation of the existing model)

Exisitng Model: 
[PV3 PvLib Python](https://github.com/htw-pv3/pvlib-python-pv3)


<a href="https://github.com/htw-pv3"><img align="right" width="100" height="100" src="https://avatars.githubusercontent.com/u/64144501?s=200&v=4" alt="PV3"></a>


## Research object

The test object is the PV system SonnJA!, which was planned by students of the HTW Berlin and the organization einleuchtend e.V..
It was planned in between 2010 and 2013 and is placed on about 620 $m^2$ of the roof area of the building G of the Wilheminenhof campus. 
The produced electricity of this 16 kWp power plant is fed into one phase of the university internal grid of HTW Berlin and remunerated according to the EEG. 
The special quality of this PV system is its conception as a research system: the system has three different module technologies, two types of inverters and a comprehensive monitoring system with its own weather station. 

## Installation

### Setup environment

Create a virtual environment (with venv)
- `python3 -m venv env`

Activate the environment
- Linux and Mac: `source env/bin/activate`
- Windows: `env/Scripts/activate.bat`

Install the required modules
- `pip install requirements.txt`


### How to start and execute the pvlib

- Update your repository (In your git bash: `git pull`)
- Open PyCharm and open the project
- Customize the configuration if necessary (`config.py`)
- Run the main script (`main.py`)
