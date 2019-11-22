'''Trends-in-under-five-mortality-rate-data-visualization-graph-with-regression '''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
df = pd.read_csv("x.csv")
plt.title("Trends in under-five mortality rate")
plt.xlabel("Year")
plt.ylabel("Rate(PER 1,000 LIVE BIRTHS)")
plt.plot(df.Year,df.Rate,color ='blue', marker ='o')
reg = linear_model.LinearRegression()
reg.fit(df[['Year']],df.Rate)
p=reg.predict(2031)
print("Prediction =",p)   
