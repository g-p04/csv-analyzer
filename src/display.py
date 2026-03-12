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

def plot_top_countries_by_deliveries(series, top_n=10):
    top = series.head(top_n)

    top.plot(kind="bar")
    plt.title("Top 10 Länder nach Anzahl der Lieferungen")
    plt.xlabel("Land")
    plt.ylabel("Anzahl Lieferungen")
    plt.tight_layout()
    plt.show()

def plot_price_distribution(df):
    plt.hist(df["total_price"], bins=30)
    plt.title("Verteilung der Preise")
    plt.xlabel("Preis")
    plt.ylabel("Anzahl Lieferungen")
    plt.tight_layout()
    plt.show()

def plot_volume_distribution(df):
    plt.hist(df["volume"], bins=30)
    plt.title("Verteilung der Volumen")
    plt.xlabel("Volumen")
    plt.ylabel("Anzahl Lieferungen")
    plt.tight_layout()
    plt.show()

def plot_price_vs_volume(df):
    plt.scatter(df["volume"], df["total_price"])
    plt.title("Preis im Vergleich zum Volumen")
    plt.xlabel("Volumen")
    plt.ylabel("Preis")
    plt.tight_layout()
    plt.show()

def plot_average_price_by_country(series, top_n=10):
    top = series.head(top_n)

    top.plot(kind="bar")
    plt.title("Top 10 Länder nach durchschnittlichem Preis")
    plt.xlabel("Land")
    plt.ylabel("Durchschnittspreis")
    plt.tight_layout()
    plt.show()
    