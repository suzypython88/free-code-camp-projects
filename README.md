## freeCodeCamp Course: 'Data Analysis with Python'
https://www.freecodecamp.org/learn/data-analysis-with-python

### Certification Exercises

---

### **Project 1: Mean-Variance-Standard Deviation Calculator**

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
