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


def dataset(filename, countries, columns, indicator):
    df = pd.read_csv(filename, skiprows=4)
    df = df[df['Indicator Name'] == indicator]
    df = df[columns]
    df.set_index('Country Name', inplace=True)
    df = df.loc[countries]
    return df, df.transpose()


filename = 'API_19_DS2_en_csv_v2_5346672.csv'
countries = ['Canada', 'Mexico', 'Belgium',
             'North America', 'United Kingdom', 'Germany']
columns = ['Country Name', '2010', '2011', '2012', '2013',
           '2014', '2015', '2016', '2017', '2018', '2019', '2020']
indicators = ['Agricultural land (% of land area)',
              'Electricity production from coal sources (% of total)', 'Forest area (% of land area)']

country_agric, year_agric = dataset(
    filename, countries, columns, indicators[0])
country_electric, year_electric = dataset(
    filename, countries, columns, indicators[1])
country_forest, year_forest = dataset(
    filename, countries, columns, indicators[2])

print(year_agric)

# plotting line graph year on year Trend of the Agricultural land (% of land area) for the 6 countries

plt.figure(figsize=(10, 7), dpi=500)
for i in range(len(countries)):
    plt.plot(year_agric.index, year_agric[countries[i]], label=countries[i])
plt.legend(bbox_to_anchor=(1, 1), fontsize=20)
plt.title('Trend of the Agricultural land', fontsize=20)
plt.xlabel('Year', fontsize=20)
plt.ylabel('Agricultural land (% of land area)', fontsize=20)
plt.show()

print(year_electric.describe())

# plotting line graph year on year Trend of the Electricity production from coal sources (% of total) for the 6 countries


plt.figure(figsize=(10, 7), dpi=500)
for i in range(len(countries)):
    plt.plot(year_electric.index,
             year_electric[countries[i]], label=countries[i])
plt.legend(bbox_to_anchor=(1, 1), fontsize=20)
plt.title('Trend of the Electricity production from coal sources', fontsize=20)
plt.xlabel('Year', fontsize=20)
plt.ylabel('Electricity production from coal sources (% of total)', fontsize=20)
plt.show()


# plotting of grouped bar chart for Electricity production from coal sources (% of total) for different countries over the years

country_electric.plot(kind='bar')
plt.title('Electricity production from coal sources', fontsize=20)
plt.xlabel('Countries', fontsize=20)
plt.ylabel('Electricity production from coal sources', fontsize=20)
plt.rcParams["figure.dpi"] = 1500
plt.show()

# plotting of grouped bar chart for Agricultural land (% of land area) for different countries over the years

country_agric.plot(kind='bar')
plt.title('Agricultural land', fontsize=20)
plt.xlabel('Countries', fontsize=20)
plt.ylabel('Forest area (% of land area)', fontsize=20)
plt.rcParams["figure.dpi"] = 1500
plt.show()

print(year_agric['Canada'])

# ploting of heatmap of Canada

Canada = pd.DataFrame(
    {'Agricultural land': year_agric['Canada'],
     'Elect prod from coal': year_electric['Canada'],
     'Forest area': year_forest['Canada']},
    ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'])

print(Canada.corr())

plt.figure(figsize=(8, 5))
sns.heatmap(Canada.corr(), annot=True, cmap='Reds')
plt.title('Correlation heatmap Canada')
plt.show()


# ploting of heatmap of Mexico

Mexico = pd.DataFrame(
    {'Agricultural land': year_agric['Mexico'],
     'Elect prod from coal': year_electric['Mexico'],
     'Forest area': year_forest['Mexico']},
    ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'])

print(Mexico.corr())

plt.figure(figsize=(8, 5))
sns.heatmap(Mexico.corr(), annot=True, cmap='Blues')
plt.title('Correlation heatmap Mexico')
plt.show()
