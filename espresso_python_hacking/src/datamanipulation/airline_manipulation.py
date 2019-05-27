import os

import matplotlib.pyplot as plt
from sklearn import preprocessing
import pandas as pd
from data_preprocessing import identify_quant_cols, make_col_positive, log_transform, normalize_data
import seaborn as sns
import sys
from espresso_python_hacking.src.plotting.data_visualisation import make_lineplot


# TODO: Initialise a simple logger and set the desired format to be: TIME LEVEL-module-function-line number-message

def transform_data(data):
    """
    Function to transform data according to some pre-defined steps.

    :param data: data to transform, dataframe format
    :return: transformed data
    """

    # dropping column 'DAY_OF_WEEK' -
    df1 = data.drop('DAY_OF_WEEK', axis=1);

    # print(len(df1.columns), 'and column names are - ', list(df1.columns.values))

    # Rename column 'WHEELS_OFF' to 'HAS_WHEELS'
    df2 = df1.rename(columns={'WHEELS_OFF': 'HAS_WHEELS'})
    # print('Column names are - ', df2.columns.values)

    # print(identify_quant_cols(df2))

    # Fill blanks in column 'AIR_SYSTEM_DELAY' with the average of the values
    # print(df2['AIR_SYSTEM_DELAY'].mean())

    df2['AIR_SYSTEM_DELAY'].fillna(df2['AIR_SYSTEM_DELAY'].mean(), inplace=True)

    # print(df2['AIR_SYSTEM_DELAY'])
    # print('Column names are - ', df2.columns.values)

    # Scale values between 0 and 1 in 'DEPARTURE_DELAY' and put them in 'DEPARTURE_DELAY_NORMALISED'

    df2 = normalize_data(df2,'DEPARTURE_DELAY')
    df2 = normalize_data(df2, 'ARRIVAL_DELAY')
    df2 = normalize_data(df2, 'AIR_SYSTEM_DELAY')
    df2 = normalize_data(df2, 'LATE_AIRCRAFT_DELAY')
    df2 = normalize_data(df2, 'WEATHER_DELAY')


    #x = df2[['DEPARTURE_DELAY']].values.astype(float)
    #min_max_scaler = preprocessing.MinMaxScaler()
    #x_normalized = min_max_scaler.fit_transform(x)
    #df2['DEPARTURE_DELAY_NORMALISED'] = pd.DataFrame(x_normalized)
    #print(df2['ARRIVAL_DELAY_NORMALISED'])
    #print(df2['DEPARTURE_DELAY_NORMALISED'])

    # Make 'ARRIVAL_DELAY' column positive using a function imported from data_preprocessing.py

    # print (df2['ARRIVAL_DELAY'])

    df = make_col_positive(df2, 'ARRIVAL_DELAY')
    # print('post change - ', df5['ARRIVAL_DELAY'])

    #take the log of the column DEPARTURE_DELAY
    # print(df5['AIRLINE'],'column names are ', df5.columns.values)

    df_log = log_transform(df, 'DEPARTURE_DELAY')

    # df2['DEPARTURE_DELAY_NORMALISED'].plot(kind='bar')
    # plt.show(block=True)
    # plt.interactive(False)
    return df


if __name__ == "__main__":
    '''
    HOMEWORK: Write a function that outputs insights into the data. I.e. aggregated data, plots etc. that will
    tell a compelling story to Heathrow about trends that we have discovered in the airline industry.
    
    The output should be the repository that helped produce the insight and a deck (.pdf, no longer that 5 slides)
    which would be used to present the insights to the client. 
    
    Please do not spend more than 3 hours on this.
    '''


    # Import Flight data
    flights_data = pd.read_csv('../../data/flights1.csv', delimiter=",")
    transformed_data = transform_data(flights_data)
    #print(transformed_data.columns.values)

    sns.lmplot('AIRLINE', 'ARRIVAL_DELAY_NORMALISED', data=transformed_data, fit_reg=False)
    sns.lmplot('AIRLINE', 'DEPARTURE_DELAY_NORMALISED', data=transformed_data, fit_reg=False)
    print(transformed_data.groupby(['AIRLINE', 'DIVERTED'])['TAIL_NUMBER'].count())
    print(transformed_data.groupby(['AIRLINE', 'CANCELLED'])['TAIL_NUMBER'].count())

    #filtering EV Airline data - Atlantic Southeast Airlines

    df_EV = transformed_data.loc[transformed_data['AIRLINE'] == 'EV']
    #print(df_EV)
    #make_lineplot(df_EV,'DAY','AIR_SYSTEM_DELAY')
    #sns.lineplot(x="MONTH", y="AIR_SYSTEM_DELAY", data=df_EV)

    #print(transformed_data.groupby(['AIRLINE', 'DEPARTURE_DELAY_NORMALISED'])['TAIL_NUMBER'].count())
    #df_UA = transformed_data.loc[transformed_data['AIRLINE'] == 'UA']
    #print('column name', df_UA.columns.values ,df_UA.AIRLINE_DELAY.unique())
    #plt.hist(df_UA['SECURITY_DELAY'])
    plt.show(block=True)
    plt.interactive(False)


