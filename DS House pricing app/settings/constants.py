import os

DATA_FOLDER = os.path.dirname(os.path.dirname(__file__))
def get_full_path(*path):
    return os.path.join(DATA_FOLDER, *path)

TRAIN_CSV = get_full_path('data', 'train.csv')
VAL_CSV = get_full_path('data', 'val.csv')

#SAVED_ESTIMATOR = get_full_path('models', 'Lasso.pickle')
SAVED_ESTIMATOR = get_full_path('models', 'XGB.pickle')



