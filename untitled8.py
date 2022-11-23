# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:43:37 2022

@author: jmjwj
"""
import os
os.chdir('C:/Users/jmjwj/Documents/UOS/3학년 1학기/빅데이터 경진대회/찐')
a = pd.read_csv('allvar2.csv')


cctv = pd.read_csv(r"C:\Users\jmjwj\Documents\UOS\3학년 1학기\빅데이터 경진대회\찐\서울시CCTV설치운영현황(자치구)_년도별_211231기준.csv",
                   encoding = 'CP949')


a1 = cctv.loc[1:, ['2015년','2016년','2017년','2018년','2019년']]


cctv_processed=  pd.concat([a1.iloc[:,0],a1.iloc[:,1],a1.iloc[:,2],a1.iloc[:,3],a1.iloc[:,4]], axis = 0)
cctv_processed = cctv_processed.reset_index(drop = True)

b = pd.concat([a, cctv_processed], axis = 1)
b = b.rename(columns = {0 : 'cctv'})

gicho = pd.read_csv(r"C:\Users\jmjwj\Documents\UOS\3학년 1학기\빅데이터 경진대회\찐\국민기초생활보장+수급자(2015_2019)_20221116185736.csv", header = 3)
gicho.columns 
gicho.columns = ['x', '구별', '2015', '2016', '2017', '2018', '2019']
gicho_processed = pd.concat([gicho.loc[2:, '2015'], gicho.loc[2:, '2016'], gicho.loc[2:, '2017'], gicho.loc[2:, '2018'], gicho.loc[2:, '2019']], axis = 0)
gicho_processed = gicho_processed.reset_index(drop = True)

all2 = pd.read_excel(r"C:\Users\jmjwj\Documents\UOS\3학년 1학기\빅데이터 경진대회\찐\ALL.xlsx", header = 0)
wide= all2.면적_km
c = pd.concat([b, gicho_processed], axis = 1)

c.columns =[     'Unnamed: 0',            'year',              'gu',
              'roadrate',             'gnp',      'yuhueng_km',
            'livingprop',  'commercialprop', 'industrial_prop',
            'green_prop',   'restricted_km', 'policeoffice_km',
                   '119',     'mandense_km',             'sum',
             'crimerate',                 'cctv',                 'gicho']

people = c.mandense_km * wide
c['cctv_km'] = c.cctv.astype(int) / wide
c['restricted_km'] = c.restricted_km / wide
c['gicho_prop'] = c.gicho / people

c.to_csv('final.csv')
c.to_excel('final.xlsx')
