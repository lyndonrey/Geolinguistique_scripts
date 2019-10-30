#! /usr/bin/env python

import sys
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt(sys.argv[1], delimiter=', ')[:, [2,3,4,5,6]]

k_means = KMeans(n_clusters=7, random_state=0).fit(data)

k_means.predict(data)

centroids = k_means.cluster_centers_
print(centroids)
