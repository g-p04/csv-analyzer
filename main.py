from src.load import load_data
from src.display import *
from src.analyse import *

def main():
    df = load_data("data/MOCK_DATA.csv")

    plot_top_countries_by_deliveries(total_deliveries_by_country(df))
    plot_top_countries(total_price_by_country(df))
    plot_top_countries(top_expensive_deliveries(df))
    plot_price_distribution(df)
    plot_volume_distribution(df)
    plot_price_vs_volume(df)
    plot_average_price_by_country(average_price_by_country(df))

if __name__ == "__main__":
    main()