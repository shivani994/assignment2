from operator import le
import pandas as pd
info={'Gender':['Male','Female','Female','Male','Female'],'Position':['Head','Asst.Prof','Associate Prof','Asst.Prof','Asst.Prof.']}
df=pd.DateFrame(info)
print(df)
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
gender_encoded=le.fit_transform(df['Gender'])
encoded_position=le.fit_transform(df['Position'])
df['Encoded_Gender']=gender_encoded
df['Encoded_Position']=encoded_position
print(df)