from src.load import load_data
from src.display import plot_top_countries
from src.analyse import total_price_by_country

def main():
    df = load_data("data/MOCK_DATA.csv")
    plot_top_countries(total_price_by_country(df))

if __name__ == "__main__":
    main()