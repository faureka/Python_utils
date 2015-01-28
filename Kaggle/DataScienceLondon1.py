import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition.pca import PCA
from sklearn.grid_search import GridSearchCV
from sklearn.svm import SVC
from sklearn.mixture import GMM
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.linear_model import SGDClassifier
from sklearn.utils import shuffle
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier

def soft_absolute(u):
    epsilon = 1e-8
    return np.sqrt(u*u + epsilon)

def logistic(u):
    return 1. / (1. + np.exp(-u))

class SparseFilter(BaseEstimator, TransformerMixin):
    def __init__(self, n_features = 200, n_iterations = 300, activate=soft_absolute):
        self.epsilon = 1e-8
        self.n_features = n_features
        self.n_iterations = n_iterations
        self.activate = activate
    def fit(self, X, y = None):
        n_samples, n_dim = X.shape
        W = np.random.randn(n_dim, self.n_features)
        b = np.random.randn(self.n_features)
        obj_fn = self.get_objective_fn(X)
        self.W_, self.b_ = optimize.fmin_l_bfgs_b(obj_fn, (W, b), 
                                iprint = 1, 
                                maxfun = self.n_iterations)
        return self
    def get_objective_fn(self, X):
        def _objective_fn(W, b):
            Y = self.activate(np.dot(X, W) + b)
            Y = Y / np.sqrt(np.sum(Y*Y, axis = 0) + self.epsilon)
            Y = Y / np.sqrt(np.sum(Y*Y, axis = 1)[:, np.newaxis] + self.epsilon)
            return np.sum(Y)
        return _objective_fn
    def transform(self, X):
        Y = self.activate(np.dot(X, self.W_) + self.b_)
        Y = Y / np.sqrt(np.sum(Y*Y, axis=0) + self.epsilon)
        Y = Y / np.sqrt(np.sum(Y*Y, axis=1)[:, np.newaxis] + self.epsilon)
        return Y

X_test = pd.read_csv('test.csv',header =None)
y = pd.read_csv('trainLabels.csv',header=None)
X = pd.read_csv('train.csv',header =None)

# print X_test.shape , y.shape , X.shape

