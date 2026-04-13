# K MEANS 
from sklearn.datasets import load_iris 
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt 
 
data=load_iris() 
x=data.data[:,:2] 
 
kmeans=KMeans(n_clusters=3,random_state=0) 
y_kmeans=kmeans.fit_predict(x) 
 
plt.scatter(x[:,0],x[:,1],c=y_kmeans) 
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=200) 
plt.title("K Means Clustering (Iris Dataset)") 
plt.show() 

# PCA 
from sklearn.datasets import load_iris 
from sklearn.decomposition import PCA 
import matplotlib.pyplot as plt 
 
data = load_iris () 
X = data.data 
y = data.target 
 
pca = PCA(n_components=2) 
X_pca = pca.fit_transform (X) 
 
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y) 
plt.title ("PCA - Iris Dataset") 
plt.xlabel ("PC1") 
plt.ylabel ("PC2") 
plt.show () 

#ICA 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.decomposition import FastICA 
 
time = np.linspace (0, 8, 1000) 
 
s1 = np.sin (2 * time) 
s2 = np.sign(np.sin(3 * time)) 
 
S = np.c_[s1, s2] 
 
A = np. array([ [1, 1], [0.5, 2]] ) 
X = np.dot (S, A.T) 
 
ica = FastICA(n_components=2) 
S = ica.fit_transform (X) 
 
plt.figure () 
plt.subplot (3,1,1) 
plt.title ("Original Signals") 
plt.plot (S) 
 
plt.subplot (3,1,2) 
plt.title ("Mixed Signals") 
plt.plot (X) 
 
plt.subplot (3,1,3) 
plt.title("Recovered Signals (ICA) ") 
plt.plot (S ) 
 
plt.tight_layout () 
plt.show () 

# Apriori 
import pandas as pd 
from mlxtend.frequent_patterns import apriori, association_rules 
 
dataset = [ 
['Milk', 'Bread', 'Butter'], 
['Bread', 'Butter' ], 
['Milk', 'Bread'], 
['Milk', 'Butter'], 
['Bread', 'Butter' ]
] 
 
from mlxtend.preprocessing import TransactionEncoder 
te = TransactionEncoder () 
te_data = te.fit (dataset) .transform (dataset) 
df = pd. DataFrame (te_data, columns=te.columns_) 
 
frequent_items = apriori (df, min_support=0.4, use_colnames=True)
rules = association_rules (frequent_items, metric="confidence", min_threshold=0.5) 
 
print ("Frequent Itemsets:\n", frequent_items) 
print ("\nAssociation Rules: \n", rules)
