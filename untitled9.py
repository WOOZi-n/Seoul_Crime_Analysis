# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 21:11:39 2022

@author: jmjwj
"""
import pandas as pd
drink = pd.read_csv(r'C:\Users\jmjwj\Documents\UOS\3학년 1학기\빅데이터 경진대회\찐\식품위생업+현황(구별)_20221116224159.csv')
motel = pd.read_csv(r"C:\Users\jmjwj\Documents\UOS\3학년 1학기\빅데이터 경진대회\찐\공중위생업+현황(2011년+이후)_20221116223813.csv")

drink2 = drink[2:].groupby('자치구별(2)').sum().reset_index()
motel2 = motel[['동별(2)','2021']][1:]

yuheung = pd.merge(drink2, motel2, left_on = '자치구별(2)', right_on = '동별(2)')
yuheung['yuheung'] = yuheung['2021_x'] + yuheung['2021_y'] 
yuheung = yuheung[['자치구별(2)','yuheung']]
yuheung

all = pd.read_excel('ALL.xlsx')
all['gu'] = list(all['구별'].apply(lambda x : x[:-4]))
temp = all[['gu','면적_km']][:25]

yuheung2= pd.merge(yuheung, temp, left_on = '자치구별(2)', right_on = 'gu')
yuheung2['yuheung_km'] = yuheung2.yuheung / yuheung2.면적_km

yuheung2
yuheung2.to_excel('2021유흥.xlsx')

all.gu = a

yuheung2['자치구별(2)' == a]
yuheung2.columns
yuheung2.index= yuheung['자치구별(2)']gu')['yuheung_km']
yuheung2

yuheung2.reindex()

pd.merge(all, yuheung2, left_on = 'gu', right_on = '