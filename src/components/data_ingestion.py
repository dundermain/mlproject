import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

from src.components.data_transformation import DataTransformation

@dataclass
class DataIngestionConfig:  #it is better to use @dataclass if you are only defining a variable, if you are planning to use any new function inside class better use dunder methods
    train_data_path:str = os.path.join('artifacts', "train.csv")
    test_data_path:str = os.path.join('artifacts', "test.csv")
    raw_data_path:str = os.path.join('artifacts', "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            df = pd.read_csv('/home/sachin/Music/MLproject/mlproject/notebook/data/stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)            #this line takes the data from stud.csv and saves it in data.csv
            logging.info("Train test split initiated")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=69)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)   #this line takes the data from raw data i.e data.csv and saves it in train.csv
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)     #this line takes the data from raw data i.e data.csv and saves it in test.csv

            logging.info("Ingestion of data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
        



if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    data_transformation.initialize_data_transformation(train_data, test_data)
    print(train_data, test_data)

