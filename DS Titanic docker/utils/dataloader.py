import pandas as pd
import re
from sklearn.preprocessing import LabelEncoder


class DataLoader(object):
    def fit(self, dataset):
        self.dataset = dataset.copy()

    # apply regex
    def get_title(self, name):
        pattern = ' ([A-Za-z]+)\.'
        title_search = re.search(pattern, name)
        # If the title exists, extract and return it.
        if title_search:
            return title_search.group(1)
        return ""

    def ticket_split(self, s):

        s = s.strip()
        split = s.split()

        if len(split) == 1:
            tnum = split[0]
            # there are 4 strange ticket numbers
            # that state 'LINE'. Assign them to 0
            if tnum == 'LINE':
                tnum = 0
            tstr = 'NA'

        elif len(split) == 2:
            tstr = split[0]
            tnum = split[1]
        else:
            tstr = split[0] + split[1]
            tnum = split[2]

        tnum = int(tnum)

        return tstr, tnum

    def load_data(self):
        # columns combination
        self.dataset['FamilySize'] = self.dataset['SibSp'] + self.dataset['Parch'] + 1

        # Filling the missing value in Fare with the median Fare of 3rd class alone passenger
        med_fare = self.dataset.groupby(['Pclass', 'Parch', 'SibSp']).Fare.median()[3][0][0]
        self.dataset['Fare'] = self.dataset['Fare'].fillna(med_fare)

        # binning with qcut
        self.dataset['CategoricalFare'] = pd.qcut(self.dataset['Fare'], 7)

        # apply regex
        self.dataset['Title'] = self.dataset['Name'].apply(self.get_title)

        # replace
        self.dataset['Title'] = self.dataset['Title'].replace(['Lady', 'Countess', 'Capt', 'Col', \
                                               'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
        self.dataset['Title'] = self.dataset['Title'].replace(['Mlle', 'Ms'], 'Miss')
        self.dataset['Title'] = self.dataset['Title'].replace('Mme', 'Mrs')

        # grouped by Title, Pclass replaced NaN with group median
        self.dataset['Age'] = self.dataset.groupby(['Title', 'Pclass'])['Age'].apply(lambda x: x.fillna(x.median()))
        # binning with qcut
        self.dataset['CategoricalAge'] = pd.cut(self.dataset['Age'], 9)

        # Creating Deck column from the first letter of the Cabin column (M stands for Missing)
        self.dataset['Cabin'] = self.dataset['Cabin'].apply(lambda s: s[0] if pd.notnull(s) else 'M')

        # replace
        # Passenger in the T deck is changed to A
        self.dataset['Cabin'] = self.dataset['Cabin'].replace('T', 'A')
        self.dataset['Cabin'] = self.dataset['Cabin'].replace(['A', 'B', 'C'], 'ABC')
        self.dataset['Cabin'] = self.dataset['Cabin'].replace(['D', 'E'], 'DE')
        self.dataset['Cabin'] = self.dataset['Cabin'].replace(['F', 'G'], 'FG')

        # fill Nans
        self.dataset.Embarked.fillna('S', inplace=True)
        self.dataset.Gender.fillna('0', inplace=True)
        self.dataset['Title'].fillna('0', inplace=True)

        # replase and transform
        #self.dataset['TicketStr'], self.dataset['TicketNum'] = zip(*self.dataset['Ticket'].map(self.ticket_split))
        #self.dataset['TicketFrequency'] = self.dataset.groupby(['TicketNum', 'TicketStr', 'Fare'])\
        #                                ['TicketNum'].transform('count')

        # new columns
        self.dataset['Single'] = self.dataset['FamilySize'].map(lambda s: 1 if s == 1 else 0)
        self.dataset['SmallFamily'] = self.dataset['FamilySize'].map(lambda s: 1 if s == 2 else 0)
        self.dataset['MedFamily'] = self.dataset['FamilySize'].map(lambda s: 1 if (s == 3)|(s == 4) else 0)
        self.dataset['LargeFamily'] = self.dataset['FamilySize'].map(lambda s: 1 if s >= 5 else 0)

        # encode labels
        la = LabelEncoder()
        self.dataset['Gender'] = la.fit_transform(self.dataset['Gender'])

        # drop columns
        #drop_cols = ['Fare', 'Age', 'Name', 'FamilySize', 'Parch', 'SibSp',
        #             'PassengerId', 'Ticket', 'Cabin', 'TicketNum', 'TicketStr']

        drop_cols = ['Fare', 'Age', 'Name', 'FamilySize', 'Parch', 'SibSp',
                     'PassengerId', 'Ticket']

        self.dataset.drop(drop_cols, inplace=True, axis=1)

        columns_not_numeric = ['Title', 'CategoricalFare', 'CategoricalAge',
                               'Cabin', 'Embarked']
        for feature in columns_not_numeric:
            self.dataset[feature] = la.fit_transform(self.dataset[feature])

        #print(self.dataset.info())
        #print(self.dataset.columns.to_list())

        #features = self.dataset.columns.to_list()
        #x = self.dataset.values
        #x = StandardScaler().fit_transform(x)
        #self.dataset = pd.DataFrame(x, columns=features)

        return self.dataset.values


