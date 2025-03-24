import constants
import pandas as pd
import random

pins = []
n = 50
for i in range(n):
    pin = ''
    for j in range(8):
        pin += str(random.randint(1, 9))
    pins.append(pin)

team_ids = list(range(1, n+1))

df = pd.DataFrame({'team': team_ids, 'pin': pins})

# don't overwrite the file if it already exists
if not constants.SUBMISSION_PINS_PATH.exists():
    df.to_csv(constants.SUBMISSION_PINS_PATH, index=False)
