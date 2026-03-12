from matplotlib import pyplot as plt
from matplotlib import ticker
import pandas as pd

def plot_top_countries(series, top_n=10):
    top = series.head(top_n)

    top.plot(kind="barh")
    plt.title("Top 10 Länder nach Gesamtpreis")
    plt.ylabel("Zielland")
    plt.xlabel("Gesamtpreis (€)")
    plt.yticks(rotation=45)

    # y-Achse formatieren
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

    plt.tight_layout()
    plt.show()