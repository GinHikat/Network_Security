import sys
import os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from network_security.constants.training_pipeline import TARGET_COLUMN, DATA_TRANSFORMATION_IMPUTER_PARAMS

from network_security.entity.artifact_entity import DataTransformationArtifact, DataValidationArtifact
from network_security.entity.config_entity import DataTransformationConfig
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.utils.main_utils.utils import save_nparray, save_object

class DataTransformation:
    def __init__(self, data_validation_artifact: DataValidationArtifact,
                 data_transformation_config: DataTransformationConfig):
        try:
            self.data_validation_artifact:DataValidationArtifact = data_validation_artifact
            self.data_transformation_config: DataTransformationConfig = data_transformation_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def get_data_transformer(cls) ->Pipeline:
        '''
        Return Pipeline object with KNNImputer as the first step
        '''
        logging.info("Enter Transformation part")
        
        try:
            imputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            logging.info(f"Initialized KNNImputer with {DATA_TRANSFORMATION_IMPUTER_PARAMS}")
            processor:Pipeline = Pipeline([("Imputer", imputer)])
            
            return processor
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    
    def init_data_transform(self) -> DataTransformationArtifact:
        logging.info("Enter data transformation")
        try:
            logging.info('Starting transformation')
            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)
        
            #Training Dataframe
            input_feature_train_df = train_df.drop(columns = [TARGET_COLUMN], axis = 1)
            target_feature_train = train_df[TARGET_COLUMN]
            target_feature_train = target_feature_train.replace(-1, 0)
            
            #Testing Dataframe
            input_feature_test_df = test_df.drop(columns = [TARGET_COLUMN], axis = 1)
            target_feature_test = test_df[TARGET_COLUMN]
            target_feature_test = target_feature_test.replace(-1, 0)
            
            prep = self.get_data_transformer()
            
            prep = prep.fit(input_feature_train_df)
            transformed_train = prep.transform(input_feature_train_df)
            transformed_test = prep.transform(input_feature_test_df)
            
            train = np.c_[transformed_train, np.array(target_feature_train)]
            test = np.c_[transformed_test, np.array(target_feature_test)]
            
            #Save data
            save_nparray(self.data_transformation_config.transformed_train_file_path, array=train)
            save_nparray(self.data_transformation_config.transformed_test_file_path, array=test)
            save_object(self.data_transformation_config.transformed_object_file_path, prep)
            
            #Prepare artifacts
            data_transformation_artifact = DataTransformationArtifact(
                transformed_object_file_path= self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
            )
            return data_transformation_artifact
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)