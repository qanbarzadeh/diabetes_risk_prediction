import json
import pandas as pd
import logging
import os

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_path='../config/config.json'):
    """
    Loads configuration from a JSON file.
    
    Args:
        config_path (str): The path to the configuration file.
        
    Returns:
        dict: Configuration settings as a dictionary, or None if loading fails.
    """
    try:
        with open(config_path, 'r') as file:
            config = json.load(file)
            logging.info("Configuration loaded successfully.")
            return config
    except FileNotFoundError:
        logging.error(f"Configuration file not found: {config_path}")
        return None
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from the configuration file: {config_path}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred while loading configuration: {e}")
        return None

def load_data(file_path):
    """
    Loads data from a specified file path into a pandas DataFrame.
    
    Args:
        file_path (str): The path to the data file.
        
    Returns:
        pandas.DataFrame: The loaded data as a DataFrame, or None if loading fails.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Data loaded successfully from {file_path}")
        return data
    except FileNotFoundError:
        logging.error(f"Data file not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        logging.error("The data file is empty.")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred while loading data: {e}")
        return None