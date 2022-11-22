import pandas
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
df = pandas.read_csv("multipleRegression.csv") 
X= df[['Weight', 'Volume']]
Y= df['CO2']
regr = LinearRegression()
regr.fit(X, Y)
test_Y = regr.predict(X)
predictedCO2 = regr.predict([2300,1300])
print(predictedCO2)

 
