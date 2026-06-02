from source.power_curve import power_curve_pd
#from source.power_curve import power_curve_np
from source.pandas_df import read_csv_pd, clean_pd
from source.make_plot import plot_line_power
import numpy as np
import pandas as pd

data = read_csv_pd()
data_clean = clean_pd(data)
plot_data = power_curve_pd(data_clean)
plot_line_power(plot_data)
