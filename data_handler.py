import pandas as pd
from logger import log_info, log_error

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        log_info("Data loaded successfully")
        return data
    except Exception as e:
        log_error(f"Error loading data: {e}")
        return None

def process_data(data):
    try:
        summary = data.describe()
        log_info("Data processed successfully")
        return summary
    except Exception as e:
        log_error(f"Error processing data: {e}")
        return None