# data paths
FILE_NAME = 'gym_members_exercise_tracking.csv'

# column renaming dictionary
RENAME_DICT = {'Weight (kg)': 'Weight', 'Height (m)': 'Height', 'Session_Duration (hours)': 'Session_Duration',
               'Water_Intake (liters)': 'Water_Intake', 'Workout_Frequency (days/week)': 'Workout_Frequency'}

# columns list for encoding
COLS_TOBE_ENCODED = ['Gender', 'Workout_Type']

# Target colum
TARGET = ['Calories_Burned']

# Random state
RANDOM_STATE = 42

# Model name
MODEL_NAME = 'regression_model.pkl'
