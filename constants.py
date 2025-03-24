from pathlib import Path

N = 5_000_000  # 5 million
RANDOM_SEED = 42

REPO_DIR = Path(__file__).parent
DATA_DIR = REPO_DIR / 'data'

FEATURES_PATH = DATA_DIR / 'features.csv'
TARGET_KNOWN_PATH = DATA_DIR / 'target_known.csv'
TARGET_UNKNOWN_PATH = DATA_DIR / 'target_unknown.csv'
SUBMISSION_PINS_PATH = DATA_DIR / 'submission_pins.csv'
