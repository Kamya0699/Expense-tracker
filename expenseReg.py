import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm
class Regression:
    def __init__(self):

         self.data=pd.read_csv("expense.csv")
         print(self.data)
         self.X=self.data['ID'].values.reshape(-1,1)
         self.y=self.data['amount'].values.reshape(-1,1)
         self.reg=LinearRegression()
         self.reg.fit(self.X,self.y)
         print("the linear model is :Y={:.5}+{:.5}X".format(self.reg.intercept_[0],self.reg.coef_[0][0]))

         self.predictions=self.reg.predict(self.y)
         plt.figure(figsize=(10,5))
         plt.scatter(self.data['amount'],self.data['ID'], c='black')
         plt.plot(self.data['amount'], self.predictions, c='blue', linewidth=2)
         plt.xlabel("amount")
         plt.ylabel("ID")
         plt.show()

         self.X = self.data['ID']
         self.y = self.data['amount']
         self.X2 = sm.add_constant(self.X)
         self.est = sm.OLS(self.y, self.X2)
         self.est2 = self.est.fit()
         print(self.est2.summary())
         print(self.predictions)
         print("Working")


