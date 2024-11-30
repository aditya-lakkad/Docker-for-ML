"""
Description:- evalutes linear regression model on below parameters.
                1. mean squred error.
                2. mean absolute error
                3. r2 score
Author:- lakkadaditya@gmail.com
Date:- 26th Nov,2024
Version:- 1.0
Changes:- > Version-1
            - initial draft
"""
import os
from pathlib import Path
import config
import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# path of this script's directory
script_dir = Path(os.path.dirname(os.path.abspath(__file__))).parent


def evaluation_metrics():
    """
    Calculates and displayes mean suqred error, mean absolute error and r2 square

    Args:
        None
    Returns:
        mse,mae,re(float)
    """
    model_path = os.path.join(script_dir, 'data', 'models', config.MODEL_NAME)
    model = joblib.load(model_path)

    test_data_path = os.path.join(script_dir, 'data', 'test', 'test.csv')
    test_df = pd.read_csv(test_data_path)

    x = test_df.drop(columns=config.TARGET)
    x.drop(columns=['Unnamed: 0'], inplace=True)
    y = test_df[config.TARGET]

    y_pred = model.predict(x)
    mse = mean_squared_error(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    return mse, mae, r2


def get_predictions(data):
    """
    takes user input and predict the output
    Args:
        data(dictionary): input data dictionary
    Returns:
        prediction(ndarray)
    """

    model_path = os.path.join(script_dir, 'data', 'models', config.MODEL_NAME)
    model = joblib.load(model_path)
    pred = model.predict(data)

    return pred


if __name__ == "__main__":
    mse, mae, r2 = evaluation_metrics()
    print('Mean Squared error is:', mse)
    print('Mean Absolute error is:', mae)
    print('R2 score is:', r2)
    # data = [[48, 83.9, 1.82, 176, 149, 70, 1.9, 13.1, 3.5, 5, 3, 25.33, 0, 1, 0, 1, 0, 0]]
    data = {'Age':34,'Weight':71.9,'Height':1.64,'Max_BPM':170,'Avg_BPM':134,'Resting_BPM':67,'Session_Duration':1.26,
            'Fat_Percentage':21.3,'Water_Intake':2.1,'Workout_Frequency':4,'Experience_Level':2,'BMI':26.73,
            'Gender_Female':0,'Gender_Male':1,'Workout_Type_Cardio':1,'Workout_Type_HIIT':0,
            'Workout_Type_Strength':0,'Workout_Type_Yoga':0}
    prediction = get_predictions(pd.DataFrame([data]))
    print('Prediction is: ', prediction)


