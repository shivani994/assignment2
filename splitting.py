# write a python program to spliting  the dataset into training and testing set
import numpy as np
import pandas as pd
dataset=pd.read_csv("play_tennis.csv")
dataset
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
outlook_encoded=le.fit_transform(dataset.outlook)
print(outlook_encoded)
temp_encoded=le.fit_transform(dataset.temp)
print(outlook_encoded)
humidity_encoded= le.fit_transform(dataset.humidity)
wind_encoded= le.fit_transform(dataset.wind)
play_encoded= le.fit_transform(dataset.play)
dataset['outlook']=le.fit_transform(dataset.outlook)
dataset['temp']=le.fit_transform(dataset.temp)
dataset['humidity']=le.fit_transform(dataset.humidity)
dataset['wind']=le.fit_transform(dataset.wind)
dataset['play']=le.fit_transform(dataset.play)
x= dataset.iloc[:,:-1].values
print(x)
y=dataset.iloc[:,4].values
print(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y ,test_size=0.2)
print(x_train)
print(x_test)


