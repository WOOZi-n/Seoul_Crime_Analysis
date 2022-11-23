# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:58:50 2022

@author: jmjwj
"""

import os
import pandas
os.chdir(r'C:\Users\jmjwj\Documents\UOS\3학년 1학기\빅데이터 경진대회\찐')

crime = pd.read_excel(r"C:\Users\jmjwj\Documents\UOS\3학년 1학기\빅데이터 경진대회\찐\5대+범죄+발생현황_20221112102601.xlsx",
                      header = [0,1,2,3])
crime

garo = pd.read_excel(r'C:\Users\jmjwj\Documents\UOS\3학년 1학기\빅데이터 경진대회\찐\도로시설물_20221112102429.xlsx',
                     header = [0,1,2])
garo

roadrate = pd.read_excel(r"C:\Users\jmjwj\Documents\UOS\3학년 1학기\빅데이터 경진대회\찐\도로현황(도로율)_20221112102507.xlsx",
                         header = [0,1])

production = pd.read_excel(r"C:\Users\jmjwj\Documents\UOS\3학년 1학기\빅데이터 경진대회\찐\자치구별+1인당+지역내총생산+및+수준지수(2015년+기준)_20221112152823.xlsx", 
                           header=  [0,1])
production

tel = pd.read_excel(r"C:\Users\jmjwj\Documents\UOS\3학년 1학기\빅데이터 경진대회\찐\공중위생업+현황(2011년+이후)_20221112153427.xlsx")
drink = pd.read_excel(r"C:\Users\jmjwj\Documents\UOS\3학년 1학기\빅데이터 경진대회\찐\식품위생업+현황(동별)(2008년+이후)_20221112152616.xlsx",
                      header = [0,1,2,3])

yongdo = pd.read_excel(r"C:\Users\jmjwj\Documents\UOS\3학년 1학기\빅데이터 경진대회\찐\용도지역+현황_20221112151144.xlsx",
                       header = [0,1,2,3,4])

# crime2
crime2 = pd.concat([crime['2015'], crime['2016'],
                    crime['2017'],crime['2018'],crime['2019']],axis = 0)
crime2.reset_index(drop = True)
crime2['year'] = [2015]*26 + [2016]*26 + [2017]*26 + [2018]*26 + [2019]*26

gu = crime['자치구별(2)']
for k in range(4):
    gu = gu.append(crime['자치구별(2)'])
gu.reset_index()

crime2['구별'] = gu

crime2 = crime2.loc[crime2.구별 != '소계',:]
crime2.to_csv('연별 범죄.csv')
crime2.columns = ['합','살인','강도','성범죄','절도','폭력','year','구별']
crime2.columns

#garo2
garo2 = pd.concat([garo['2015'], garo['2016'],
                    garo['2017'],garo['2018'],garo['2019']],axis = 0)
garo2.reset_index(drop = True)
garo2['year'] = [2015]*26 + [2016]*26 + [2017]*26 + [2018]*26 + [2019]*26

gu = garo['자치구별(2)']
for k in range(4):
    gu = gu.append(garo['자치구별(2)'])
gu.reset_index()

garo2['구별'] = gu

garo2 = garo2.loc[garo2.구별 != '소계',:]
garo2.columns = ['가로등','year','구별']
garo2.to_csv('연별 r가로등.csv')

#roadrate
roadrate2 = pd.concat([roadrate['2015'], roadrate['2016'],
                    roadrate['2017'],roadrate['2018'],roadrate['2019']],axis = 0)
roadrate2.reset_index(drop = True)
roadrate2['year'] = [2015]*26 + [2016]*26 + [2017]*26 + [2018]*26 + [2019]*26

gu = roadrate['자치구별(2)']
for k in range(4):
    gu = gu.append(roadrate['자치구별(2)'])
gu.reset_index()

roadrate2['구별'] = gu

roadrate2 = roadrate2.loc[roadrate2.구별 != '소계',:]
roadrate2 = roadrate2[['도로율 (%)','year','구별']]
roadrate2.to_csv('연별 도로율.csv')
roadrate2
#production2
production2 = pd.concat([production['2015'], production['2016'],
                    production['2017'],production['2018'],production['2019']],axis = 0)
production2.reset_index(drop = True)
production2['year'] = [2015]*26 + [2016]*26 + [2017]*26 + [2018]*26 + [2019]*26

gu = production['자치구별(2)']
for k in range(4):
    gu = gu.append(production['자치구별(2)'])
gu.reset_index()

production2['구별'] = gu

production2 = production2.loc[production2.구별 != '소계',:]
production2.to_csv('연별 1인당생산.csv')
production2
#tel
tel2 = tel[['동별(2)','2015','2016','2017','2018','2019']]
tel3 = tel2.set_index('동별(2)').stack().reset_index()[5:]
tel3.columns = ['구별','year','motel']
tel3.reset_index(drop =True)
tel3['year'] = tel3.year.astype(int)
tel3.to_csv('연별 모텔.csv')
#drink
drink2 = pd.concat([drink['2015'], drink['2016'],
                    drink['2017'],drink['2018'],drink['2019']],axis = 0)
drink2.reset_index(drop = True)
drink2['year'] = [2015]*26 + [2016]*26 + [2017]*26 + [2018]*26 + [2019]*26

gu = drink['동별(2)']
for k in range(4):
    gu = gu.append(drink['동별(2)'])
gu.reset_index()

drink2['구별'] = gu

drink2 = drink2.loc[drink2.구별 != '소계',:]
drink2.columns = [['총','접객업','단란주점','유흥주점','year','구별']]
drink2.columns = drink2.columns.get_level_values(0)
drink2['drink'] = drink2.단란주점+drink2.유흥주점
drink3 = drink2[['drink', 'year','구별']]
drink3.to_csv('연별 술집.csv')

#yongdo
yongdo
yongdo2 = pd.concat([yongdo['2015'], yongdo['2016'],
                    yongdo['2017'],yongdo['2018'],yongdo['2019']],axis = 0)
yongdo2.reset_index(drop = True)
yongdo2['year'] = [2015]*26 + [2016]*26 + [2017]*26 + [2018]*26 + [2019]*26

gu = yongdo['자치구별(2)']
for k in range(4):
    gu = gu.append(yongdo['자치구별(2)'])
gu.reset_index()

yongdo2['구별'] = gu

yongdo2 = yongdo2.loc[yongdo2.구별 != '소계',:]
yongdo2
yongdo2.columns.get_level_values(2)
yongdo2.columns = ['주거', '1', '2', '3', '4', '5', '6', '상업',
       '공업', '녹지', '연', '구별']

yongdo3 = yongdo2[['주거','상업','공업','녹지','연','구별']]
yongdo3.replace('-',0)
yongdo3.to_csv('연별 용도지역.csv')



dat = pd.merge(crime2, garo2, on = ['구별','year'])
dat2 = pd.merge(dat, roadrate2, on = ['구별','year'])
dat3 = pd.merge(dat2, production2, on = ['구별','year'])
dat4 = pd.merge(dat3,tel3, on = ['구별','year'])
dat5 = pd.merge(dat4, drink3, on = ['구별','year'])
dat6 = pd.merge(dat5, yongdo3,left_on = ['구별','year'], right_on = ['구별','연'])
dat6.to_csv('all.csv')


