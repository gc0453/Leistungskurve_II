from pandas_df import df_csv
import pandas as pd

def power_curve(data):
    power_curve = []
    power_curve = data["PowerOriginal"]

    zeit = [1, 3, 6, 10, 30, 60, 100, 300, 600, 1000, 3000, 6000]
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
        power_result.append(max_power)



    return print(power_result)


power_curve(df_csv())
