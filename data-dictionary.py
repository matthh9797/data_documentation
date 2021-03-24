# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 06:06:17 2021

@author: MattH
"""

import pandas as pd

# helper function
def count_blanks(columns):
    count = 0
    for column in columns:
        if not column:
            count += 1
    return count

# read dataset
data = pd.read_csv('INSERT PATH TO DATASET')

data_documentation = pd.DataFrame(index=data.columns, columns=['Description', 'Type', 'Missing Values', 'Blanks'])
for name in data.columns:
    data_documentation.loc[name, 'Type'] = data[name].dtypes
    data_documentation.loc[name, 'Missing Values'] = data[name].isna().sum()
    data_documentation.loc[name, 'Blanks'] = count_blanks(data[name])
      
# (Optional) Manual Change to data types
data_string = ['INSERT LIST OF DATA TYPE STRING']
data_bools = ['INSERT LIST OF DATA TYPE BOOLS']
data_dates = ['INSERT LIST OF DATA TYPE DATES']
date_numbers = ['INSERT LIST OF DATA TYPE NUMBERS']

# Insert data types to table
data_documentation.loc[data_string, 'type'] = 'string'
data_documentation.loc[data_bools, 'type'] = 'boolean'
data_documentation.loc[data_dates, 'type'] = 'date'
data_documentation.loc[date_numbers, 'type'] = 'number'

# sort values by type
data_documentation.sort_values(by='type')

# take a look at the data documentation
data_documentation

# Save the data documentation as a csv
data_documentation.to_csv('data_documentation.csv')






