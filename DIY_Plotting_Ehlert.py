"""
Program Name: DIY_Plotting_Ehlert.py
Author: Tony Ehlert
Date: 9/27/2023

Program Description: This program creates two visualizations of a  video game dataset using the matplotlib library.
One dataset is very simple and displays the total video games sales by genre, while the other is more complex and
contains coloring options as well as shadowing and font size options in the legend and displays the percentage
of genre sales by region
"""
import pandas as pd
import matplotlib.pyplot as plt

# read .csv file to new df
base_video_game_df = pd.read_csv('Video_Games_Dataset.csv')
#print(base_video_game_df)

# create new df with only needed columns
vid_game_sales_by_genre_df = base_video_game_df[['Genre', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].copy()
#print(vid_game_sales_by_genre_df)

# remove any records that has null/NaN for 'Genre'
vid_game_sales_df = vid_game_sales_by_genre_df.dropna(subset=['Genre'])
#print(vid_game_sales_df)

# create new grouped by genre df
vid_game_sales_by_genre_df = vid_game_sales_by_genre_df.groupby(['Genre'])

# sum new grouped by dataframe and overwrite existing df
vid_game_sales_by_genre_df = vid_game_sales_by_genre_df.sum()

# sort grouped df by 'Global_Sales' in ascending order
vid_game_sales_by_genre_df = vid_game_sales_by_genre_df.sort_values(by=['Global_Sales'], ascending=True)
#print(vid_game_sales_by_genre_df.to_string())
#print(vid_game_sales_by_genre_df.shape)

# reset index of df so 'Genre' can be selected as column
vid_game_sales_by_genre_df = vid_game_sales_by_genre_df.reset_index()

# rename 'Role-Playing' 'Genre' to RPG to save space on plot
vid_game_sales_by_genre_df.loc[8, 'Genre'] = 'RPG'
#print(vid_game_sales_by_genre_df)

# create list of 'Genre' values for use on y-axis plot
y_labels = vid_game_sales_by_genre_df['Genre'].to_list()
#print(y_labels)

# create basic plot/chart and adjust y-axis font size using yticks()
plt.barh(y_labels, vid_game_sales_by_genre_df['Global_Sales'])
plt.title('Total Video Game Sales by Genre')
plt.xlabel('Millions Sold')
plt.yticks(fontsize= 9)
plt.show()

# create separate figures for top four selling genres for plotting
fig1_na = vid_game_sales_by_genre_df[['Genre', 'NA_Sales']]
fig2_eu = vid_game_sales_by_genre_df[['Genre', 'EU_Sales']]
fig3_jp = vid_game_sales_by_genre_df[['Genre', 'JP_Sales']]
fig4_other = vid_game_sales_by_genre_df[['Genre', 'Other_Sales']]

# create genre labels for complex graph
complex_graph_labels = fig1_na['Genre'].tolist()

# create total_height variable
total_height = [sum(x) for x in zip(fig1_na['NA_Sales'].tolist(), fig2_eu['EU_Sales'].tolist(), fig3_jp['JP_Sales'].tolist(), fig4_other['Other_Sales'].tolist())]

fig1_na = (fig1_na['NA_Sales']/total_height)*100
fig2_eu = (fig2_eu['EU_Sales']/total_height)*100
fig3_jp = (fig3_jp['JP_Sales']/total_height)*100
fig4_other = (fig4_other['Other_Sales']/total_height)*100

# create height variables for figures
fig2_height = fig1_na.tolist()
fig3_height = [sum(x) for x in zip(fig2_height, fig2_eu.tolist())]
fig4_height = [sum(x) for x in zip(fig3_height, fig3_jp.tolist())]


plt.barh(complex_graph_labels, fig1_na, color='b', label='North American Sales')
plt.barh(complex_graph_labels, fig2_eu, left=fig2_height, color='g', label='European Sales')
plt.barh(complex_graph_labels, fig3_jp, left=fig3_height, color='y', label='Japanese Sales')
plt.barh(complex_graph_labels, fig4_other, left=fig4_height, color='purple', label='Other Regions Sales')
plt.yticks(fontsize=9)
plt.legend(loc= 'best', fancybox=True, shadow=True, fontsize=9)
plt.title('% of Video Game Genre Sales by Region')
plt.show()