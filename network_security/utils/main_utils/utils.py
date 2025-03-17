import yaml
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
import os, sys
import numpy as np
import dill
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

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
    
def load_object(file_path: str, ) ->object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f'File {file_path} not exist')
        with open(file_path, 'rb') as file:
            print(file)
            return pickle.load(file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)  
    
def load_np(file_path: str) -> np.array:
    try:
        with open(file_path, 'rb') as file:
            return np.load(file)
    except Exception as e:
        raise NetworkSecurityException(e, sys) 
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise NetworkSecurityException(e, sys)