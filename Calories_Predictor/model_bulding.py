"""
Description:- This script load the encoded data and train multiple linear regression model to predict the calories burned
              during gym session based on several input features.
Author:- lakkadaditya@gmail.com
Date:- 26th Nov,2024
Version:- 1.0
Changes:- > Version-1
            - initial draft
"""
import pandas as pd
import os
from pathlib import Path
import config
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# path of this script's directory
script_dir = Path(os.path.dirname(os.path.abspath(__file__))).parent


def data_load_and_splitting(test_size=0.2):
    """
    Loads the encoded_data and split them into train and test sets
    Args:
        test_size(float) = user input for size of test data
    Returns:
        train_df, test_df (DataFrame): train and test data arrays
    """
    # load the encoded data
    data_path = os.path.join(script_dir, 'data', 'processed_data', 'encoded_data.csv')
    encoded_df = pd.read_csv(data_path, index_col=None)
    encoded_df.drop(columns=["Unnamed: 0"], inplace=True)

    # data Splitting
    train_df, test_df = train_test_split(encoded_df, test_size=0.2, random_state=config.RANDOM_STATE)

    return train_df, test_df


def save_train_test_data(train_df, test_df):
    """
    Save the train and test data
    Args:
        train_df(DataFrame): training data
        test_df(DataFrame) : tetsing data
    Returns:
        None
    """
    train_save_path = os.path.join(script_dir, 'data', 'train', 'train.csv')
    test_save_path = os.path.join(script_dir, 'data', 'test', 'test.csv')

    train_df.to_csv(train_save_path)
    test_df.to_csv(test_save_path)

    return None


def model_training():
    """
    load the train data and trains the mutiple linear regression model to it
    Args:
        None
    Returns:
        None
    """
    # train data path
    train_data_path = os.path.join(script_dir, 'data', 'train', 'train.csv')
    train_df = pd.read_csv(train_data_path)

    # splitting into features and target
    x = train_df.drop(columns=config.TARGET)
    x.drop(columns=['Unnamed: 0'], inplace=True)
    y = train_df[config.TARGET]

    # defining multiple linear regression model
    mlr = LinearRegression()

    # fitting the data
    mlr.fit(x, y)

    # saving fitted model
    save_path = os.path.join(script_dir, 'data', 'models', config.MODEL_NAME)
    joblib.dump(mlr, save_path)

    return None


if __name__ == "__main__":
    train_df, test_df = data_load_and_splitting(test_size=0.25)
    save_train_test_data(train_df, test_df)
    model_training()

