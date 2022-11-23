# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:16:01 2022

@author: jmjwj
"""

# 시각화

import pandas as pd
import os
import matplotlib.pyplot as plt
os.chdir('C:/Users/jmjwj/Documents/UOS/3학년 1학기/빅데이터 경진대회/찐')

a = pd.read_excel('final.xlsx')
a['class'] = pd.Series(['None']*26)
a.loc[(a['gu'] == '도봉구') | (a['gu'] == '성북구') | (a['gu'] == '양천구') |
      (a['gu'] == '노원구') | (a['gu'] == '은평구'), 'class'] = 'low'


a.loc[(a['gu'] == '중구') | (a['gu'] == '종로구') | (a['gu'] == '영등포구') |
      (a['gu'] == '용산구') | (a['gu'] == '강남구'), 'class'] = 'high' 
a.loc[a['class'] == 'None', 'class'] = 'mid'




from matplotlib import font_manager, rc
font_path = r"C:\Windows\Fonts\malgun.ttf"   #폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 도봉 성북 양천 노원 은평 / 중위값들 / 중구 종로 영등포 용산 강남
# 경제적 요인 
a['class'].group
#1. gdp -> 단순 비교?
a.groupby('class')['roadrate'].mean().loc[['low','mid','high']].plot.bar()
plt.title('1만명당 범죄 수 vs 도로율')

#2. 유흥구역 밀도 -> km 당 술집비교
a.groupby('class')['yuhueng_km'].mean().loc[['low','mid','high']].plot.bar()
plt.title('1만명당 범죄 수 vs 유흥업소 밀도')
#4. 제한구역 비율 -> 그냥 비교
a.groupby('class')['restricted_km'].mean().loc[['low','mid','high']].plot.bar()
plt.title('1만명당 범죄 수 vs 제한구역면적 비율')

#5. 인구밀도
a.groupby('class')['mandense_km'].mean().loc[['low','mid','high']].plot.bar()
plt.title('1만명당 범죄 수 vs 인구밀도')

#도로율
a.groupby('class')['roadrate'].mean().loc[['low','mid','high']].plot.bar()
plt.title('1만명당 범죄 수 vs 도로율')

a.loc[:,['gu','roadrate']].sort_values(by = a.roadrate)
