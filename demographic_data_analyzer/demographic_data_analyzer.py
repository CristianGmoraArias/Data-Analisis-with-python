import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('/workspace/boilerplate-demographic-data-analyzer/adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.value_counts('race')

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = ((df[df['education'] == 'Bachelors']['education'].count()/df['education'].count()) * 100).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    levels_advance_education = ['Bachelors','Masters','Doctorate']
    education = df['education'].isin(levels_advance_education)
    df_higher_education = df[education]
    df_lower_education = df[~education]
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round((len(df_higher_education)/len(df)) * 100,1)
    lower_education = round((len(df_lower_education)/len(df)) * 100,1)

    # percentage with salary >50K
    higher_education_rich = ((df_higher_education[df_higher_education['salary'] == '>50K']['education'].count()/df_higher_education['education'].count()) * 100).round(1)
    lower_education_rich = ((df_lower_education[df_lower_education['salary'] == '>50K']['education'].count()/df_lower_education['education'].count()) * 100).round(1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == 1 ]
    rich_percentage = round(((num_min_workers['salary'] == '>50K').sum() / num_min_workers['salary'].count()) * 100 , 1 )

    # What country has the highest percentage of people that earn >50K?
    count_by_country_salary = df.groupby(['native-country','salary']).size().unstack(fill_value = 0)
    count_by_country_salary['Total'] = count_by_country_salary['<=50K'] + count_by_country_salary['>50K']
    count_by_country_salary['% >50K'] = round((count_by_country_salary['>50K']/count_by_country_salary['Total']) * 100 , 1 )
    results_order = count_by_country_salary.sort_values(by='% >50K',ascending = False)

    highest_earning_country = results_order.first_valid_index()
    highest_earning_country_percentage = results_order.iloc[0]['% >50K']

    # Identify the most popular occupation for those who earn >50K in India.
    India_people = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    India_people = India_people.groupby(['occupation']).size().sort_values(ascending=False)
    top_IN_occupation = India_people.first_valid_index()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
