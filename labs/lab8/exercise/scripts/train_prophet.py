import fbprophet

# print version number
print('Prophet %s' % fbprophet.__version__)

import pandas as pd
import numpy as np
from pandas import read_csv, to_datetime
import pickle

# Exercise, read into a Pandas DataFrame the energy-train S3 file we mounted.
train_path = None  # FILLME
df = read_csv(train_path, header=0)[["Date", "Load"]]
# summarize shape
print(df.shape)
# show first few rows

# prepare expected column names. Prophet expects 2 columns: ds and y as target
df.columns = ['ds', 'y']
df['ds'] = None ## Convert each ds row into datetime
print(df)
# define the model Prophet
model = None # Fillme
# fit the model

# Test a prediction
future = list()
for i in range(0, 55, 5):
    date = f'2020-12-25 23:{i}:00'
    future.append([date])
future = pd.DataFrame(future)
future.columns = ['ds']
future['ds'] = to_datetime(future['ds'])
# use the model to make a forecast
forecast = None # Fillme
forecast['actual'] = df['y']
# Calculate the MSE and print it. This can be Regexed to an actual metric if interested
print(f"loss={np.sum((forecast['yhat'] - forecast['actual']) ** 2)}")

# Eercise: Use pickle to write the forecast dataframe (in case you want to do diagnostics on your notebook) and the model
pkl_path = None  # FILLME
with open(pkl_path, "wb") as f:
    # Pickle the 'Prophet' model using the highest protocol available.
    pass  # FILLME

# save the forecast dataframe
None
print("*** Data Saved ***")
