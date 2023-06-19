import pandas as pd


def read_csv_ignore_errors(file_path):
    try:
        dataset = pd.read_csv(file_path, sep=';', low_memory=False)
        return dataset
    except pd.errors.ParserError as e:
        print(f"Error during the file lecture: {e}")
        return None
