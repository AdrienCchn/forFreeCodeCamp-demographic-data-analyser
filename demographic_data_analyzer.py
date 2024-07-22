import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    DATA_FILENAME = "adult.data.csv"
    df = pd.read_csv(DATA_FILENAME, header=None, sep=",", index_col=False, skipinitialspace=True, names=["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "income-class"])
    
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts().values
    
    
    # What is the average age of men?
    average_age_men = df[df["sex"] == "Male"]["age"].mean()
    
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df[df["education"] == "Bachelors"].shape[0] / df.shape[0]) * 100
    
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    bool_sup50K = df["income-class"] == ">50K"
    bool_higher_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[bool_higher_education].shape[0]
    lower_education = df[~bool_higher_education].shape[0]
    
    
    # percentage with salary >50K
    higher_education_rich = (df[bool_higher_education & bool_sup50K].shape[0] / higher_education) * 100
    lower_education_rich = (df[(~bool_higher_education) & bool_sup50K].shape[0] / lower_education) * 100
    
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()
    
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    bool_min_workers = df["hours-per-week"] == df["hours-per-week"].min()
    num_min_workers = df[bool_min_workers].shape[0]
    
    bool_min_workers_sup50K = (df["hours-per-week"] == df["hours-per-week"].min()) & bool_sup50K
    num_min_workers_sup50K = df[bool_min_workers_sup50K].shape[0]
    
    rich_percentage = (num_min_workers_sup50K / num_min_workers) * 100
    
    
    # What country has the highest percentage of people that earn >50K?
    ## Create the colonnes to compare to obtain percentage
    df_per_countries_all = pd.DataFrame(df["native-country"].value_counts().sort_index())
    df_per_countries_sup50K = pd.DataFrame(df["native-country"][bool_sup50K].value_counts().sort_index())
    
    ## Create the dataframe then obtain the percentage
    df_per_countries_allAndsup50K = pd.concat([df_per_countries_all, df_per_countries_sup50K], axis=1)
    df_per_countries_allAndsup50K.columns = ["total", "sup50K"]
    df_per_countries_allAndsup50K['rich_percentage_by_countries'] = (df_per_countries_allAndsup50K["sup50K"] / df_per_countries_allAndsup50K["total"]) * 100
    
    ## Answers
    highest_earning_country = df_per_countries_allAndsup50K['rich_percentage_by_countries'].idxmax()
    highest_earning_country_percentage = df_per_countries_allAndsup50K['rich_percentage_by_countries'].max()
    
    
    # Identify the most popular occupation for those who earn >50K in India.
    df_IN_occupation = pd.DataFrame(df[(df["native-country"] == "India") & bool_sup50K]["occupation"].value_counts())
    top_IN_occupation = df_IN_occupation.idxmax()[0]
    
    
    
    
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
