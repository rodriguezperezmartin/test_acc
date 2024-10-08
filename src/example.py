import logging
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option("display.max_rows", None)



def fn_data_analysis(data_df, data_crew, logger):
    logger.info(f"Dataframe shape: {data_df.shape, data_crew}")
    logger.info(f"Dataframe columns: {data_df.columns, data_crew}")
    logger.info(f"Dataframe info: {data_df.info(), data_crew.info()}")
    logger.info(f"Dataframe describe: {data_df.describe(), data_crew.describe()}")
    logger.info(f"Dataframe head: {data_df.head(), data_crew.head}")
    logger.info(f"Dataframe tail: {data_df.tail(), data_crew.tail()}")
    logger.info(f"Dataframe null values: {data_df.isnull().sum(), data_crew.isnull().sum()}")
    logger.info(f"Dataframe duplicated values: {data_df.duplicated().sum(), data_crew.duplicated().sum()}")

    print(data_df.shape)
    print(data_crew.shape)


def fn_fetch_data(logger):
    csv_file_path = '../local_data/titanic.csv'
    data_df = pd.read_csv(csv_file_path)  # Read the data from the CSV file into tabular format
    logger.info(f"Dataframe shape: {data_df.shape}")
    print(data_df.head()) #prints the first 5 records. .tail shows the bottom 5.
    return data_df

def fn_fetch_data_crew(logger):
    csv_file_path_crew = '../local_data/titanic_crew.csv'
    data_crew = pd.read_csv(csv_file_path_crew)
    logger.info(f"Dataframe shape: {data_crew.shape}")
    print(data_crew.head())
    return data_crew



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
    data_crew = fn_fetch_data_crew(logger)

    ##Data Analysis / Discovery##
    fn_data_analysis(data_df, data_crew, logger)
    print('project end')






if __name__ == '__main__':
    main()