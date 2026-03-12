def dataset_overview(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isnull().sum().to_dict()
    }

#returns total prices from highest to lowest 
def total_price_by_country(df):
    return df.groupby("destination_country")["total_price"].sum().sort_values(ascending=False)

#returns total volume from highest to lowest
def total_volume_by_country(df):
    return df.groupby("destination_country")["volume"].sum().sort_values(ascending=False)

#return amount of deliveries by country
def total_deliveries_by_country(df):
    return df.groupby("destination_country").size().sort_values(ascending=False)

def average_price_per_delivery(df):
    return df["total_price"].mean()

def top_expensive_deliveries(df, n=10):
    return df.sort_values("total_price", ascending=False).head(n)

def add_price_per_volume(df):
    df = df.copy()
    df["price_per_volume"] = df["total_price"] / df["volume"]
    return df

def average_price_by_country(df):
    return df.groupby("destination_country")["total_price"].mean().sort_values(ascending=False)

