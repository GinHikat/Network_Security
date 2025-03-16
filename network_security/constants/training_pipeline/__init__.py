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


#Data Ingestion 
DATA_INGESTION_COLLECTION_NAME: str = "NetworkSecurity"
DATA_INGESTION_DATABASE: str = "PDANH"
DATA_INGESTION_DIR_NAME: str = "Data_Ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = 'feature_store'
DATA_INGESTION_INGESTED_DIR: str = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2