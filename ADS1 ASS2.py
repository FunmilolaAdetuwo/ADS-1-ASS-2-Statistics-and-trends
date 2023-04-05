# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 02:17:39 2023

@author: Hp
"""


# importing different libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


"""reading csv files of Agricultural land(% of land area),Electricity Production from coal sources(% of total),
     and  forest area (% of land area) into pandas data frame"""

def dataset(filename,countries,columns,indicator):
    df = pd.read_csv(filename,skiprows=4)
    df = df[df['Indicator Name'] == indicator]
    df = df[columns]
    df.set_index('Country Name', inplace = True)
    df = df.loc[countries]
    return df,df.transpose()
     
     
filename = 'API_19_DS2_en_csv_v2_5346672.csv'
countries = ['Canada', 'Mexico', 'Belgium', 'North America','United Kingdom','Germany']
columns = ['Country Name', '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
indicators = ['Agricultural land (% of land area)', 'Electricity production from coal sources (% of total)', 'Forest area (% of land area)']

country_agric,year_agric = dataset(filename,countries,columns,indicators[0])
country_electric,year_electric = dataset(filename,countries,columns,indicators[1])
country_forest,year_forest = dataset(filename,countries,columns,indicators[2])

print(year_agric)

#plotting line graph year on year Trend of the Agricultural land (% of land area) for the 6 countries

plt.figure(figsize=(10,7),dpi=500)
for i in range(len(countries)):
    plt.plot(year_agric.index,year_agric[countries[i]],label=countries[i])
plt.legend(bbox_to_anchor=(1,1))
plt.title('Trend of the Agricultural land')
plt.xlabel('Year')
plt.ylabel('Agricultural land (% of land area)')
plt.show()

print(year_electric.describe())

#plotting line graph year on year Trend of the Electricity production from coal sources (% of total) for the 6 countries


plt.figure(figsize=(10,7),dpi=500)
for i in range(len(countries)):
    plt.plot(year_electric.index,year_electric[countries[i]],label=countries[i])
plt.legend(bbox_to_anchor=(1,1))
plt.title('Trend of the Electricity production from coal sources')
plt.xlabel('Year')
plt.ylabel('Electricity production from coal sources (% of total)')
plt.show()


#plotting of grouped bar chart for Electricity production from coal sources (% of total) for different countries over the years

country_electric.plot(kind='bar')
plt.title('Electricity production from coal sources')
plt.xlabel('Countries')
plt.ylabel('Electricity production from coal sources')
plt.rcParams["figure.dpi"] = 1500
plt.show()

#plotting of grouped bar chart for Agricultural land (% of land area) for different countries over the years

country_agric.plot(kind='bar')
plt.title('Agricultural land')
plt.xlabel('Countries')
plt.ylabel('Forest area (% of land area)')
plt.rcParams["figure.dpi"] = 1500
plt.show()

print(year_agric['Canada'])

#ploting of heatmap of Canada

Canada = pd.DataFrame(
{'Agricultural land': year_agric['Canada'],
'Elect prod from coal': year_electric['Canada'],
'Forest area': year_forest['Canada']},
['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'])

print(Canada.corr())