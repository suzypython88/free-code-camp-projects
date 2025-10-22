## freeCodeCamp Course: 'Data Analysis with Python'
https://www.freecodecamp.org/learn/data-analysis-with-python

### Certification Exercises

---

### **Project 1: Mean-Variance-Standard Deviation Calculator**

Project Details: https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator

Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min,
and sum of the rows, columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, 
and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

The returned dictionary should follow this format:

{

  'mean': [axis1, axis2, flattened],
  
  'variance': [axis1, axis2, flattened],
  
  'standard deviation': [axis1, axis2, flattened],
  
  'max': [axis1, axis2, flattened],
  
  'min': [axis1, axis2, flattened],
  
  'sum': [axis1, axis2, flattened]
  
}


If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: 

"List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.

---


### **Project 2: Demographic Data Analyzer**

Project Details: https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer

In this challenge you must analyze demographic data using Pandas. You are given a dataset of demographic data that was extracted from the 1994 Census database.

You must use Pandas to answer the following questions:

1. How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)

2. What is the average age of men?

3. What is the percentage of people who have a Bachelor's degree?

4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

5. What percentage of people without advanced education make more than 50K?

6. What is the minimum number of hours a person works per week?

7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?

8. What country has the highest percentage of people that earn >50K and what is that percentage?

9. Identify the most popular occupation for those who earn >50K in India.

Update the code so all variables set to None are set to the appropriate calculation or code.
Round all decimals to the nearest tenth.

---
### **Project 3: Medical Data Visualizer**

Project Details: https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer

In this project, you will visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas.
The dataset values were collected during medical examinations.

**Data description**

The rows in the dataset represent patients and the columns represent information like body measurements,
results from various blood tests, and lifestyle choices.
You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

**Instructions:**

Create a chart similar to examples/Figure_1.png, where we show the counts of good and bad outcomes for the cholesterol, gluc, alco, active,
and smoke variables for patients with cardio=1 and cardio=0 in different panels.

By each number in the medical_data_visualizer.py file, add the code from the associated instruction number below.


1. Import the data from medical_examination.csv and assign it to the df variable.

2. Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight
in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for
NOT overweight and the value 1 for overweight.

3. Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0.
If the value is more than 1, set the value to 1.

4. Draw the Categorical Plot in the draw_cat_plot function.

5. Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.

6. Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

7. Convert the data into long format and create a chart that shows the value counts of the categorical features using the following
method provided by the seaborn library import: sns.catplot().

8. Get the figure for the output and store it in the fig variable.

9. Do not modify the next two lines.

10. Draw the Heat Map in the draw_heat_map function.

11. Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:

- diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
- height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
- height is more than the 97.5th percentile
- weight is less than the 2.5th percentile
- weight is more than the 97.5th percentile

12. Calculate the correlation matrix and store it in the corr variable.

13. Generate a mask for the upper triangle and store it in the mask variable.

14. Set up the matplotlib figure.

15. Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap().

16. Do not modify the next two lines.

---
### **Project 4: Page View Time Series Visualizer**
Project Details: https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer

For this project you will visualize time series data using a line chart, bar chart, and box plots. You will use Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. The data visualizations will help you understand the patterns in visits and identify yearly and monthly growth.

**Use the data to complete the following tasks:**

1. Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
   
3. Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
   
4. Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.
   
5. Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
   
6. Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data. For each chart, make sure to use a copy of the data frame.
The boilerplate also includes commands to save and return the image.

