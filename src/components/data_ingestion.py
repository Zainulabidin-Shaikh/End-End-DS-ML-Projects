# ========================== IMPORTING STANDARD LIBRARIES ==========================

import os
'''
✅ os: This module provides a way to interact with the operating system.
You can create folders, list files, delete files, work with file paths, etc.
'''

import sys
'''
✅ sys: Gives access to system-specific parameters and functions.
Used here for detailed error handling (like traceback info with sys.exc_info()).
'''
from src.exception import CustomException
'''
✅ CustomException: A user-defined exception class from src/exception.py.
It gives detailed error info like file name, line number, and the actual error message.
'''

from src.logger import logging
'''
✅ logging: A custom logging module from src/logger.py.
Used instead of print() to track program execution and debug more effectively.
'''
import pandas as pd

from sklearn.model_selection import train_test_split

from dataclasses import dataclass
'''
✅ dataclass: A Python decorator that automatically creates init (constructor), 
repr, and other methods for classes. Perfect for configuration and parameter storage.
'''

# ========================== PIPELINE COMPONENTS ==========================

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
'''
✅ These two handle the data preprocessing step — 
null removal, encoding, scaling, and converting data to arrays.
'''

# from src.components.model_trainer import ModelTrainerConfig
# from src.components.model_trainer import ModelTrainer
'''
✅ These handle the final step — training the machine learning model
and evaluating its performance.
'''

# ========================== STEP 1: DATA CONFIGURATION ==========================

@dataclass
class DataIngestionConfig:
    '''
    ✅ A configuration class that stores file paths:
    - train_data_path: where to save the training data
    - test_data_path: where to save the testing data
    - raw_data_path: where to save the raw/original data
    '''

    train_data_path: str = os.path.join('artifacts', "train.csv")
    '''
    os.path.join(): Joins folder and file name to make a full file path.
    Example: 'artifacts/train.csv' — ensures it's OS-independent (works on Windows/Linux/Mac).
    '''

    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

# ========================== STEP 2: DATA INGESTION CLASS ==========================

class DataIngestion:
    def __init__(self):
        '''
        ✅ Constructor method. When you create an object of this class,
        it creates a DataIngestionConfig object and stores it in self.ingestion_config.
        '''
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        '''
        ✅ Main method to perform:
        - Reading the CSV file
        - Creating folders
        - Splitting the data
        - Saving train/test datasets
        - Logging each step
        '''
        logging.info("Entered the data ingestion method or component")

        try:
            df = pd.read_csv('notebook\data\stud.csv')
            '''
            ✅ pd.read_csv(): Reads a CSV file into a pandas DataFrame.
            - 'notebook\\data\\stud.csv' is the relative path to the data.
            - df will hold the full dataset in a table format.
            '''

            logging.info('Read the dataset as dataframe')

            # 🔽 CREATE THE ARTIFACT FOLDER
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            '''
            ✅ os.path.dirname(path):
            - Takes a full file path and returns only the folder path.
            - Example: os.path.dirname('artifacts/train.csv') ➜ 'artifacts'

            ✅ os.makedirs(path):
            - Creates the folder (and parent folders if needed).
            - If the folder already exists, it throws an error — so we use:

            ✅ exist_ok=True:
            - Tells Python to NOT throw an error if the folder already exists.
            '''

            # 🔽 SAVE THE RAW DATA TO A CSV FILE FOR BACKUP
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            '''
            ✅ df.to_csv(): Saves a DataFrame to a CSV file.
            - raw_data_path ➜ 'artifacts/data.csv'
            - index=False ➜ Don't write row numbers
            - header=True ➜ Include column names
            '''

            logging.info("Train test split initiated")

            # 🔽 SPLIT THE DATASET INTO TRAINING AND TESTING
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            '''
            ✅ train_test_split():
            - Randomly splits data into training and testing sets.
            - test_size=0.2 ➜ 20% test data, 80% training data
            - random_state=42 ➜ Ensures same split every time (reproducibility)
            '''

            # 🔽 SAVE TRAINING DATA TO A FILE
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            # 🔽 SAVE TESTING DATA TO A FILE
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            '''
            ✅ Return the paths of train.csv and test.csv
            So other components (like transformation and model trainer) can use them.
            '''

        except Exception as e:
            '''
            ✅ If any error happens during ingestion,
            catch it and raise a custom exception with full traceback details.
            '''
            raise CustomException(e, sys)

# ========================== STEP 3–5: MAIN EXECUTION BLOCK ==========================

if __name__ == "__main__":
    '''
    ✅ This ensures the below code only runs when this file is executed directly.
    It won’t run if this file is imported elsewhere.
    '''

    # 🔽 STEP 3: Run Data Ingestion
    obj = DataIngestion()  # Create an instance of the DataIngestion class
    # obj.initiate_data_ingestion()
    train_data, test_data = obj.initiate_data_ingestion()  # Start ingestion, get file paths

    # 🔽 STEP 4: Data Transformation
    data_transformation = DataTransformation()  # Create instance of transformation class
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)
    '''
    ✅ This step processes the train and test data:
    - Handles missing values, encoding, feature scaling
    - Converts data into NumPy arrays suitable for ML models
    - Returns: train_arr, test_arr, and preprocessing object (if needed)
    '''

    # 🔽 STEP 5: Model Training
    # modeltrainer = ModelTrainer()  # Create instance of model trainer class
    # print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
    '''
    ✅ Trains the machine learning model on the processed train array
    ✅ Tests it on the test array
    ✅ Prints the model score (e.g., R², accuracy)
    '''