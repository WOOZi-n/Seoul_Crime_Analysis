# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 18:09:35 2022

@author: jmjwj
"""
import pandas as pd
import os
os.chdir('C:/Users/jmjwj/Documents/UOS/3학년 1학기/빅데이터 경진대회/찐')
a = pd.read_csv('all.csv')
a['industrial_area'] = a.industrial_area.replace('-',0).astype(float)

b = pd.read_excel('ALL.xlsx', header = 0)
b.columns

tot = pd.concat([b,a] , axis =1)
tot.columns

a.columns
area = a.living_area + a.commercial_area + a.industrial_area + a.green_area
a['주거지역비율'] = a.living_area / area 
a['상업지역비율'] = a.commercial_area / area 
a['공업지역비율'] = a.industrial_area / area 
a['녹지지역비율'] = a.green_area / area 

a['유흥업소'] = a.motel + a.drink
a['유흥업소_km'] = a.유흥업소 / b.면적_km
a.columns
a.columns
a = a.drop(['garo','motel','drink','living_area','commercial_area', 'industrial_area', 'green_area', '유흥업소'], axis = 1)
a.to_csv('all2.csv')

import numpy as np

# data leakage
x = b['119신고수']
y = a['sum']
np.corrcoef(x,y)


a.columns
b.columns

#X
a_sort = a[['year','gu','roadrate','gnp','유흥업소_km','주거지역비율','상업지역비율','공업지역비율','녹지지역비율']]
b_sort = b[['구별','제한구역면적_km','치안기관수_km','119신고수','인구밀도_km']]
X = pd.concat([a_sort,b_sort], axis = 1)

#y

y = a['sum']


#modeling
#without 신고수
formodel = pd.concat([X,y], axis = 1 )
formodel.drop('구별', axis = 1)
from statsmodels.formula.api import ols
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
scaled = sc.fit_transform(formodel.iloc[:, 2:])
scaled = pd.DataFrame(scaled)

formodel['crimerate'] = formodel['sum']*10000 / (b['면적_km'] * b['인구밀도_km']) # 1만명당 범죄 수
formodel.drop(['구별'], axis = 1, inplace = True)
formodel.columns= ['year', 'gu', 'roadrate', 'gnp', 'yuhueng_km', 'livingprop', 'commercialprop','industrial_prop', 'green_prop', 'restricted_km', 'policeoffice_km', '119', 'mandense_km', 'sum','crimerate' ]
formodel.to_csv('allvar2.csv')
formodel.to_excel('allvar2.xlsx')


model = ols('crimerate ~  gnp + 유흥업소_km + 주거지역비율 + 제한구역면적_km + roadrate',  formodel)

model.fit().summary()
model.exog_names
for k in range(1, len(model.exog_names)):
    print(variance_inflation_factor(model.exog, k))

y = formodel.crimerate
x = formodel[['gnp','유흥업소_km', '주거지역비율','공업지역비율','제한구역면적_km','roadrate','치안기관수_km']]

y2 = formodel2.crimerate
x2 = formodel2[['gnp','유흥업소_km', '주거지역비율','공업지역비율','제한구역면적_km','roadrate','치안기관수_km']]

from sklearn.model_selection import train_test_split

formodel2 = formodel.sort_values(by = 'gu')
x_train = x2.iloc[:100,:]
x_test = x2.iloc[100:,:]
y_train = y2.iloc[:100]
y_test = y2.iloc[100:]

train = pd.concat([x_train, y_train], axis = 1)
test = pd.concat([x_test, y_test], axis = 1)
formodel2.columns


# 최종모델 결정
model = ols('crimerate ~  gnp + 유흥업소_km + 주거지역비율 + 제한구역면적_km + roadrate',  train)
model3 = ols('crimerate ~  gnp + 유흥업소_km + 주거지역비율 + 제한구역면적_km + roadrate',  formodel2)

model.fit().summary()
model3.fit().summary()

model.fit().summary()
model.exog_names
for k in range(1, len(model.exog_names)):
    print(variance_inflation_factor(model.exog, k))

x_train2 = x_train[['gnp', '유흥업소_km','roadrate', '주거지역비율', '제한구역면적_km']]
x_test2 = x_test[['gnp', '유흥업소_km','roadrate', '주거지역비율', '제한구역면적_km']]
y_train
y_test

from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(x_train2, y_train)
reg.score(x_train2, y_train)
reg.score(x_test2, y_test)

mean_squared_error(y_train, reg.predict(x_train2))
mean_squared_error(y_test, reg.predict(x_test2))


forsasx = pd.concat([x_train2, x_test2], axis = 0)
forsasy = pd.concat([y_train, y_test], axis = 0)
forsas = pd.concat([forsasx, forsasy], axis = 1)
forsas.to_csv('forsas.csv')

forsas.iloc[110:120,:]
forsas2 = pd.concat([forsas.iloc[:110,:], forsas.iloc[120:,:]], axis = 0)
forsas2.to_csv('forsas2.csv')
# 종로구와 중구는 예측값이 크다.


forsas2
