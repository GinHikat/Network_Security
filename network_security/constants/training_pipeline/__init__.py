import os
import sys
import numpy as np
import pandas as pd

#Define constant variable
TARGET_COLUMN = 'Result'
PIPELINE_NAME:str = 'NetworkSecurity'
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = 'phishingData.csv'

TRAIN_FILE_NAME: str = 'train.csv'
TEST_FILE_NAME: str = 'test.csv'

SCHEMA_FILE_PATH = os.path.join('data_schema', 'schema.yml')

#Data Ingestion 
DATA_INGESTION_COLLECTION_NAME: str = "NetworkSecurity"
DATA_INGESTION_DATABASE: str = "PDANH"
DATA_INGESTION_DIR_NAME: str = "Data_Ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = 'feature_store'
DATA_INGESTION_INGESTED_DIR: str = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

#Data Validation
DATA_VALIDATION_DIR_NAME: str = 'data_validation'
DATA_VALIDATION_VALID_DIR: str = 'validated'
DATA_VALIDATION_INVALID_DIR: str = 'invalid'
DATA_VALIDATION_DRIFT_REPORT_DIR: str = 'drift_report'
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = 'report.yml'
PREPROCESSING_OBJECT_FILE_NAME:str = "preprocessing.pkl"


#Data Transformation
DATA_TRANSFORMATION_DIR_NAME: str = 'data_transformation'
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = 'transformed'
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = 'transformed_object'

##KNN Imputer to replace nan
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    'n_neighbors': 3,
    'weights': 'uniform'
}