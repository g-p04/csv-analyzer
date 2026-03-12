from src.load import load_data
from src.display import *
from src.analyse import *

def main():
    df = load_data("data/MOCK_DATA.csv")
    overview = dataset_overview(df)
    print("Zeilen:", overview["rows"])
    print("Spalten:", overview["columns"])
    print("Fehlende Werte:", overview["missing_values"])

if __name__ == "__main__":
    main()