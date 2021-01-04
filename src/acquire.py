import numpy as np
import pandas as pd


################################ Data Prep Functions #########################################
def pct_nulls_per_column(df):
    '''
    This function accepts a pandas dataframe.
    Returns the percentage of values missing in each column.
    
    Parameters
    ----------
    df : pandas.core.DataFrame
        Any pandas dataframe.
        
    Returns
    -------
    None
        Displays a table of each column name with the percent of nulls in that column.
    '''
    # Total the null values in each column
    nulls = df.isnull().sum()
    
    # Store the length of the dataframe: Number of rows
    data_length = df.shape[0]

    # Divide the number of missing values by the length of the dataframe
    pct_missing = (nulls/data_length).sort_values(ascending=False)
    
    # Apply formatting for presentation.
    pct_missing_chart = pct_missing.apply("{0:.2%}".format)

    # Display the results.
    print('Percentage of values missing per column')
    print('-' * 39)
    print(f"{pct_missing_chart}")
