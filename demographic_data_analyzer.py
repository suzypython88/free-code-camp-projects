""" In this challenge you must analyze demographic data using Pandas.
You are given a dataset of demographic data that was extracted from the
1994 Census database.
You must use Pandas to answer the following questions:

Q1 How many people of each race are represented in this dataset?
This should be a Pandas series with race names as the index labels. (race column)
Q2 What is the average age of men?
Q3 What is the percentage of people who have a Bachelor's degree?
Q4 What percentage of people with advanced education (Bachelors, Masters, or Doctorate)
make more than 50K?
Q5 What percentage of people without advanced education make more than 50K?
Q6 What is the minimum number of hours a person works per week?
Q7 What percentage of the people who work the minimum number of hours per week have a
salary of more than 50K?
Q8 What country has the highest percentage of people that earn >50K and what is that percentage?
Q9 Identify the most popular occupation for those who earn >50K in India.
Use the starter code in the file demographic_data_analyzer.py.

Update the code so all variables set to None are set to the appropriate calculation or code.
Round all decimals to the nearest tenth.
"""

# Import pandas library
import pandas as pd

def calculate_demographic_data(print_answers=True):

    # Import data from 1994 US Census (from https://archive.ics.uci.edu/dataset/20/census+income)
    url = 'https://raw.githubusercontent.com/JakubPyt/Demographic_Data_Analyzer/main/adult.data.csv'
    cen = pd.read_csv(url, delimiter=';')
    # cen.head()

    # Check data types and look for null values
    # cen.info()

    # Q1 How many people of each race are represented in this dataset?
    # This should be a Pandas series with race names as the index labels. (race column)
    race_stats = cen['race'].value_counts()
    race_stats

    # Q2 What is the average age of men?
    # Create a filter to select 'Male' only
    men = cen['sex'] == 'Male'

    # Calculate the mean age for the filtered Male-only data set, rounding to 1 decimal place
    average_age_men = round(cen[men]['age'].mean(),1)

    # Q3 What is the percentage of people who have a Bachelor's degree?
    # Create a filter for just Bachelor's (disregarding that those with a Masters or Doctorate would also have a bachelor's degree)
    bachelors = cen['education'] == 'Bachelors'

    # Calculate the percentage of people with a Bachelor's degree, dividing number people with B by total number of people
    perc_bachelors = round((len(cen[bachelors]) / len(cen))*100,1)

    # Q4 What percentage of people with an advanced education make more than 50K?
    # Create a filter for people with a Bachelors, Masters or Doctorate
    advanced = cen['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    # Create filter for those who earn more than $50k
    earn_50k_plus = cen['salary'] == '>50K'

    # Create a combined filter for these two conditions
    adv_50k_filter = advanced & earn_50k_plus
    adv_50k_filter_df = cen[adv_50k_filter]

    # Calculate percentage of earners with advanced degrees that earn over $50k
    perc_adv_50k = round((len(cen[adv_50k_filter]) / len(cen[advanced]))*100,1)

    # Q5 What percentage of people without an advanced education make more than 50K?
    # Create a filter for those without an advanced degree using drop function
    non_advanced = ~cen['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    # Create a combined filter for these two conditions
    non_adv_50k_filter = non_advanced & earn_50k_plus
    non_adv_50k_filter_df = cen[non_adv_50k_filter]

    # Calculate percentage of earners without advanced degrees that earn over $50k
    perc_non_adv_50k = round((len(cen[non_adv_50k_filter]) / len(cen[non_advanced]))*100,1)

    # Q6 What is the minimum number of hours a person works per week?
    # We can find the minimum value of the column 'hours-per-week' using min function (or the describe function)
    min_work_hours = cen['hours-per-week'].min()

    # Q7 What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    # Create filter to combine both conditions
    min_work_hours_filter = cen['hours-per-week'] == min_work_hours

    # Create a combined filter for these two conditions
    min_hr_50k_filter = min_work_hours_filter & earn_50k_plus

    # Calculate the percentage of people with min hours with +50k salary
    perc_min_hr_50k = round((len(cen[min_hr_50k_filter]) / len(cen[min_work_hours_filter]))*100,1)

    # Q8 What country has the highest percentage of people that earn >50K and what is that percentage?
    # Find the number of people from each native country
    country_count = cen['native-country'].value_counts()

    # Find the number of $50k+ earners for each country
    country_50k_count = cen[cen['salary'] == '>50K']['native-country'].value_counts()

    # Find country with highest percentage of high earners (identify id in series with max value)
    # Max value will be the percentage of high earners in that country
    highest_50k_country = (country_50k_count / country_count * 100).idxmax()
    highest_perc_salary = round((country_50k_count / country_count * 100),1).max()

    # Q9 Identify the most popular occupation for those who earn >50K in India.
    # Select people with native country India who earn over $50k
    india_50k_plus = cen[(cen['native-country'] == 'India') & (cen['salary'] == '>50K')]
    top_India_occ = india_50k_plus['occupation'].value_counts()
    top_In = top_India_occ.idxmax()

    if print_answers:
        print("Number of each race:\n", race_stats)
        print('The average age of men is:', average_age_men)
        print(f"Percentage of people with a bachelor's degree: {perc_bachelors}%")
        print(f"Percentage of people with advanced's degrees earning over $50k: {perc_adv_50k}%")
        print(f"Percentage of People without Advanced's Degrees Earning over $50k: {perc_non_adv_50k}%")
        print(f"Minimum Hours Worked Per Week: {min_work_hours} hours/week")
        print(f"Percentage of People Working the Minimum Number of Hours Earning over $50k: {perc_min_hr_50k}%")
        print("The country with the highest number of earners over $50k in salary is", highest_50k_country, f"with {highest_perc_salary}%" )
        print("The most popular occupation for those who earn >50K of Indian nationality is", top_In)
    
    return {
        'race_count': race_stats,
        'average_age_men': average_age_men,
        'perc_bachelors': perc_bachelors,
        'perc_adv_50k': perc_adv_50k,
        'perc_non_adv_50k': perc_non_adv_50k,
        'min_work_hours': min_work_hours,
        'perc_min_hr_50k': perc_min_hr_50k,
        'highest_50k_country': highest_50k_country,
        'highest_perc_salary': highest_perc_salary,
        'top_In': top_In

    }