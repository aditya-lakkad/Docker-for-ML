"""
Description:- This script load the data from in raw format, changes the column names,encode the data and finally split
              it into train and test set
Author:- lakkadaditya@gmail.com
Date:- 25th Nov,2024
Version:- 1.0
Changes:- > Version-1
            - initial draft
"""
import os
from pathlib import Path
import pandas as pd
import config

# path of this script
script_dir = Path(os.path.dirname(os.path.abspath(__file__))).parent

def load_dataset(file_name=config.FILE_NAME):
    """
    Load the dataset from specific path
    Args:
        file_name(str): name of the raw data file
    Returns:
        df(pd.DataFrame): returns raw data into pandas dataframe
    """
    data_path = os.path.join(script_dir, 'data', 'raw', file_name)
    df = pd.read_csv(data_path, index_col=None)
    return df


def renaming_cols(df):
    """
    Rename the column names for better accessibility and further processing
    Args:
        df(pd.DataFrame): input raw data frame
    Returns:
        df(pd.DataFrame): dataframe with new column
    """
    df = df.rename(columns=config.RENAME_DICT)
    return df


def data_encoding(df):
    """
    OneHOt encoding of the 'Gender' and 'Workout_Type' columns, the save processed data
    Args:
        df(pd.DataFrame): input raw data frame
    Returns:
        None
    """
    df = pd.get_dummies(df, columns=config.COLS_TOBE_ENCODED)
    save_path = os.path.join(script_dir, 'data', 'processed_data', 'encoded_data.csv')
    df.to_csv(save_path)
    return None


if __name__ == "__main__":
    data = load_dataset()
    renamed_data = renaming_cols(data)
    encoded_data = data_encoding(renamed_data)
