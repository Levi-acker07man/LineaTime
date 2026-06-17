import os

# i am using python bult-in os so that i doesnot crash on ohter systems
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#update the file path if neede
DATA_DIR = os.path.join(BASE_DIR, 'data')
DATA_FILE_PATH = os.path.join(DATA_DIR, 'latency_data.csv')