# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Use Pandas to import the data from "fcc-forum-pageviews.csv" Set the index to the date column.
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = ['date'], index_col='date')

# 2. Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[
(df['value'] >= df['value'].quantile(0.025)) &
(df['value'] <= df['value'].quantile(0.975))]

# 3. Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png".
# The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019.
# The label on the x axis should be Date and the label on the y axis should be Page Views.

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(df.index, df['value'], color='r', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

# 4. Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". 
# It should show average daily page views for each month grouped by year. 
# The legend should show month labels and have a title of Months. 
# On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.

def draw_bar_plot():
    # Add columns for 'month' and 'years' extracted from 'date'
    df['year'] = df.index.year
    df['month'] = df.index.month
    # Restructure the dataframe to give the average page views per month
    df_bar = df.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()

    df_bar.plot(kind='bar', legend=True, figsize=(8,8))
    plt.title('Average Daily freeCodeCamp Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                'August', 'September', 'October', 'November', 'December'],
              title = 'Months');
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

# 5. Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". 
# These box plots should show how the values are distributed within a given year or month and how it compares over time. 
# The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). 
# Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. 
# The boilerplate includes commands to prepare the data. For each chart, make sure to use a copy of the data frame.

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')

    fig, axes = plt.subplots(1, 2, figsize=(15,5))
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    # Year-wise Box Plot (Trend)
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0], hue=df_box['year'].astype(str))
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise Box Plot (Seasonality)
    sns.boxplot(data=df_box, x='month', y='value', ax=axes[1], hue=df_box['month'].astype(str))
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views');

    fig.savefig('box_plot.png')
    return fig
