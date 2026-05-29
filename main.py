from source.power_curve import power_curve_pd
from source.power_curve import power_curve_np
from source.pandas_df import df_csv
import numpy as np
import pandas as pd

data = df_csv()
if isinstance(data, np.ndarray):
    power_curve_np(data)

elif isinstance(data, pd.DataFrame):
    power_curve_pd(data)

else:
    print("Daten konnten nicht verarbeitet werden")
