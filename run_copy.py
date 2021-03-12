

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#

import sys
import json
import pandas as pd
import configparser

sys.path.insert(0, 'src')
from passengerBusABM import busAgent, NaiveModel
from visualization import visualize_step_model
from timelapse import timelapse_step_model



def main(targets): 

    # config parser 
    parser_busPath = configparser.ConfigParser()
    parser_busPath.read('./config/params.ini')

    ##########################
    abm_config = parser_busPath['ABM_PARAMS']

    abm_config_dict = {}

    abm_config_dict["breath_prob"] = float(abm_config["breath_prob"])
    abm_config_dict["cough_prob"] = float(abm_config["cough_prob"])
    abm_config_dict["sneeze_prob"] = float(abm_config["sneeze_prob"])

    abm_config_dict["breath_dist"] = int(abm_config["breath_dist"])
    abm_config_dict["cough_dist"] = int(abm_config["cough_dist"])
    abm_config_dict["sneeze_dist"] = int(abm_config["sneeze_dist"])

    abm_config_dict["prob_infected"] = float(abm_config["prob_infected"])

    abm_config_dict["num_col_left"] = int(abm_config["num_col_left"])
    abm_config_dict["num_col_mid"] = int(abm_config["num_col_mid"])
    abm_config_dict["num_col_right"] = int(abm_config["num_col_right"])

    abm_config_dict["num_row"] = int(abm_config["num_row"])

    abm_config_dict["dist_bw_seats"] = int(abm_config["dist_bw_seats"])

    abm_config_dict["num_infected"] = int(abm_config["num_infected"])
    ##########################

    ##########################
    model_config = parser_busPath['MODEL_PARAMS']

    model_config_dict = {}

    model_config_dict["breathes_per_min"] = int(model_config["breathes_per_min"])
    model_config_dict["trip_duration"] = int(model_config["trip_duration"])
    model_config_dict["destination"] = model_config["destination"]
    ##########################
    
    ##########################
    visualization_config = parser_busPath['VISUALIZATION_PARAMS']

    visualization_params_dict = {}

    visualization_params_dict["input_source"] = visualization_config["input_source"]
    visualization_params_dict["output_source"] = visualization_config["output_source"]
    ##########################

    # makes the bus-passenger ABM
    if 'abm' in targets: 
        busABM = NaiveModel(busAgent, **abm_config_dict)

    if 'model' in targets: 
        visualize_step_model(busABM, **model_config_dict)

    if 'visualize' in targets:
        timelapse_step_model(**visualization_config_dict)



      
        
if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)
