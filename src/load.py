import pandas as pd

def load_data(path):
    df = pd.read_csv("data/MOCK_DATA.csv")
    return df