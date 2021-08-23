import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAYS=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


"""user input """

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input(' \nInter one city of these :  chicago , new york city or washington \n').lower()
        if city in CITY_DATA:
            break
        else:
            print("\nwrong!! wrong!! , enter agian ")
    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("\nInter one months  of these : January, February, March, April, May, June or all \n").lower()

        if month in MONTHS:
            break
        else:
            print("\nwrong!! wrong!! , enter agian ")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nInter one days  of these :? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all)? \n").lower()
        if day in DAYS:
            break
        else:
            print("\nwrong!! wrong!! , enter agian ")

    print('-'*40)
    return city, month, day







def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['DofW'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        df = df[df['Month'] == month]



    if day != 'all':
        df = df[df['DofW'] == day.title()]

    return df





def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(f"The most common month  {df['Month'].mode()[0]}")

    # display the most common day of week
    print(f"The most common day of week  {df['DofW'].mode()[0]}")

    # display the most common start hour
    print(f"The most common start hour  {df['Hour'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df ):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_s_station = df['Start Station'].mode()[0]
    print('The Most common start station:', common_s_station)

    # TO DO: display most commonly used end station

    common_e_station = df['End Station'].mode()[0]
    print(' The Most common end station:', common_e_station)
    # TO DO: display most frequent combination of start station and end station trip

    df[' The Trip']=  df['Start Station'] + '   ' + df['End Station'] + '\"'
    common_trip = df[' The Trip'].mode()[0]
    print(common_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration ')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_sum =df['Trip Duration'].sum()
    print("total travel : " ,total_travel_sum )
    # TO DO: display mean travel time
    total_travel_mean=df['Trip Duration'].mean()
    print(" mean travel :" , total_travel_mean)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # TO DO: Display counts of user types

    utc = df['User Type'].value_counts()
    print(utc)
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("Sorry , no gender information in this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print(f" earliest year  {df['Birth Year'].min()}")
        print(f" recent year  {df['Birth Year'].max()}")
        print(f" most common year  {df['Birth Year'].mode()}")
    else:
        print("Sorry, there's no Birth Year information for selected city.")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df, fiveline):
    display = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
    if display == 'yes':
        print(df.iloc[fiveline:fiveline+5])
        fiveline += 5
        return display_data(df, fiveline)
    if display == 'no':
        return
    else:
        print("\nI'm sorry, I'm not sure if you wanted to see more data or not. Let's try again.")
        return display_data(df, fiveline)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df,0)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
