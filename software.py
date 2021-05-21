from flask import Flask, render_template
import pandas as pd
import numpy as np
import sys

app = Flask(__name__)

# file_name = name of the csv file as a string
def load_csv( file_name ):
    '''Reads a csv files information and returns it as a pandas dataframe'''
    data_frame = pd.DataFrame()

    try:
        data_frame = pd.read_csv(file_name)
    except:
        print("A file with the name \"" + str(file_name) + "\" does not exist or is not readable")
    
    return data_frame

def sort(dataframe, column):
    '''Sorts the dataframe by column and returns the sorted dataframe'''
    sorted_df = dataframe.sort_values(by=[column])
    return sorted_df

def get_country(dataframe, country):
    '''Returns a list with data about the specified country'''
    lst = dataframe.loc[dataframe['Country_Region'] == country]
    return lst

file='04-21-2021.csv'
tables = list(pd.read_csv( file ).values.tolist())
titles=pd.read_csv( file ).columns.values
# countries = pd.read_csv( file ).rows.values


@app.route( "/" )
def home():
    '''Home page function'''

    return render_template( 'home.html', titles=titles, tables=tables )


# @app.route( "/home" )

if __name__ == '__main__':
    app.run( debug=True ) 