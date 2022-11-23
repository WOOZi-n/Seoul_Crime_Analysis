# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 12:04:03 2022

@author: jmjwj
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
os.chdir('C:/Users/jmjwj/Documents/UOS/3학년 1학기/빅데이터 경진대회')
original = pd.read_csv('original.csv')
original = original.drop('Unnamed: 0', axis = 1)
original = pd.merge(original, alone_processed, left_on = '구별', right_on = '자치구별(2)').drop('자치구별(2)', axis = 1)
original.columns
original.columns =  ['gu', 'roadrate', '112call', 'living_pop', 'man_total', 'woman_total',
       'korean', 'korean_man_total', 'korean_woman_total', 'foreigner', 'foreigner_man_total',
       'foreigner_woman_total', 'unemployment', 'light', 'size', 'housing_land_rate', 'commercial_land_rate', 'industry_land_rate',
       'green_land_rate', 'yuhueng_per_km', 'light_per_km', 'murder_per_10k', 'rob_per_10k', 'sexualcrime_per_10k',
       'thief_per_10k', 'violence_per_10k', 'prod_per_1','women_alone_house']




#EDA 필요

#클러스터링 전 표준화
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
original_scaled = ss.fit_transform(original.iloc[:,1:])
original_scaled = pd.DataFrame(original_scaled)
original_scaled.columns = original.columns[1:]
original_scaled.index=  original['gu']

# 여성범죄 / 생계형 범죄 / 아동범죄 /  

original.columns
#클러스터링 돌릴만한 것.

original.