import pandas as pd

def power_curve_pd(data):
    power_curve = []
    power_curve = data["PowerOriginal"]

    zeit = [1, 2, 3, 4, 6, 10, 15, 30, 45, 60, 120, 180, 300, 360, 600, 900, 1080, 1260, 1440, 1620, 1800]

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

    result_table = pd.DataFrame({
        "Zeit_s": zeit,
        "Leistung_W": power_result
    })

    return result_table
