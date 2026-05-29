from pandas_df import df_csv
import pandas as pd

def power_curve(data):
    power_curve = []
    power_curve = data["PowerOriginal"]

    #zeit = [1, 3, 6, 10, 30, 60, 100, 300, 600, 1000, 3000, 6000]
    #i = len(zeit)

    #i = len(power_curve)
    i = 0
    pw = []
    for i in range(i,len(power_curve)):
        for j in range(i + 1,len(power_curve)):
            window = power_curve.iloc[i:j]
            avg_power = window.mean()
            pw.append(avg_power)


    return pw


power_curve(df_csv())
