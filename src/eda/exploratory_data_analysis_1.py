# Import library
from pprint import pprint

import pandas as pd  # Data Manipulation
import numpy as np  # Data Manipulation
import matplotlib.pyplot as plt  # Data Visualization
import seaborn as sns
import json
# https://appdividend.com/2022/03/15/pandas-to_json/


def set_up_plot_configuration():
    """

    :return:
    """
    plt.rcParams['figure.figsize'] = [8, 5]
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.style.use('seaborn-whitegrid')
    sns.set_style('darkgrid')
    sns.set(font_scale=1.3)


class ExploratoryDataAnalysis:
    """
    Performs Data Exploration
    """

    def __init__(self):
        """
        Initialization
        """
        self.path = "C:\\Arunangsu\\AI\\Data\\"
        self.file_name = None
        self.df_insurance = None
        self.data_types = None

    def fetch_dataset(self, file_name):
        """
        Fetch the dataset to be explored
        :param file_name:
        :return:
        """
        self.file_name = file_name
        try:
            self.df_insurance = pd.read_csv(self.path + self.file_name)
        except FileNotFoundError as fe:
            print(fe)
        finally:
            print('Fetch Dataset Operation Completed')

        return self.df_insurance

    def perform_eda(self, dataset):
        """
        Perform Exploratory Data Analysis
        :return:
        """
        # self.file_name = dataset
        # df_insurance_exploration = self.fetch_dataset(dataset)
        self.df_insurance = self.fetch_dataset(dataset)

        if self.df_insurance is not None:
            try:
                print(f'Number of rows and columns in the dataset:{self.df_insurance.shape}')
                # Let's look into top few rows and columns in the dataset
                print(f'First Few Rows of the dataset:\n{self.df_insurance.head()}')
                print(f'Dataset Info:\n{self.df_insurance.info()}')
                print(f'Dataset Description:\n{self.df_insurance.describe()}')
                # pprint(f'First Few Rows of the dataset:\n{self.df_insurance.head().to_json(orient="columns")}')
                # pprint(f'First Few Rows of the dataset:\n{self.df_insurance.head().to_json(orient="index")}')
                # pprint(f'{self.df_insurance.head().to_json(orient="records")}')
                # pprint(f'{self.df_insurance.head().to_json(orient="table")}')
                print(f'The data types of the feature:\n{self.df_insurance.dtypes}')
            except FileNotFoundError as fe:
                print(fe)
            finally:
                print('Fetch Dataset Operation Completed')
        else:
            print('Dataset does not exist')

    def get_dtypes_as_json(self, dataset):
        """

        :return:
        """
        self.df_insurance = self.fetch_dataset(dataset)
        if self.df_insurance is not None:
            try:
                print(f'The data types of the feature:\n{self.df_insurance.dtypes}')

                # Create dType dictionary
                res = self.df_insurance.dtypes.to_frame('dtypes').reset_index()
                print(f'Dtypes:\n{res}')
                res1 = self.df_insurance.dtypes.to_json
                print(f'Dtypes as JSON:\n{res1}')
                # First Create dictionary
                dict_dtypes = res.set_index('index')['dtypes'].astype(str).to_dict()
                print(f'Dtypes as JSON:\n{dict_dtypes}')
                with open('types.json', 'w') as f:
                    json.dump(dict_dtypes, f)

                with open('types.json', 'r') as f:
                    self.data_types = json.load(f)

                print(f'DTypes from the json file:\n{self.data_types}')

            except FileNotFoundError as fe:
                print(fe)
            finally:
                print('Fetch Dataset Operation Completed')
        else:
            print('Dataset does not exist')


if __name__ == '__main__':
    eda = ExploratoryDataAnalysis()
    # eda.fetch_dataset('insurance.csv')
    eda.perform_eda('insurance.csv')
    # eda.get_dtypes_as_json('insurance.csv')
    print("foo'bar")
    print(r'foo\\bar\nbaz')
