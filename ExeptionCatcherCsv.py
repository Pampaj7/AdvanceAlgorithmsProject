import pandas as pd


def read_csv_ignore_errors(file_path):
    try:
        dataset = pd.read_csv(file_path, sep=';')
        return dataset
    except pd.errors.ParserError as e:
        print(f"Errore durante la lettura del file: {e}")
        return None
