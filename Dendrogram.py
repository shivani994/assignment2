import numpy as nm
import pandas as pd
import matplotlib.pyplot as mtp
dataset=pd.read_csv("diabetes.csv")
x=dataset.iloc[:,[3,4]].values
import scipy.cluster.hierarchy as shc
dendro =shc.dendrogram(shc.linkage(x,method ="ward"))
mtp.title("Dendrogrma Plot")
mtp.ylabel("Euclidean Distance")
mtp.xlabel("Customers")
mtp.show()
