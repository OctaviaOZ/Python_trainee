from sklearn.linear_model import Lasso
import pickle
import numpy as np
import xgboost as xgb


class Estimator:
    @staticmethod
    def fit(train_x, train_y):
        model = xgb.XGBRegressor(learning_rate=0.01, n_estimators=2048,
                              max_depth=5, min_child_weight=0,
                              gamma=0, subsample=0.7,
                              colsample_bytree=0.7,
                              objective='reg:squarederror', nthread=-1,
                              scale_pos_weight=1, seed=27,
                              reg_alpha=0.00006)

        #model = Lasso(alpha=0.0005, selection='random', max_iter=15000)
        #train_y = np.log1p(train_y)
        result = model.fit(train_x, train_y)
        with open('models/XGB.pickle', 'wb')as f:
            pickle.dump(model, f)
        return result

    @staticmethod
    def predict(trained, test_x):
        return trained.predict(test_x)


