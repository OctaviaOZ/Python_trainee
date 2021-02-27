import json
import pandas as pd
import numpy as np
from utils.trainer import Estimator

from utils.dataloader import DataLoader
from settings. constants import TRAIN_CSV


with open('settings/specifications.json') as f:
    specifications = json.load(f)

raw_train = pd.read_csv(TRAIN_CSV)
x_columns = specifications['description']['X']
y_column = specifications['description']['y']

x_raw = raw_train[x_columns]

loader = DataLoader()
loader.fit(x_raw)
X = loader.load_data()
y = raw_train.SalePrice

estimate = Estimator()
estimate.fit(X, y)
