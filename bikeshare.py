import time
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Would you like to see data for Chicago, New York, or Washington?').lower()
    while city not in CITY_DATA:
        print('please enter Chicago, New York, or Washington')
        city=input('Would you like to see data for Chicago, New York, or Washington?').lower()
    Filters=['month','day','both']
    filters=input('Would you like to filter data by month ,day or both?').lower()
    while filters not in Filters:
        print('\enter day or month or both\n')
        filters=input('Would you like to filter data by month ,day or both?').lower()

    months =['all','january','february','march','april','may','june','july','august','september','october','november','december']
    days=['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    if filters =='month':
    # get user input for month (all, january, february, ... , june)
        month=input('\nWhat month do u like to filter the data by? pls enter all, january, february:\n').lower()
        while month not in months:
            month=input('\nWhat month do u like to filter the data by? pls enter all, january, february:\n').lower()
        day='none'
    if filters =='day':
    # get user input for day of week (all, monday, tuesday, ... sunday)
        day=input('\nWhat day do u like to filter the data by? pls enter all,monday, tuesday,sunday:\n').lower()
        while day not in days:
             day=input('\nWhat day do u like to filter the data by? pls enter all,monday,tuesday,sunday:\n').lower()
        month='none'
    if filters =='both':
       month=input('\nWhat month do u like to filter the data by? pls enter all, january, february:\n').lower()
       while month not in months:
             month=input('\nWhat month do u like to filter the data by? pls enter all, january, february:\n').lower()

       day=input('\nWhat day do u like to filter the data by? pls enter all,monday,tuesday,sunday:\n').lower()
       while day not in days:
             day=input('\nWhat day do u like to filter the data by? pls enter all,monday,tuesday,sunday:\n').lower()

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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all' and month != 'none':
        # use the index of the months list to get the corresponding int
        months =['january','february','march','april','may','june','july','august','september','october','november','december']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    elif month == 'none':
        df.drop('month',inplace=True,axis=1)   
    # filter by day of week if applicable
    if day != 'all' and day!='none':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]        
    elif day == 'none':
        df.drop('day_of_week',inplace=True,axis=1)
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    df
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if 'month' in df.columns:
    # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        popular_month = df['month'].mode().values[0]
        print('Most Frequent  month:', popular_month)
    if 'day_of_week' in df.columns:   
    # display the most common day of week
        df['day_of_week'] = df['Start Time'].dt.day_name()
        popular_day = df['day_of_week'].mode().values[0]
        print('\nMost Frequent day:', popular_day)
    # extract hour from the Start Time column to create an hour column
    df['hour'] =df['Start Time'].dt.hour
    # display the most common start hour
    popular_hour = df['hour'].mode().values[0]
    print('\nMost Frequent Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode().values[0]
    print('\nMost Frequent Start Station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode().values[0]
    print('\nMost Frequent End Station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    frequent_combination=df[['Start Station', 'End Station']].mode().loc[0]
    print('\nMost frequent combination of start station and end station trip:{},{}'.format(frequent_combination[0],frequent_combination[1]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    total=df['Trip Duration'].sum()
    print('\n Total Trip Duration...\n',total)

    # display mean travel time
    avg=df['Trip Duration'].mean()
    print('\n Average Trip Duration...\n',avg)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # print value counts for each user type
    user_types = df['User Type'].value_counts()
        
    print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        user_Gender = df['Gender'].value_counts()
        print(user_Gender)
    else:
        print('No gender data to share')
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode().values[0]
        print('\nthe earliest year of birth is : ',earliest_year)
        print('\nthe most recent year of birth is : ',most_recent_year)
        print('\nthe most common year of birth is : ',most_common_year)
        print("\nThis took %s seconds." % (time.time() - start_time))
    else:
        print('No birth year data to share')     
    
    print('-'*40)

def view_users(city):
    df = pd.read_csv(CITY_DATA[city])

    userdata=input('\nwould u like to see some individuals data?Enter yes or no\n').lower()
    while userdata not in ['yes','no']:
           userdata=input('\nwould u like to see some individuals data?Enter yes or no\n').lower()
    i=0
    
    df = df.rename(columns = {"Unnamed: 0":"User Number"}) 
    while userdata =='yes':
            j=i+5
            print(df[i:j])
            
            userdata=input('\nWould u like to see some individuals data?Enter yes or no\n').lower()
            while userdata not in ['yes','no']:
                userdata=input('\nWould u like to see some individuals data?Enter yes or no\n').lower()
            i+=5   
    
def main():
    while True:

        
        city, month, day = get_filters()
        df = load_data(city, month, day)
        timeshow=input('\nWould you like to show times of travel stats?Enter yes or no.\n').lower()
        while timeshow not in ['yes','no']:
            timeshow=input('\nWould you like to show times of travel stats?Enter yes or no.\n').lower()
        if timeshow.lower() == 'yes':
            time_stats(df)
            
        stationshow=input('\nWould you like to show stistics on the most popular stations and trip?Enter yes or no.\n').lower()
        while stationshow not in ['yes','no']:
            stationshow=input('\nWould you like to show stistics on the most popular stations and trip?Enter yes or no.\n').lower()
        if stationshow.lower() == 'yes':
            station_stats(df)
            
        tripshow=input('\nWould you like to show stistics on trips duration?Enter yes or no.\n').lower()
        while tripshow not in ['yes','no']:
            tripshow=input('\nWould you like to show stistics on trips duration?Enter yes or no.\n').lower()
        if tripshow.lower() == 'yes':
            trip_duration_stats(df)
            
        usershow=input('\nWould you like to show users breakbown?Enter yes or no.\n').lower()
        while usershow not in ['yes','no']:
            usershow=input('\nWould you like to show users breakbown?Enter yes or no.\n').lower()
        if usershow.lower() == 'yes':
            user_stats(df)
        view_users(city)    
        restart = input('\nwould you like to restart ? Enter yes or no.\n').lower()
        while restart not in ['yes','no']:
            restart = input('\nwould you like to restart ? Enter yes or no.\n').lower()
        if restart.lower() == 'no':
            break
        



if __name__ == "__main__":
	main()
