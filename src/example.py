import logging
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

pd.set_option('display.max_columns', None)
pd.set_option("display.max_rows", None)



def fn_data_analysis(data_df, logger):
    logger.info(f"Dataframe shape: {data_df.shape}")
    logger.info(f"Dataframe columns: {data_df.columns}")
    logger.info(f"Dataframe info: {data_df.info()}")
    logger.info(f"Dataframe describe: {data_df.describe()}")
    logger.info(f"Dataframe head: {data_df.head()}")
    logger.info(f"Dataframe tail: {data_df.tail()}")
    logger.info(f"Dataframe null values: {data_df.isnull().sum()}")
    logger.info(f"Dataframe duplicated values: {data_df.duplicated().sum()}")

    print(data_df.shape)

def fn_fetch_data(logger):
    csv_file_path = '../local_data/titanic.csv'
    data_df = pd.read_csv(csv_file_path)  # Read the data from the CSV file into tabular format
    logger.info(f"Dataframe shape: {data_df.shape}")
    print(data_df.head())
    return data_df

def main():
    print('Project Starting')

    # Create a logger object
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)


    # Create a file handler
    file_handler = logging.FileHandler('../logs/martin_project.log')
    logger.addHandler(file_handler)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)    # Set the formatter for the handler

    ##read in dataset##
    data_df = fn_fetch_data(logger)
    ##Data Analysis / Discovery##
    fn_data_analysis(data_df, logger)

    print('project end')






if __name__ == '__main__':
    main()