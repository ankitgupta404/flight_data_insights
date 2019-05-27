import matplotlib as plt
import numpy as np
from scipy.stats import boxcox
from sklearn import preprocessing
import pandas as pd


def identify_quant_cols(data):
    """
        Function to identify quantitative columns.

        :param data: data to transform, dataframe format
        :return: columns object
        """

    quantCols = data._get_numeric_data().columns
    return quantCols


def make_col_positive(data, col_name):
    """
            Function to make particular column of dataframe positive.

            :param data: data to transform, dataframe format
            :param col_name: string, name of the column to be transformed
            :return: columns object
            """
    data[col_name] = data[col_name].abs()
    return data


def log_transform(data, col_name):
    """
               Function to make log tranform entire column of dataframe .

               :param data: data to transform, dataframe format
               :param col_name: string, name of the column to be transformed
               :return: NA
               """
    data1 = data[np.isfinite(data[col_name])]
    data2 = np.log2(data1[col_name])
    return data2

def normalize_data(data,column):
    x = data[[column]].values.astype(float)
    min_max_scaler = preprocessing.MinMaxScaler()
    x_normalized = min_max_scaler.fit_transform(x)
    col_name=column+'_NORMALISED'
    data[col_name] = pd.DataFrame(x_normalized)
    return data

    #print(data2)
    # Add any code here to log transform an entire column.
