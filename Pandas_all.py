import pandas as pd
import numpy as np
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
#print(df.groupby('Year').get_group(2014))
#print(df[(df['Team']=='Kings') & (~df['Year'].isin([2014,2017]))])
#print(df[(df['Team'] =='Riders') | (df['Year'].isin([2014,2017]))])
#print(df[(df.Team =='Riders') & (df.Year.ge(2014))])
#print(df[(df.Team =='Riders') & (df['Year'].gt(2014))])
#print(df[(df.Team =='Riders') & (df['Year'].between(2015,2017))])
#print(df[df.Year.isin([2014,2017]) & (df.Team=='Kings')].sort_values(by='Rank',ascending=False))
#print(df.query('Rank >= 3 and Year in [2014,2015]'))
print(df.shape)

''' can use filters in many ways
df.where((df[column_name]conditions values) &|....)
df.loc[(df[column_name]conditions values) &|....]
df.eval("'column_name conditions values &| (same format like previous)....")same as query
df.query('column_name conditions values &| (same format like previous)....')
df.column_name conditoins value
df[(df[column_name] conditions(like >=<str) values) &| (df[])......[specific column names to display if want to, sperated by comma in quotes]

'''

'''
apart from this can use (filter and transfor) are used but with groupby only
(half will continue when get time)
'''
