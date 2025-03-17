import yaml
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
import os, sys
import numpy as np
import dill
import pickle

def read_yaml_file(file_path: str) ->dict:
    try:
        with open(file_path, 'rb') as yml_file:
            return yaml.safe_load(yml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
def write_yaml_file(file_path: str, content: object, replace:bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=  True)
        with open(file_path, 'w') as file:
            yaml.dump(content, file)
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
def save_nparray(file_path: str, array: np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file:
            np.save(file, array)
    except Exception as e:
        raise NetworkSecurityException(e, sys)   
    
def save_object(file_path: str, obj: object) -> None:
    try:
        logging.info('Saving object of mainUtil class')
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
        logging.info('End the saving')
    except Exception as e:
        raise NetworkSecurityException(e, sys)     