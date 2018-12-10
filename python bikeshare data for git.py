import time
import datetime as dt
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    city = ""
    while city.lower() != "chicago" and city !="new york city" and city != "washington":
            city = input("Would you like data on chicago, new york city, or washington?").lower()
            city = str(city).lower()
            city= "chicago"
    month = ""
    while month.lower() != "no" and month != "yes":
        month = input("Would you like to choose a month?").lower()
    if month.lower() == "no":
       month="all"
    elif month == "yes":
        month = ""
        while month.lower() !="january" and month.lower() !="february" and month.lower() !="march" and month.lower() !="april" and month.lower() !="may" and month.lower() !="june":
            month = input("Please type the month you want from January to May.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while day.lower() != "no" and day != "yes":
        day = input("Would you like to choose a day of the week?")
    if day.lower() == "no":
       day="all"
    elif day == "yes":
        day = ""
        while day.lower() !="monday" and day.lower() !="tuesday" and day.lower() !="wednesday" and day.lower() !="thursday" and day.lower() !="friday" and  day.lower() !="satday" and day.lower() !="sunday":
            day = input("What day of the week would you like to choose?")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        ('int' or str) month - number of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_name'] = df['Start Time'].dt.weekday_name
    #get start hour from start time
    df['start_hour'] = df['Start Time'].dt.hour
    #make new collom of combo start and end
    df['start_end_combo'] = df['Start Station']+' to '+df['End Station']
    # filter by month if applicable (((
    if month != 'all':
        # filter by month to create the new dataframe
                      # use the index of the months list to get the corresponding int
        mo = ['january', 'february', 'march', 'april', 'may', 'june']
        month = mo.index(month) + 1
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_name'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
#(is most common a function? yes called mode )
    pop_month = df['month'].mode()[0]
    # TO DO: display the most common day of week
#(same as above but with filtered from datetime?)
    pop_day = df['day_name'].mode()[0]
    # TO DO: display the most common start hour
#(same as first? maybe some filtering like a dropon minutes)
    pop_hour = df['start_hour'].mode()[0]
    print("Most common month, day, and hour were;",pop_month,",", pop_day,",and", pop_hour,".")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
#(special function to find most common?)
    pop_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
#(lit same as above)
    pop_end_station = df['End Station'].mode()[0]
    # TO DO: display most frequent combination of start station and end station trip
#(make dic holding both then fillter? filter is likely a function so make new data type and use the function)
    pop_start_end_combo = df['start_end_combo'].mode()[0]
   #
    print("The most used start station was",pop_start_station,". The most used end station was",pop_end_station,". The most used start end combo was ",pop_start_end_combo)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Biikes were used for",total_time, "sec and the mean travel time was",mean_time,"sec.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    customers = df["User Type"].value_counts()
    # TO DO: Display counts of gender
#(same as above but check for city no check for line first or maybe just go with adding blank line and computing on that? set.issubset also nan out somewhere here for dropna oh wow just the first for both
    if "Gender" in df.columns:
        customer_gender = df["Gender"].value_counts()
        print("\nCounts of gender are",customer_gender,".")
    else:
        print("There is no gender data.")
        # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        recent_birth = df["Birth Year"].min()
        early_birth = df["Birth Year"].max()
        common_birth = df["Birth Year"].mode()[0]
        print("\nThe most common birth year was", common_birth,". \nThe earlist birth was",early_birth,". \nThe most recent birth was",recent_birth,".")
    else:
        print("There is no birth year data.")

    print("Counts of customer types are",customers,".")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def see_raw(df):# this is to see the raw data if wanted
    get_raw = ""
    gr= 0
    while get_raw != "y" and get_raw != "n": #filters user feedback
        get_raw = input("Would you like to see some lines of raw code from the dates selected? y/n")
    while get_raw == "y": #prints head if desired
        print(df.iloc[gr:gr+5])
        get_raw= ""
        gr = gr+5
        get_raw = input("Would you like to see more lines of code? y/n").lowercase


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        see_raw(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter y or n.\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
