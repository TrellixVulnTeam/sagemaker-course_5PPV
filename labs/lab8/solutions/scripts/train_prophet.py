import fbprophet
# print version number
print('Prophet %s' % fbprophet.__version__)

import pandas as pd
import numpy as np
from pandas import read_csv, to_datetime

# load data
train_path = '/opt/ml/processing/input/energy-train.csv'
df = read_csv(train_path, header=0)[["Date", "Load"]]
# summarize shape
print(df.shape)
# show first few rows

# prepare expected column names
df.columns = ['ds', 'y']
df['ds'] = to_datetime(df['ds'])
print(df)
# define the model
model = fbprophet.Prophet()
# fit the model
model.fit(df)

# define the period for which we want a prediction
future = list()
for i in range(0, 55, 5):
    date = f'2020-12-25 23:{i}:00'
    future.append([date])
future = pd.DataFrame(future)
future.columns = ['ds']
future['ds'] = to_datetime(future['ds'])
# use the model to make a forecast
forecast = model.predict(future)
forecast['actual'] = df['y']
# summarize the forecast
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper', 'actual']])
print(f"loss={np.sum((forecast['yhat'] - forecast['actual'])**2)}")
# plot forecast

import pickle

pkl_path = "/opt/ml/processing/output/model/Prophet.pkl"
with open(pkl_path, "wb") as f:
    # Pickle the 'Prophet' model using the highest protocol available.
    pickle.dump(model, f)

# save the dataframe
forecast.to_pickle("/opt/ml/processing/output/forecast/forecast.pkl")
print("*** Data Saved ***")
