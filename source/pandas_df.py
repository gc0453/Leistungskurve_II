import pandas as pd
import numpy as np

def read_csv_pd():
    directory = "data/" #Speicherort
    file_name_csv = "activity.csv" #Dateiname der csv-Datei
    df = pd.read_csv(directory + file_name_csv, sep=',',header=0) #Datenframe erstellen
    return df #Die "gereinigten" Daten werden zurückgegeben

def clean_pd(data):
    pd_clean = data.dropna(subset=["PowerOriginal"]) #Alle None aus PowerOriginal entfernen
    return pd_clean
