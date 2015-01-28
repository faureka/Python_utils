import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition.pca import PCA
from sklearn.grid_search import GridSearchCV
from sklearn.svm import SVC
from sklearn.mixture import GMM
from sklearn.base import BaseEstimator
from sklearn.metrics import accuracy_score

class PcaGMM(BaseEstimator):
	"""docstring for PcaGMM"""
	def __init__(self, X_all,pca_components = 12,GMM_components = 4,
		covariance_type = "full",min_cov = 0.1,
		gamma = 0, C = 1.0):

		self.X_all = X_all
		self.pca_components = pca_components
		self.GMM_components = GMM_components
		self.covariance_type = covariance_type
		self.min_cov = min_cov
		self.gamma = gamma
		self.C = C

		X_all = X_all[:,:pca_components]
		self.gmm = GMM(n_components = GMM_components,
			covariance_type = covariance_type,
			min_covar = min_cov)

		self.gmm.fit(X_all)

	def fit(self,X,y):
		X = X[:,:self.pca_components]
		X = self.gmm.predict_proba(X)
		self.svm = SVC(C = self.C,gamma = self.gamma)
		self.svm.fit(X,y)

	def predict(self,X):
		X = X[:,:self.pca_components]
		return self.svm.predict(self.gmm.predict_proba(X))

	def score(self,X,y):
		y_pred = self.predict(X)
		return accuracy_score(y,y_pred)

	def transform(self,X,y = None):
		X = X[:,:self.pca_components]
		return self.gmm.predict_proba(X)

	def __str__(self):
		return "PCA(%d)-GMM(%d, %s, %f)-SVM(C=%f, gamma=%f)" % (self.pca_components, self.GMM_components,
                                                                self.covariance_type, self.min_cov,
                                                                self.C, self.gamma)


def kde_plot(x):
	from scipy.stats.kde import gaussian_kde
	kde = gaussian_kde(x)
	positions = np.linspace(x.min(),x.max())
	smoothed = kde(positions)
	plt.plot(positions,smoothed)	

def qq_plot(x):
	from scipy.stats import probplot
	probplot(x, dist='norm', plot=plt)

X_test = pd.read_csv('test.csv',header =None).as_matrix()
y = pd.read_csv('trainLabels.csv',header=None)[0].as_matrix()
X = pd.read_csv('train.csv',header =None).as_matrix()	

pca2 = PCA(n_components = 2, whiten = True)
pca2.fit(np.r_[X,X_test])
X_pca = pca2.transform(X)
i0 = np.argwhere(y ==0)[:,0]
i1 = np.argwhere(y ==1)[:,0]
X0 = X_pca[i0,:]
X1 = X_pca[i1,:]

# fig = plt.figure()
# fig = plt.plot(X0[:,0],X0[:,1],'ro',X1[:,0],X1[:,1],'bx')

pca = PCA(whiten=True)
X_all = pca.fit_transform(np.r_[X, X_test])
# print pca.explained_variance_ratio_


clf = PcaGMM(X_all,
            30, 4, 'full', 0, gamma = .6, C = 0.3)

X_t = clf.transform(pca.transform(X))
X0 = X_t[i0, :]
X1 = X_t[i1, :]
pca2 = PCA(n_components=2)
pca2.fit(np.r_[X0, X1])
# clf.fit(pca.transform(X_t),y)
# y_pred = clf.predict(pca.transform(X))
# print clf.score(pca.transform(X),y)
X0 = pca2.transform(X0)
X1 = pca2.transform(X1)
plt.plot(X0[:, 0], X0[:, 1], 'ro')
plt.plot(X1[:, 0], X1[:, 1], 'b*')

plt.show()



