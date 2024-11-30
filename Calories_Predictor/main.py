"""
Description:- Main script that takes all the data processing , model building and model evaluation task and generate predictions
Author:- lakkadaditya@gmail.com
Date:- 26th Nov,2024
Version:- 1.0
Changes:- > Version-1
            - initial draft
"""

from data_preprocessing import load_dataset, renaming_cols, data_encoding
from model_bulding import data_load_and_splitting, save_train_test_data, model_training
from model_evalution import evaluation_metrics, get_predictions
import pandas as pd

# loading the dataset
raw_df = load_dataset()
# renaming the column names
renamed_data = renaming_cols(raw_df)
# encoding categorical columns
encoded_data = data_encoding(renamed_data)
# loading processed data and splitting
train_df, test_df = data_load_and_splitting(test_size=0.25)
# saving test and train data
save_train_test_data(train_df, test_df)
# model training
model_training()
# getting model evaluation metrics
mse, mae, r2 = evaluation_metrics()
print('Mean Squared error is:', mse)
print('Mean Absolute error is:', mae)
print('R2 score is:', r2)
# getting prediction on sample data
data = {'Age': 34, 'Weight': 71.9, 'Height': 1.64, 'Max_BPM': 170, 'Avg_BPM': 134, 'Resting_BPM': 67,
        'Session_Duration': 1.26,
        'Fat_Percentage': 21.3, 'Water_Intake': 2.1, 'Workout_Frequency': 4, 'Experience_Level': 2, 'BMI': 26.73,
        'Gender_Female': 0, 'Gender_Male': 1, 'Workout_Type_Cardio': 1, 'Workout_Type_HIIT': 0,
        'Workout_Type_Strength': 0, 'Workout_Type_Yoga': 0}
prediction = get_predictions(pd.DataFrame([data]))
print('Prediction is: ', prediction)




