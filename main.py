import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_csv("data/MOCK_DATA.csv")

preis_pro_land = (
    df.groupby("destination_country")["total_price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
preis_pro_land.plot(kind="barh")

plt.title("Top 10 Länder nach Gesamtpreis")
plt.ylabel("Zielland")
plt.xlabel("Gesamtpreis (€)")
plt.yticks(rotation=45)

# y-Achse formatieren
plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

plt.tight_layout()
plt.show()