weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast', 'Sunny','Sunny','Rainy','sunny','Overcast','Overcats','Rainy']
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
play=['No','No','yes','yes','yes','No','yes','No','yes','yes','yes','yes','No']
#import LabelEncoder
from sklearn import preprocessing
#creating labelEncoder
le=preprocessing.LabEncoder()
#converting string label into numbers
temp_encoder=le.fit_transform(temp)
la