# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 01:58:43 2022

@author: jmjwj
"""

import pandas as pd
import os
os.chdir('C:/Users/jmjwj/Documents/UOS/3학년 1학기/빅데이터 경진대회')

dfall = pd.read_csv("구별데이터2.csv", encoding = 'CP949')
dfall.drop('Unnamed: 0', axis = 1, inplace = True)
garo = pd.read_csv("도로시설물_20221109025414.csv")
garo = garo.iloc[10:, 1:3]
dfall2 = pd.merge(dfall, garo, left_on = '구별', right_on = '자치구별(2)')
dfall2.columns
dfall2 = dfall2.rename(columns = {'주거지역1' : '주거지역', '2021': '가로등'})
dfall2.drop('자치구별(2)', axis =1 , inplace = True)

income = pd.read_excel("자치구별 지역내총생산(2015년 기준)_20221111003009.xlsx")
income = income.iloc[2:, :2].reset_index(drop = True)
admin = pd.read_excel("행정구역(1990_2005)_20221111003033.xlsx",header = 1)
size = admin.iloc[1:, :2]

motel = pd.read_csv("서울시 숙박업 인허가 정보.csv", encoding = 'CP949')
motel = motel['지번주소']
motel = motel.dropna()
motel = motel.apply(lambda x : str(x).split()[1])
motel_count = motel.value_counts().reset_index()

dfall3 = pd.merge(dfall2, motel_count, left_on = '구별', right_on = 'index')
dfall3.drop(['index'], axis =1, inplace = True)
income = income.rename(columns = {'자치구별': '구별'})
income['구별'] = income.구별.apply(lambda x: x.strip())
size['구별'] = size.자치구별.apply(lambda x: x.strip())

dfall4 = pd.merge(dfall3, income, on = '구별')
dfall5 = pd.merge(dfall4, size, on = '구별')
dfall5.drop('자치구별', axis = 1, inplace= True)
dfall5['유흥'] = dfall5.주점 + dfall5.지번주소
dfall5.drop(['주점', '지번주소'], axis = 1, inplace = True)
dfall5.columns
# dfall5를 rawdata로 두자.
#파생변수

dfall6 = dfall5.copy()
dfall6['용도지역'] = dfall6['주거지역'] + dfall6['상업지역'] + dfall6['공업지역'] + dfall6['녹지지역']
dfall6['주거지역비율'] = dfall6['주거지역'] / dfall6['용도지역']
dfall6['상업지역비율'] = dfall6['상업지역'] / dfall6['용도지역']
dfall6['공업지역비율'] = dfall6['공업지역'] / dfall6['용도지역']
dfall6['녹지지역비율'] = dfall6['녹지지역'] / dfall6['용도지역']
dfall6['가로등_per_km'] = dfall6['가로등'].astype(int) / dfall6['면적 (km²)']
dfall6['유흥_per_km'] = dfall6['유흥'] / dfall6['면적 (km²)']
dfall6['살인_1만명당'] = dfall6['살인발생'] / dfall6['거주인구(명)']*10000
dfall6['강도_1만명당'] = dfall6['강도발생'] / dfall6['거주인구(명)']*10000
dfall6['성범죄_1만명당'] = dfall6['강간 및 강제추행발생'] / dfall6['거주인구(명)']*10000
dfall6['절도_1만명당'] = dfall6['절도발생'] / dfall6['거주인구(명)']*10000
dfall6['폭력_1만명당'] = dfall6['폭력발생'] / dfall6['거주인구(명)']*10000

dfall6 = dfall6[['구별', '도로율 (%)', '112 신고출동 수', '거주인구(명)', '합계 (명) 남자',
       '합계 (명) 여자', '한국인 (명)', '한국인 (명) 남자', '한국인 (명) 여자', '외국인 (명)',
       '외국인 (명) 남자', '외국인 (명) 여자', '실업률', '가로등', '2019', '면적 (km²)',
       '주거지역비율', '상업지역비율', '공업지역비율', '녹지지역비율', '유흥_per_km', '가로등_per_km',
       '살인_1만명당', '강도_1만명당', '성범죄_1만명당', '절도_1만명당', '폭력_1만명당']]


dfall6['1인당생산'] = dfall6['2019']/dfall6['거주인구(명)']
dfall6.drop('2019', axis =1, inplace = True)
dfall6


dfall5.to_csv('rawdata.csv')
dfall6.to_csv('original.csv')

alone = pd.read_csv("1인가구(연령별)_20221108024555.csv", header = 4)
alone.columns = ["자치구별(1)",'자치구별(2)','소계1','소계2','소계3','20세미만총','20세미만남','20세미만여',
                 '20~24세총','20~24세남','20~24세여','25~29세총','25~29세남','25~29세여','30~34세총','30~34세남',
                 '30~34세여','35~39세총','35~39세남','35~39세여','40~44세총','40~44세남','40~44세여','45~49세총',
                 '45~49세남','45~49세여','50~54세총','50~54세남','50~54세여','55~59세총','55~59세남','55~59세여',
                 '60~64세총','60~64세남','60~64세여','65~69세총','65~69세남','65~69세여','70~74세총','70~74세남',
                 '70~74세여','75~79세총','75~79세남','75~79세여','80~84세총','80~84세남','80~84세여',
                 '85세이상총','85세이상남','85세이상여']

alone['취약여성1인가구'] = alone['20세미만여'] + alone['20~24세여'] + alone['30~34세여'] + alone['35~39세여'] + alone['40~44세여'] + alone['45~49세여'] 
alone_processed = alone[['자치구별(2)', '취약여성1인가구']]
alone_processed

dfall6

