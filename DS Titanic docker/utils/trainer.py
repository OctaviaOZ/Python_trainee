from sklearn.svm import SVC
import pickle


class Estimator:
    @staticmethod
    def fit(train_x, train_y):

        model = SVC(kernel='rbf', C=10, degree=0, gamma=0.01, probability=True)
        result = model.fit(train_x, train_y)
        with open('models/SVC.pickle', 'wb')as f:
            pickle.dump(model, f)
        return result

    @staticmethod
    def predict(trained, test_x):
        return trained.predict(test_x)


