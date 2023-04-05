# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 02:17:39 2023

@author: Hp
"""


# bringing in various libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


""" importing/reading csv files into a pandas data frame """


def dataset(world_bank, country, column, indicators):
    data = pd.read_csv(world_bank, skiprows=4)
    data = data[data['Indicator Name'] == indicators]
    data = data[column]
    data.set_index('Country Name', inplace=True)
    data = data.loc[country]
    transposed_data = data.transpose()
    return data, transposed_data


world_bank = 'API_19_DS2_en_csv_v2_5346672.csv'
country = ['North America', 'Canada', 'Mexico',
           'United Kingdom', 'Belgium', 'Germany']


column = ['Country Name', '2010', '2011', '2012', '2013',
          '2014', '2015', '2016', '2017', '2018', '2019', '2020']

indicators = ['Agricultural land (% of land area)',
              'Electricity production from coal sources (% of total)', 'Forest area (% of land area)']

country_agric, yr_agric = dataset(
    world_bank, country, column, indicators[0])
country_electric, yr_electric = dataset(
    world_bank, country, column, indicators[1])
country_forest, yr_forest = dataset(
    world_bank, country, column, indicators[2])

print(yr_agric)

# Annual line graph charting Trends for the 6 countries' agricultural land (percentage of total land area)


# Annual line graph charting Trends for the 6 countries' agricultural land (percentage of total land area)
# set the figure size and dpi
plt.figure(figsize=(15, 9), dpi=600)

# plot the agricultural land data for each country
for n in range(len(country)):
    plt.plot(yr_agric.index, yr_agric[country[n]], label=country[n])

# add a legend and adjust its position
plt.legend(bbox_to_anchor=(0, 1), fontsize=15)

# adding title, x-axis label, and y-axis label
plt.title('Trend in Agricultural Land', fontsize=15)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Agricultural Land (% of Land Area)', fontsize=15)

# display the plot
plt.show()
print(yr_electric.describe())

# plotting line graph of the trend over time for the 6 countries'Electricity production from coal sources(as a percentage of the total)


plt.figure(figsize=(15, 11), dpi=600)
for x in range(len(country)):
    plt.plot(yr_electric.index,
             yr_electric[country[x]], label=country[x])
plt.legend(bbox_to_anchor=(0, 1), fontsize=15)
plt.title('The state of coal-based electricity production', fontsize=15)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Electricity production from coal sources (% of total)', fontsize=15)
plt.show()


# Showing a grouped bar graph for the amount of electricity produced from coal sources for various nations over time
country_electric.plot(kind='bar')

# adding a title, x-axis label, and y-axis label
plt.title('Electricity Production from Coal Sources by Country', fontsize=15)
plt.xlabel('Country', fontsize=15)
plt.ylabel('Coal-fueled Electricity Production (% of Total)', fontsize=15)

# setting the figure dpi
plt.rcParams["figure.dpi"] = 1500

# displaying the plot
plt.show()


# Agricultural land(% of land area) for several countries over time plotted as a grouped bar chart
country_agric.plot(kind='bar')

# adding a title, x-axis label, and y-axis label
plt.title('Agricultural Land by Country', fontsize=15)
plt.xlabel('Country', fontsize=15)
plt.ylabel('Agricultural Land (% of Land Area)', fontsize=15)

# setting the figure dpi
plt.rcParams["figure.dpi"] = 1600

# displaying the plot
plt.show()


print(yr_agric['Canada'])

# Showing heatmap for Canada

Canada_data = pd.DataFrame(
    {'Lands for Agriculture': yr_agric['Canada'],
     'Electricity production from coal': yr_electric['Canada'],
     'Forest areas': yr_forest['Canada']},
    ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'])

print(Canada_data.corr())

plt.figure(figsize=(10, 7))
sns.heatmap(Canada_data.corr(), cmap='magma', annot=True)
plt.title('Heatmap for Canada')
plt.show()


# Showing heatmap for Mexico

Mexico_data = pd.DataFrame(
    {'Lands for Agriculture': yr_agric['Mexico'],
     'Electricity production from coal': yr_electric['Mexico'],
     'Forest areas': yr_forest['Mexico']},
    ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'])

print(Mexico_data.corr())

plt.figure(figsize=(12, 7))
sns.heatmap(Mexico_data.corr(), cmap='viridis', annot=True)
plt.title('Heatmap for Mexico')
# showing the plot
plt.show()
