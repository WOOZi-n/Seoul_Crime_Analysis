# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 18:45:46 2022

@author: jmjwj
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor

model2=smf.ols(formula='crimetotal~녹지지역비율+신고출동수+유흥_per_km+가로등_per_km+실업률+도로율+주거지역비율',data=df20).fit()
model2.summary()
dfall6 = dfall6.rename(columns = {'112 신고출동 수' : '신고출동수', '도로율 (%)' : '도로율'})
dfall6['crimetotal'] = dfall6[['살인_1만명당', '강도_1만명당', '성범죄_1만명당','절도_1만명당', '폭력_1만명당']].sum(axis = 1)


dfall6.columns
model3=smf.ols(formula='crimetotal~녹지지역비율+신고출동수+유흥_per_km+가로등_per_km+실업률+도로율+주거지역비율',data=dfall6).fit()

model3.summary()
model3=smf.ols(formula='crimetotal~녹지지역비율+신고출동수+유흥_per_km+실업률+도로율+주거지역비율',data=dfall6).fit()
model3.summary()

model3=smf.ols(formula='crimetotal~녹지지역비율+신고출동수+유흥_per_km+실업률+도로율',data=dfall6).fit()
model3.summary()
model3.summary()
model3=smf.ols(formula='crimetotal~녹지지역비율+신고출동수+유흥_per_km+실업률',data=dfall6).fit()








dfall6.





