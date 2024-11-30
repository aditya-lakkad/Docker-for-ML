import numpy as np
import pytest
import pandas as pd
import sys
import os
from pathlib import Path

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from model_evalution import get_predictions

@pytest.fixture
def test_case1():
    return {'Age': 34, 'Weight': 71.9, 'Height': 1.64, 'Max_BPM': 170, 'Avg_BPM': 134, 'Resting_BPM': 67,
            'Session_Duration': 1.26, 'Fat_Percentage': 21.3, 'Water_Intake': 2.1, 'Workout_Frequency': 4,
            'Experience_Level': 2, 'BMI': 26.73, 'Gender_Female': 0, 'Gender_Male': 1,
            'Workout_Type_Cardio': 1, 'Workout_Type_HIIT': 0, 'Workout_Type_Strength': 0, 'Workout_Type_Yoga': 0}


def test_calories_burned(test_case1):
    y_pred1 = get_predictions(pd.DataFrame([test_case1]))

    assert int(y_pred1) == int(913.29290198)

