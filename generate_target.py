import numpy as np
import pandas as pd
import constants

# Load the demographic data
df = pd.read_csv(constants.FEATURES_PATH)

np.random.seed(constants.RANDOM_SEED)

state_multipliers = {
    'AL': 0.9, 'AK': 1.1, 'AZ': 1.0, 'AR': 0.8, 'CA': 1.5, 'CO': 1.2, 'CT': 1.3, 'DE': 1.0, 'FL': 1.1, 'GA': 1.0,
    'HI': 1.4, 'ID': 0.9, 'IL': 1.1, 'IN': 0.9, 'IA': 0.8, 'KS': 0.9, 'KY': 0.8, 'LA': 0.9, 'ME': 0.8, 'MD': 1.2,
    'MA': 1.3, 'MI': 1.0, 'MN': 1.1, 'MS': 0.7, 'MO': 0.9, 'MT': 0.8, 'NE': 0.9, 'NV': 1.0, 'NH': 1.0, 'NJ': 1.4,
    'NM': 0.8, 'NY': 1.5, 'NC': 1.0, 'ND': 0.8, 'OH': 0.9, 'OK': 0.8, 'OR': 1.1, 'PA': 1.0, 'RI': 1.0, 'SC': 0.9,
    'SD': 0.8, 'TN': 0.9, 'TX': 1.2, 'UT': 1.0, 'VT': 0.8, 'VA': 1.1, 'WA': 1.3, 'WV': 0.7, 'WI': 0.9, 'WY': 0.8
}

base_income = {
    'High School': 30000,
    'Bachelors': 50000,
    'Masters': 70000,
    'PhD': 90000
}

occupation_multiplier = {
    'Engineer': 1.2,
    'Doctor': 1.5,
    'Teacher': 0.8,
    'Artist': 0.7,
    'Lawyer': 1.3,
    'Scientist': 1.4,
    'Nurse': 0.9,
    'Mechanic': 0.6,
    'Chef': 0.5,
    'Musician': 0.4
}


def generate_income(education_level, occupation, state):

    income = base_income[education_level] * \
        occupation_multiplier[occupation] * state_multipliers[state]

    # Add some randomness to the income
    income += np.random.normal(loc=10000, scale=5000)

    return income


df['income'] = df.apply(lambda row: generate_income(
    row['education'], row['occupation'], row['state']), axis=1)

df['income'] = df['income'].astype(int)
df = df[['id', 'income']]

# send the first 90% of the data to target_known.csv
df.iloc[:int(0.9 * len(df))].to_csv(constants.TARGET_KNOWN_PATH, index=False)

# send the last 10% of the data to target_unknown.csv
df.iloc[int(0.9 * len(df)):].to_csv(constants.TARGET_UNKNOWN_PATH, index=False)
