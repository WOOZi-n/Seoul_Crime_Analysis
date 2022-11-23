# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 03:12:47 2022

@author: jmjwj
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


a = pd.read_excel('ALL.xlsx')
a2 = pd.read_csv('연별 범죄.csv', header = 2)
a3 = pd.concat([a,a2.발생], axis = 1)
b = a3.iloc[100:,:]
b.columns
b['범죄per'] = b.발생/(b.인구밀도_km * b.면적_km)
b.sort_values(by = '범죄per')
b.columns


# 2019 기준 상위 5: 중구 종로구 영등포구 용산구 강남구
            # 하위 5: 도봉구 성북구 양천구 노원구 은평구
            # 비교 대상 : 주거지역(용도지역 분포) / 소득 / 유흥주점 / ....
# 직관 : 유동인구가 높은 곳에서 범죄율이 높게 일어남. (자명)

# 범죄별 추이?
a2.columns = ['id', '합계', '살인', '강도', '성범죄', '절도', '폭력',
       '연', '구별']

a2['합계']  = a2.합계/(a.인구밀도_km * a.면적_km)
a2['살인']  = a2.살인/(a.인구밀도_km * a.면적_km)
a2['강도']  = a2.강도/(a.인구밀도_km * a.면적_km)
a2['성범죄']  = a2.성범죄/(a.인구밀도_km * a.면적_km)
a2['절도']  = a2.절도/(a.인구밀도_km * a.면적_km)
a2['폭력']  = a2.폭력/(a.인구밀도_km * a.면적_km)




a4 = a2.loc[a2.연==2019 ,['합계','살인','강도','성범죄','절도','폭력','구별']]
# 범죄율 하위 5개구/ 범죄율 상위 5개구
a4.sort_values(by = '합계') # 도봉 성북 양천 노원 은평 / 중구 종로 영등포 용산 강남
a4.sort_values(by = '살인') # 도봉 마포 서대문 은평 성북  / 종로 금천 구로 성동 강북
a4.sort_values(by = '강도') # 은평 동작 양천 강서 마포 / 중구 종로 금천 강동 성동
a4.sort_values(by = '성범죄') # 도봉 양천 노원 중랑 성북 / 종로 중구 서초 마포 강남 
a4.sort_values(by = '절도') # 도봉 성북 노원 성동 양천 / 중구 종로 영등포 마포 강남
a4.sort_values(by = '폭력') # 양천 성북 도봉 강서 은평 / 중구 종로 용산 강북 영등포



gicho = pd.read_csv(r"C:\Users\jmjwj\Documents\UOS\3학년 1학기\빅데이터 경진대회\찐\국민기초생활보장+수급자(2020년+이후)_20221116173611.csv", header = 2)
gicho
