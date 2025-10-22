# freeCodeCamp Data Analysis with Python - Project 3
# Medical Data Analyzer
# See https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Import the data from medical_examination.csv and assign it to the df variable.
df = pd.read_csv('medical_examination.csv')

# 2. Add an overweight column to the data.
# To determine if a person is overweight, first calculate their BMI by dividing their
# weight in kilograms by the square of their height in meters.
df['bmi'] = round(df['weight'] / (df['height']/100)**2,1)

# If that value is > 25 then the person is overweight.
# Use the value 0 for NOT overweight and the value 1 for overweight.
df['overweight'] = df['bmi'].apply(lambda x: 1 if x > 25 else 0)

# 3. Normalize the data by making 0 always good and 1 always bad.
# If the value of cholesterol or gluc is 1, set the value to 0.
# If the value is more than 1, set the value to 1
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4. Draw the Categorical Plot in the draw_cat_plot function
# 5. Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature.
    # You will have to rename one of the columns for the catplot to work correctly.

    # 7. Convert the data into long format and create a chart that shows the value counts of the categorical features
    df_cat['total'] = 1
    df_cat1 = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()

    ''' Create a chart that shows the value counts of the categorical features using
    the following method provided by the seaborn library import: sns.catplot() '''
    # Optional: Set the style theme to the inbuilt Seaborn 'darkgrid' style
    # sns.set_theme(style="darkgrid")
    fig = sns.catplot(x="variable",
                  y="total",
                  hue="value",
                  col="cardio",
                  data=df_cat1,
                  kind="bar").fig
    # 8. Get the figure for the output and store it in the fig variable.
    # 9. Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# 10. to 16. Draw the Heat Map in the draw_heat_map function.
# 11. Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data
df_heat = df[
(df['ap_lo'] <= df['ap_hi']) &
(df['height'] >= df['height'].quantile(0.025)) &
(df['height'] <= df['height'].quantile(0.975)) &
(df['weight'] >= df['weight'].quantile(0.025)) &
(df['weight'] <= df['weight'].quantile(0.975))]

# 12. Calculate the correlation matrix and store it in the corr variable
corr = df_heat.corr()

# 13. Generate a mask for the upper triangle and store it in the mask variable
# Use Numpy function triu to nullify the upper half of the correlation matrix, otherwise it would be duplicated
mask = np.triu(corr) 

# 14. Set up the matplotlib figure
# Set up blank chart to host the correlation matrix
fig, ax = plt.subplots(figsize=(12,12))

# 15. Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap()
plt.title('Correlation Between Health Factors')
sns.heatmap(corr, linewidths=1, annot=True, square=True, mask=mask, fmt='.1f', center=0.08, cbar_kws={'shrink':0.5});

# 16. Do not modify the next two lines.
fig.savefig('heatmap.png')
return fig
