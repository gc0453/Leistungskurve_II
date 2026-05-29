from source.pandas_df import df_csv
import pandas as pd
import numpy as np

def power_curve_pd(data):
    power_curve = []
    power_curve = data["PowerOriginal"]

    zeit = [1, 2, 3, 4, 6, 10, 15, 30, 45, 60, 75, 90, 120, 180, 240, 300, 360, 720, 900, 1080, 1260, 1440, 1620, 1800]
    #i = len(zeit)
    print(data["PowerOriginal"].dtype)

    #i = len(power_curve)
    i = 0
    power_result = []
    for dauer in zeit:
        max_power = 0
        for i in range(len(power_curve) - dauer + 1):
            window = power_curve.iloc[i:i + dauer]
            avg_power = window.mean()

            if avg_power > max_power:
                max_power = avg_power
        power_result.append(float(max_power))



    return print(power_result)

def power_curve_np(data):
    power_curve = []
    power_curve = data["PowerOriginal"]

    zeit = [1, 2, 3, 4, 6, 10, 15, 30, 45, 60, 75, 90, 120, 180, 240, 300, 360, 720, 900, 1080, 1260, 1440, 1620, 1800]
    #i = len(zeit)
    print(data["PowerOriginal"].dtype)

    #i = len(power_curve)
    i = 0
    power_result = []
    for dauer in zeit:
        max_power = 0
        for i in range(len(power_curve) - dauer + 1):
            window = power_curve.iloc[i:i + dauer]
            avg_power = window.mean()

            if avg_power > max_power:
                max_power = avg_power
        power_result.append(float(max_power))



    return print(power_result)

