from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.cross_validation import train_test_split
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
Data = pd.read_csv("f_DFF.csv", header = False)
Data = Data[["MNTM", "TSNW", "Specific_Yield", "Failure_Rate","CSI Project Tilt","MTR","GHI"]]
Data.columns # check all the variables 
Data.columns = ["MNTM", "TSNW", "Specific_Yield", "Failure_Rate","Tilt","MTR","GHI"]
train, test = train_test_split(Data, test_size = 0.2) #split the data set
#convert array to data frame
train = pd.DataFrame(train, columns=["MNTM", "TSNW", "Specific_Yield", "Failure_Rate","Tilt","MTR", "GHI"])
test = pd.DataFrame(test, columns=["MNTM", "TSNW", "Specific_Yield", "Failure_Rate","Tilt","MTR","GHI"])
train.to_csv("train.csv")
test.to_csv('test.csv')
lm = smf.ols(formula='Specific_Yield ~ MNTM + TSNW + Failure_Rate + Tilt + MTR + GHI',
             data=train, missing='drop').fit()
lm.summary()

lm1 = smf.ols(formula='Specific_Yield ~ MNTM  + Tilt + GHI + MTR + TSNW',
             data=train, missing='drop').fit()
lm1.summary()
lm2 = smf.ols(formula='Specific_Yield ~ GHI + MNTM',
             data=train, missing='drop').fit()
lm2.summary()
#Factory = Data[Data['Manufacturer' == 'BYD' or 'Canadian Solar' or "First Solar" or "Hanwha" or "solarone"
#                    or "Jinko Solar" or "SunPower" or "LG Electronics" or 
