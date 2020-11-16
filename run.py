

<<<<<<< HEAD
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#

import sys
import json
import pandas as pd

sys.path.insert(0, 'src')
from passengerBusABM import busAgent, NaiveModel
from visualization import visualize_step_model
# from timelapse import timelapse_step_model



def main(targets): 

    abm_config = json.load(open('config/abm_params.json'))
    model_config = json.load(open('config/model_params.json'))
    # visualization_config = json.load(open('config/visualization_params.json'))


    # makes the bus-passenger ABM
    if 'abm' in targets: 
        busABM = NaiveModel(busAgent, **abm_config)

    if 'model' in targets: 
        visualize_step_model(busABM, **model_config)


      
        
if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)
=======
#STUB CODE
import numpy as np
import random
from matplotlib import pyplot, colors
from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector
from numpy.random import choice

# mesa imports
from mesa_geo import GeoAgent, GeoSpace
from mesa.time import BaseScheduler
from mesa import datacollection
from mesa import Model

# shapely imports
from shapely.geometry import Polygon, Point, LineString
import shapely

# data analysis imports
import geopandas as gpd
import pandas as pd
import numpy as np

# plotting imports
import matplotlib as plt

from PIL import Image
import glob
import os

import re



# EXAMPLE: say we have a bus with 3 columns on the left, 1 column in between, 2 columns to the right, and 15 rows.
# the distance between the seats is 3 feet, and we're setting 2 people to be initially infected.
nmodel = NaiveModel(busAgent, [3,1,2,15],3,2)
specific_step_model(nmodel, 0)


# EXAMPLE: say we have a bus with 2 columns on the left, 2 column in between, 2 columns to the right, and 10 rows.
# the distance between the seats is 1 foot, and we're setting 5 people to be initially infected. 
nmodel = NaiveModel(busAgent, [2,2,2,10],1,5)
specific_step_model(nmodel, 0)


# EXAMPLE: say we have a bus with 3 columns on the left, 1 column in between, 2 columns to the right, and 15 rows.
# the distance between the seats is 3 feet, and we're setting 2 people to be initially infected. 

# we are then going to run a model for 5 'action moments'
nmodel = NaiveModel(busAgent, [3,1,2,15],3,2)
visualize_step_model(nmodel, 5)


# EXAMPLE: say we have a bus with 3 columns on the left, 1 column in between, 2 columns to the right, and 15 rows.
# the distance between the seats is 3 feet, and we're setting 2 people to be initially infected. 

# we are then going to run a model for 5 'action moments'
nmodel = NaiveModel(busAgent, [3,1,2,15],3,2)
timelapse_step_model(nmodel, 5)
>>>>>>> 651e7492c240bc6540dfe0e10c99def8d49736f1
