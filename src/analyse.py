import pandas as pd

#returns 10 highest total prices
def total_price_by_country(df):
    return df.groupby("destination_country")["total_price"].sum().sort_values(ascending=False)