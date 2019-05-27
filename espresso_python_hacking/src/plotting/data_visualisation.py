# TODO: WRITE SOME FUNCTION TO VISUALISE THE DATA - BE CREATIVE, WHAT VISUALISATIONS WOULD MAKE SENSE?
# CAN ALSO ASK THE INSTRUCTORS FOR INSPIRATION


import pandas as pd
import matplotlib.pyplot as plt1

import seaborn as sns1


def make_pivot_table(data, index_name, columns, values, afffunc):
    """
               Function to make particular column of dataframe positive.

               :param data: data to transform, dataframe format
               :param col_name: string, name of the column to be transformed
               :return: columns object
               """

    pvt = data.pivot_table(index=[index_name], columns=[columns], values=values, aggfunc=afffunc)
    return pvt


def make_lineplot(data, x, y):
    sns1.lineplot(x, y, data=data)
    plt1.show(block=True)
    plt1.interactive(False)

