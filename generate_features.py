import pandas as pd
import constants
from constants import N
import numpy as np
import random


np.random.seed(constants.RANDOM_SEED)


# Generate random demographic data
data = {
    'id': range(1, N + 1),
    'age': np.random.randint(18, 90, size=N),
    'gender': np.random.choice(['Male', 'Female'], size=N),
    'income': np.random.randint(20000, 150000, size=N),
    'education': np.random.choice(['High School', 'Bachelors', 'Masters', 'PhD'], size=N),
    'marital_status': np.random.choice(['Single', 'Married', 'Divorced', 'Widowed'], size=N),
    'occupation': np.random.choice(['Engineer', 'Doctor', 'Teacher', 'Artist', 'Lawyer'], size=N),
    'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], size=N),
    'state': np.random.choice(['NY', 'CA', 'IL', 'TX', 'AZ'], size=N),
    'children': np.random.randint(0, 5, size=N),
    'home_owner': np.random.choice([True, False], size=N),
    'car_owner': np.random.choice([True, False], size=N),
    'credit_score': np.random.randint(300, 850, size=N),
    'internet_usage': np.random.randint(0, 24, size=N),
    'exercise_frequency': np.random.randint(0, 7, size=N),
    'smoker': np.random.choice([True, False], size=N),
    'alcohol_consumption': np.random.choice(['None', 'Moderate', 'Heavy'], size=N),
    'diet': np.random.choice(['Vegetarian', 'Non-Vegetarian', 'Vegan'], size=N),
    'pet_owner': np.random.choice([True, False], size=N),
    'travel_frequency': np.random.choice(['Never', 'Rarely', 'Often'], size=N),
    'hobbies': np.random.choice(['Reading', 'Traveling', 'Cooking', 'Sports', 'Music'], size=N)
}

df = pd.DataFrame(data)
df.to_csv(constants.FEATURES_PATH, index=False)
