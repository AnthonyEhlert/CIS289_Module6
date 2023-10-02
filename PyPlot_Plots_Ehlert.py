"""
Program Name: PyPlot_Plots_Ehlert.py
Author: Tony Ehlert
Date: 9/27/2023

Program Description:  This program cleans and prepares a dataset containing information about two different climates for
visualizations. Once the dataset has been prepped a simple visualization is created displaying the average temp
for each reporting location, then a more complex visualization is created using subplots displaying the
average temperature along with the amount of precipitation for each day.
"""
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 450

# read csv file and create new df
base_climate_df = pd.read_csv("IA_HI_Climate_Dataset.csv")
#print(base_climate_df.columns)

# create new df with only needed columns from base df
trimmed_climate_df = base_climate_df[['NAME', 'DATE', 'PRCP', 'TAVG']]
#print(trimmed_climate_df.dtypes)

# remove any records that contain NaN in either 'PRCP' or 'TAVG' columns and create new df variable
nan_records_drop_df = trimmed_climate_df.dropna(subset=['PRCP', 'TAVG'])
#print(nan_records_drop_df)

# convert DATE col to datetime datatype and remove records not in month of January
jan_climate_df = nan_records_drop_df.copy()
jan_climate_df['DATE'] = pd.to_datetime(jan_climate_df['DATE'])
jan_climate_df = jan_climate_df[jan_climate_df['DATE'].dt.month == 1]
#print(jan_climate_df.to_string())

# create figures with only capital cities of states (one city per figure)
fig1_ia = jan_climate_df[jan_climate_df['NAME'] == 'DES MOINES INTERNATIONAL AIRPORT, IA US']
#print(fig1_ia)
fig2_hi = jan_climate_df[jan_climate_df['NAME'] == 'HONOLULU INTERNATIONAL AIRPORT, HI US']

# create basic plot showing average temp for locations
plt.plot(fig1_ia['DATE'].dt.day, fig1_ia['TAVG'], label='Des Moines, IA')
plt.plot(fig2_hi['DATE'].dt.day, fig2_hi['TAVG'], label='Honolulu, HI')
plt.xticks(fontsize=12)
plt.xlabel('Day of Month')
plt.ylabel("Avg. Temp(F)")
plt.title('Avg. Temp(F) for January 2023')
plt.minorticks_on()
plt.legend()
plt.show()

# create complex plot using subplots
fig, axs = plt.subplots(2,1)

axs[0].plot(fig1_ia['DATE'].dt.day, fig1_ia['TAVG'], label='Des Moines, IA')
axs[0].plot(fig2_hi['DATE'].dt.day, fig2_hi['TAVG'], label='Honolulu, HI')
axs[0].axes.get_xaxis().set_visible(True)
axs[0].axes.set_xticklabels('')
axs[0].title.set_text('Avg. Temp(F) for January 2023')
axs[0].axes.set_ylabel('Avg. Temp(F)')
axs[0].legend()
axs[0].grid(which='major', linestyle='-', color='#DDDDDD', linewidth=1.0)
axs[0].grid(which='minor', linestyle=':',color='#EEEEEE', linewidth=0.8)
axs[0].minorticks_on()

axs[1].plot(fig1_ia['DATE'].dt.day, fig1_ia['PRCP'], label='Des Moines, IA', color='g')
axs[1].plot(fig2_hi['DATE'].dt.day, fig2_hi['PRCP'], label='Honolulu, HI', color='r')
axs[1].title.set_text('Precipitation(Inches) for January 2023')
axs[1].axes.set_xlabel('Day of Month')
axs[1].axes.set_ylabel('Inches of Precipitation')
axs[1].legend()
axs[1].grid(which='major', linestyle='-', color='#DDDDDD', linewidth=1.0)
axs[1].grid(which='minor', linestyle=':',color='#EEEEEE', linewidth=0.8)
axs[1].minorticks_on()
plt.show()