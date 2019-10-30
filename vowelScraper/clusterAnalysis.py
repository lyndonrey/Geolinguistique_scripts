#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import csv 
from sklearn.cluster import KMeans
import sys

# Get data from CSV file
data = np.genfromtxt(sys.argv[1], delimiter=", ")
#I CHANGED THE DATA ROW INDICES B/C THE BUCKEYE CORPUS DOESN'T HAVE INTENSITY
f1 = data[:, [1]]
f2 = data[:, [2]]

f1f2 = data[:, [2,1]]

kmeans = KMeans(n_clusters=int(sys.argv[2]))
kmeans.fit(f1f2)
labels = kmeans.predict(f1f2)
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(15,15))
colmap = {1: 'r', 2: 'g', 3: 'b', 4: 'c', 5: 'm', 6: 'y', 7: 'k', 8: 'w'}
colors = map(lambda x: colmap[x+1], labels)

colorsList = list(colors)

if (sys.argv[3] == 'true'):
    plt.scatter(f2, f1, color=colorsList, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])
       

print(centroids)

plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.show()
fig.savefig(sys.argv[4], bbox_inches='tight')