import os
import sys
import json
import pandas as pd
import numpy as np
import pymongo
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop = True, inplace = True)
            record = list(json.loads(data.T.to_json()).values())
            return record
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def mongo_db_push(self, record, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.record = record
            
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.record)
            return (len(self.record))
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == '__main__':
    FILE_PATH = 'network_data/phisingData.csv'
    DATABASE = 'PDANH'
    Collection = "NetworkSecurity"
    network = NetworkDataExtract()
    record = network.csv_to_json(file_path=FILE_PATH)
    no_of_records = network.mongo_db_push(record, DATABASE, Collection)
    print(no_of_records)