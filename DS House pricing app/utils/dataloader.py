import numpy as np # linear algebra
from sklearn.preprocessing import LabelEncoder


class DataLoader(object):
    def fit(self, dataset):
        self.dataset = dataset.copy()

    def load_data(self):
        #self.dataset['MSSubClass'] = self.dataset['MSSubClass'].apply(str)
        #self.dataset['YrSold'] = self.dataset['YrSold'].astype(str)
        #self.dataset['MoSold'] = self.dataset['MoSold'].astype(str)
        #self.dataset['YearRemodAdd'] = self.dataset['YearRemodAdd'].astype(str)

        quantitative = ['LotFrontage', 'MasVnrArea']
        qualitative = ['MasVnrType', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
                        'Electrical', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond']

        # Fill missing values for quantitative variables
        for i in quantitative:
            self.dataset.fillna(self.dataset.median(), inplace=True)

        # Fill missing values for special variables
        spec_categ_col = ['PoolArea', 'Fence', 'Alley', 'FireplaceQu']
        for i in spec_categ_col:
            self.dataset[i].fillna('None', inplace=True)

        # Fill missing values for categorical variables
        for i in qualitative:
            self.dataset[i].fillna(self.dataset[i].mode()[0], inplace=True)

        # Feature Engineering
        # Total Floor area of entire house
        #self.dataset['TotalSF'] = self.dataset['TotalBsmtSF'] + self.dataset['1stFlrSF'] + \
        #                          self.dataset['2ndFlrSF']
        # Total number of baths
        self.dataset['TotalBath'] = (self.dataset['FullBath'] + (0.5 * self.dataset['HalfBath']) + \
                                     self.dataset['BsmtFullBath'] + (0.5 * self.dataset['BsmtHalfBath']))
        # Total porch area
        self.dataset['TotalPorchSF'] = self.dataset['OpenPorchSF'] + self.dataset['3SsnPorch'] + \
                                       self.dataset['EnclosedPorch'] + self.dataset['ScreenPorch'] + \
                                       self.dataset['WoodDeckSF']

        #feature columns with correlation greater than 0.8
        to_drop = ['Id', 'PoolQC', 'MiscFeature']#,'WoodDeckSF'
        self.dataset.drop(to_drop, axis=1, inplace=True)

        #quantitative = [f for f in raw_train.columns if raw_train.dtypes[f] != 'object']
        #qualitative = [f for f in raw_train.columns if raw_train.dtypes[f] == 'object']

        qualitative = ['MSZoning',
         'Street',
         'Alley',
         'LotShape',
         'LandContour',
         'Utilities',
         'LotConfig',
         'LandSlope',
         'Neighborhood',
         'Condition1',
         'Condition2',
         'BldgType',
         'HouseStyle',
         'RoofStyle',
         'RoofMatl',
         'Exterior1st',
         'Exterior2nd',
         'MasVnrType',
         'ExterQual',
         'ExterCond',
         'Foundation',
         'BsmtQual',
         'BsmtCond',
         'BsmtExposure',
         'BsmtFinType1',
         'BsmtFinType2',
         'Heating',
         'HeatingQC',
         'CentralAir',
         'Electrical',
         'KitchenQual',
         'Functional',
         'FireplaceQu',
         'GarageType',
         'GarageFinish',
         'GarageQual',
         'GarageCond',
         'PavedDrive',
         'Fence',
         'SaleType',
         'SaleCondition']

        # encode labels
        le = LabelEncoder()

        for feature in qualitative:
            le.fit(self.dataset[feature])
            self.dataset[feature] = le.transform(self.dataset[feature])

        #scaler = MinMaxScaler()
        #scaler.fit(self.dataset[quantitative])

        #x = scaler.transform(self.dataset[quantitative])

        #for feature in quantitative:
        #    self.dataset[feature] = (self.dataset[feature] + 1).transform(np.log)

        #x = np.log1p(self.dataset[quantitative])

        #self.dataset[quantitative] = x

        #print(self.dataset.columns.to_list())

        return self.dataset


