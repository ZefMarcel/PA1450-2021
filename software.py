from flask import Flask
import pandas as pd
import sys

app = Flask(__name__)

@app.route("/")
def home():
    '''Home page function'''
    return "HTML goes here"


# file_name = name of the csv file as a string
def load_csv(file_name):
    '''Reads a csv files information and returns it as a pandas dataframe'''
    data_frame = pd.DataFrame()

    try:
        data_frame = pd.read_csv(file_name)
    except:
        print("A file with the name \"" + str(file_name) + "\" does not exist or is not readable")
    
    return data_frame

def quick_sort(data, lowest, highest, column):
    """The sorting algorithm (is called from sort function)"""

    if lowest < highest:
        index = lowest - 1
        pivot = data[column].iloc[highest]
        for i in range(lowest, highest):
            if data[column][i] <= pivot:
                index += 1

                a, b = data.iloc[index], data.iloc[i]

                temp = data.iloc[index].copy()

                data.iloc[index] = b
                data.iloc[i] = temp

        data.iloc[index + 1], data.iloc[highest] = data.iloc[highest], data.iloc[index + 1]

        quick_sort(data, lowest, index, column)
        quick_sort(data, index + 1, highest, column)

# data = csv file as a pandas dataframe
# column = what to sort by (example: Deaths)
def sort(data, column):
    """Calls for the sorting algorithm and returns the sorted data as a pandas dataframe when it is done"""
    lowest, highest = get_values(data.FIPS)
    if len(data) < 2:
        return data

    quick_sort(data, lowest, highest, column)
    return data

def get_values(data):
    """Picks the last and first indexes from the data"""
    return 0, len(data) - 1

if __name__ == "__main__":
    app.run()