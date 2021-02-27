import json
import requests
import pandas as pd
from sklearn.metrics import r2_score
import numpy as np

from utils.trainer import Estimator
from utils.dataloader import  DataLoader
from settings.constants import TRAIN_CSV, VAL_CSV

def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

with open('settings/specifications.json') as f:
    specifications = json.load(f)

info = specifications['description']
x_columns, y_column, metrics = info['X'], info['y'], info['metrics']

train_set = pd.read_csv(TRAIN_CSV, header=0)
val_set = pd.read_csv(VAL_CSV, header=0)

train_x, train_y = train_set[x_columns], train_set[y_column]
val_x, val_y = val_set[x_columns], val_set[y_column]

loader = DataLoader()
loader.fit(val_x)
val_processed = loader.load_data()
print('data: ', val_processed[:10])

req_data = {'data': json.dumps(val_x.to_dict())}
response = requests.get('http://127.0.0.1:8000/predict', data=req_data)
api_predict = response.json()['prediction']
print('predict: ', api_predict[:10])

api_score = r2_score(val_y, api_predict)
print('r2_score: ', api_score)

mape = mean_absolute_percentage_error(val_y, api_predict)
print('mape: ', mape)