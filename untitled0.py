# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:53:52 2022

@author: jmjwj
"""

import os
import pandas as pd


os.chdir('C:/Users/jmjwj/Documents/UOS/3학년 1학기/빅데이터 경진대회')

#데이터 스키마
# df1 : 장소별 5대범죄 발생건수 데이터
# df2 ; 구 별 서울시 도로율 데이터
# df3_processed : 동 별 주점 수 합
# df4 : 구 별 용도지역 현황
# df5 : 동 별 주민등록인구 현황
# df6: 구 별 경찰서 신고출동 수
# df7 : 구 별 강력범죄 집계 수
# df8_matched : 동별 생활인구. 성별, 연령, 시간별
# df8_processed:  동별 생활인구. 이때 시간은 일몰 후인 
# df9 : 구 별 가로등 설치현황
# dongcode : 행정동코드와 실제 동명 매칭


df1=pd.read_csv('경찰청 서울특별시경찰청_5대범죄 발생 장소별 현황_20211231.csv',encoding='CP949')

df2= pd.read_excel('도로현황(도로율)_20221108014713.xlsx', header = 0)
df2[df2['자치구별(2)']!='소계']
df2.columns=['자치구별(1)','구별','도로연장 (km)','도로면적 (㎢)','도로율 (%)']
df2=df2.iloc[2:,1:].reset_index()
df2.drop('index', axis = 1, inplace = True)
df2


df4=pd.read_csv('용도지역+현황_20221109014219.csv',encoding='UTF-8', header = 4)
df4.columns
df4.columns = ["자치구별(1)",'자치구별(2)','주거지역1',
               '주거지역2','주거지역3','주거지역4','주거지역5','주거지역6','주거지역7',
               '상업지역','공업지역','녹지지역']
df4= df4[['자치구별(2)','주거지역1', '상업지역','공업지역','녹지지역']]
df4.replace('-', 0, inplace = True)
df4


df5=pd.read_csv('주민등록인구(월별)_20221108025100.csv',encoding='UTF-8')
df5=df5[(df5['동별(3)']!='소계')]
df5=df5[df5['2022. 09']!='소계']
df5.columns=['동별(1)','구별','동별','세대 (세대)','합계 (명)','합계 (명) 남자','합계 (명) 여자','한국인 (명)','한국인 (명) 남자','한국인 (명) 여자','외국인 (명)','외국인 (명) 남자','외국인 (명) 여자']
df5=df5.iloc[1:,1:]
df5


df3=pd.read_excel('식품위생업+현황(동별)(2008년+이후)_20221108015805.xlsx')
df3.columns=['동별(1)','구별','동별','소계','단란주점','유흥주점']
df3=df3.iloc[3:,2:].reset_index()
df3.drop(['index', '소계'], axis = 1, inplace =True )
df3.replace('-',0, inplace = True)
df3['주점'] = df3['단란주점'] + df3['유흥주점']
df3_processed = df3.drop(['단란주점','유흥주점'], axis = 1).iloc[2:,]
df3_processed

df6=pd.read_excel('경찰청 서울특별시경찰청_경찰서별 112신고 출동 현황_20211231.xlsx')
df6

df7=pd.read_excel('5대+범죄+발생현황_20221108210023.xlsx')
df7.drop(["Unnamed: 3","Unnamed: 5","Unnamed: 7","Unnamed: 9","Unnamed: 11","Unnamed: 13"],axis=1, inplace = True)
df7.columns=["자치구별(1)","구별","발생소계","살인발생","강도발생","강간 및 강제추행발생","절도발생","폭력발생"]
df7=df7.iloc[3:,1:]
df7


df8 = pd.read_csv("LOCAL_PEOPLE_DONG_202210.csv")
df8  = df8.reset_index().iloc[:,:-1]
df8
df8.columns = ['기준일ID', '시간대구분', '행정동코드', '총생활인구수', '남자0세부터9세생활인구수', '남자10세부터14세생활인구수',
       '남자15세부터19세생활인구수', '남자20세부터24세생활인구수', '남자25세부터29세생활인구수',
       '남자30세부터34세생활인구수', '남자35세부터39세생활인구수', '남자40세부터44세생활인구수',
       '남자45세부터49세생활인구수', '남자50세부터54세생활인구수', '남자55세부터59세생활인구수',
       '남자60세부터64세생활인구수', '남자65세부터69세생활인구수', '남자70세이상생활인구수', '여자0세부터9세생활인구수',
       '여자10세부터14세생활인구수', '여자15세부터19세생활인구수', '여자20세부터24세생활인구수',
       '여자25세부터29세생활인구수', '여자30세부터34세생활인구수', '여자35세부터39세생활인구수',
       '여자40세부터44세생활인구수', '여자45세부터49세생활인구수', '여자50세부터54세생활인구수',
       '여자55세부터59세생활인구수', '여자60세부터64세생활인구수', '여자65세부터69세생활인구수',
       '여자70세이상생활인구수']

dongcode = pd.read_excel("행정동코드.xlsx")
dongcode = dongcode.loc[dongcode.시도명 == '서울특별시',['행정동코드','시군구명','읍면동명']]
dongcode['행정동코드'] = dongcode.행정동코드.apply(lambda x : int(''.join(list(str(x))[:-2])))
df8_matched = pd.merge(df8, dongcode, on = '행정동코드', how = 'left')
df8_matched.groupby(['시군구명','시간대구분']).mean().reset_index().columns
df8_matched.head()



df9 = pd.read_csv("도로시설물_20221109025414.csv", header = 2)
df9 = df9.iloc[8:,1:3]


# dfall에 포함된 데이터 : 1(x) 2(o) 3(o) 4(ㅐo) 5(o) 6(보류) 7(o) 8(x) 9(o)
dfall=pd.merge(df5,df2,on='구별',how='outer')
dfall=pd.merge(dfall,df6,on='구별',how='outer')
# df6에서 구는 경찰서 별 구역을 뜻하는 것 같다. #df6파일 변경함. 주의
dfall=pd.merge(dfall,df7,on='구별',how='outer')

dfall2=pd.merge(dfall,df3_processed,on=['동별'],how='outer')
dfall3=pd.merge(dfall,df3_processed,on=['동별'])
dfall4= pd.merge(dfall3, df4, left_on = '구별', right_on = '자치구별(2)', how = 'left' )
dfall5= pd.merge(dfall4, df9, left_on = '구별', right_on = '자치구별(2)', how = 'left')
dfall5.drop('자치구별(2)_y', axis = 1, inplace = True)
#8번데이터는 분석 목적에 따라 다르게 전처리를 해서 붙여야 할것 같다.
#dfall3_1=dfall3.drop(['index_x','index_y'],axis=1)
# 현재 최종 데이터셋 : dfall5
# 구별데이터를 중심으로 만들자

gudata = pd.merge(df2, df4, left_on = '구별', right_on = '자치구별(2)', how = 'left')
gudata = pd.merge(gudata, df9, left_on = '구별', right_on = '자치구별(2)', how = 'left')
gudata = pd.merge(gudata, df7, on ='구별' , how = 'left')
gudata = pd.merge(gudata, df6, on = '구별', how= 'left')

dongdata = pd.merge(df5, df3_processed, on = '동별', how = 'left')
dongdata.columns
# 결측값 대체
dongdata.iloc[426, 12] = 0
dongdata.iloc[427, 12] = 0
dongdata.iloc[427, 11] = 34

dongdata[['세대 (세대)', '합계 (명)', '합계 (명) 남자', '합계 (명) 여자', '한국인 (명)',
       '한국인 (명) 남자', '한국인 (명) 여자', '외국인 (명)', '외국인 (명) 남자', '외국인 (명) 여자',
       '주점']] = dongdata[['세대 (세대)', '합계 (명)', '합계 (명) 남자', '합계 (명) 여자', '한국인 (명)',
       '한국인 (명) 남자', '한국인 (명) 여자', '외국인 (명)', '외국인 (명) 남자', '외국인 (명) 여자',
       '주점']].astype(int)

dongdata = dongdata.groupby(['구별']).sum().reset_index()

gudata = pd.merge(gudata, dongdata, on = '구별')
gudata.to_csv('20221110_구별로묶은데이터')

#최종데이터 : gudata

motel = pd.read_csv("서울시 숙박업 인허가 정보.csv", encoding = 'CP949')
motel = motel['지번주소']
motel = motel.dropna()
motel = motel.apply(lambda x : str(x).split()[1])
motel.value_counts().reset_index()

