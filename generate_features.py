import pandas as pd
import constants
from constants import N
import numpy as np


np.random.seed(constants.RANDOM_SEED)

df = pd.DataFrame({
    'id': range(1, N + 1),
})

# Pareto distribution scaled to adult ages
df['age'] = np.random.randint(18, 99, size=N)
df['age'] = df['age'].astype(int)


# education
education_distribution = {
    'High School': 0.30,
    'Bachelors': 0.35,
    'Masters': 0.20,
    'PhD': 0.15
}

education_levels = list(education_distribution.keys())
education_probs = list(education_distribution.values())
df['education'] = np.random.choice(education_levels, size=N, p=education_probs)

# occupation
occupation_distribution = {
    'Engineer': 0.20,
    'Doctor': 0.10,
    'Teacher': 0.15,
    'Artist': 0.10,
    'Lawyer': 0.15,
    'Scientist': 0.05,
    'Nurse': 0.10,
    'Mechanic': 0.05,
    'Chef': 0.05,
    'Musician': 0.05
}

occupation_levels = list(occupation_distribution.keys())
occupation_probs = list(occupation_distribution.values())
df['occupation'] = np.random.choice(
    occupation_levels, size=N, p=occupation_probs)

# state
state_distribution = {
    'AL': 5197720, 'AK': 743756, 'AZ': 7691740, 'AR': 3107240, 'CA': 39663800, 'CO': 6013650, 'CT': 3707120, 'DE': 1067410, 'FL': 23839600, 'GA': 11297300,
    'HI': 1450900, 'ID': 2032120, 'IL': 12778100, 'IN': 6968420, 'IA': 3264560, 'KS': 2989710, 'KY': 4626150, 'LA': 4607410, 'ME': 1410380, 'MD': 6309380,
    'MA': 7205770, 'MI': 10197600, 'MN': 5833250, 'MS': 2942920, 'MO': 6282890, 'MT': 1143160, 'NE': 2023070, 'NV': 3320570, 'NH': 1415860, 'NJ': 9622060,
    'NM': 2139350, 'NY': 19997100, 'NC': 11210900, 'ND': 804089, 'OH': 11942600, 'OK': 4126900, 'OR': 4291090, 'PA': 13139800, 'RI': 1121190, 'SC': 5569830,
    'SD': 931033, 'TN': 7307200, 'TX': 31853800, 'UT': 3564000, 'VT': 648278, 'VA': 8887700, 'WA': 8059040, 'WV': 1769460, 'WI': 5991540, 'WY': 590169
}
total = sum(state_distribution.values())
state_distribution = {k: v / total for k, v in state_distribution.items()}

state_levels = list(state_distribution.keys())
state_probs = list(state_distribution.values())
df['state'] = np.random.choice(state_levels, size=N, p=state_probs)


# marital status
marital_status_options = ['Single', 'Married', 'Divorced', 'Widowed']


def generate_marital_status(age):
    if age < 25:
        return np.random.choice(marital_status_options, p=[0.85, 0.13, 0.015, 0.005])
    elif 25 <= age < 35:
        return np.random.choice(marital_status_options, p=[0.6, 0.3, 0.08, 0.02])
    elif 35 <= age < 50:
        return np.random.choice(marital_status_options, p=[0.3, 0.5, 0.15, 0.05])
    else:
        return np.random.choice(marital_status_options, p=[0.1, 0.6, 0.2, 0.1])


df['marital_status'] = df['age'].apply(generate_marital_status)

# home owner
home_owner_options = [True, False]


def generate_home_owner(age, marital_status):
    if age < 25:
        return np.random.choice(home_owner_options, p=[0.1, 0.9])
    elif 25 <= age < 35:
        if marital_status == 'Married':
            return np.random.choice(home_owner_options, p=[0.5, 0.5])
        else:
            return np.random.choice(home_owner_options, p=[0.3, 0.7])
    elif 35 <= age < 50:
        if marital_status == 'Married':
            return np.random.choice(home_owner_options, p=[0.7, 0.3])
        else:
            return np.random.choice(home_owner_options, p=[0.5, 0.5])
    else:
        return np.random.choice(home_owner_options, p=[0.8, 0.2])


df['home_owner'] = df.apply(lambda row: generate_home_owner(
    row['age'], row['marital_status']), axis=1)


df['pet_owner'] = np.random.choice([True, False], size=N)
df['travel_frequency'] = np.random.choice(
    ['Never', 'Rarely', 'Often'], size=N)


df.to_csv(constants.FEATURES_PATH, index=False)
