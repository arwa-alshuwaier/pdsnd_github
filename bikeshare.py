import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all', 'january', 'february', 'march', 'april', 'may' , 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
            
    while True:
        
        city = input('would you like to see information for chicago,new york or washington? \n').lower()
        if CITY_DATA.get(city) is not None:
            break  
        else:
            print ('please choose one city name with correct spelling')
               
    

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        
            month = str(input('which month? january, February, March, April, May , June or all? \n')).lower()
            if month in months:
                break
            else:
                print ('please inter the name of the month with correct spelling')
        
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        
            day = str(input('which day? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or All? \n')).title()
           
            if day in ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday' ,'All']:
                break
            else:
                print ('please inter the name of the day with correct spelling')
        
    

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
    df= pd.read_csv( CITY_DATA[city] )
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']= df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        month = months.index(month)
        df=df[df['month'] == month]
        
    if day != 'All':
        df=df[df['day_of_week']==day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    common_month=months[common_month].title()
    print('Most common month is: ', common_month)

    # TO DO: display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print('Most common day of week is: ', common_day)

    # TO DO: display the most common start hour
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print('Most common start hour is: ', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The Common start station is :', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The Common end station is :', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('The Common combination of start & end station is: Start Station(', (df['Start Station']+') End Station('+df['End Station']+')').mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is: ',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('The mean travel time is: ',df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The counts of user types: \n', df['User Type'].value_counts(),'\n')
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns :
        print('The counts of gender: \n', df['Gender'].value_counts(),'\n')
    else:
        print('There are no Gender and year of birth stats in washington')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns :
        print('The earliest year of birth is: \"', int(df['Birth Year'].min()),'\" ')
        print('The most recent is: \"',  int(df['Birth Year'].max()),'\"')
        print('The common is: \"', int(df['Birth Year'].mode()[0]),'\"')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def load_info(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
   
    if view_data == 'yes':
        start_loc = 0
        
        while (start_loc <= len(df.index)):
            print(len(df.index))
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input("Do you wish to continue?: Enter yes or no\n ").lower()
            if (view_display == 'no'):
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        load_info(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            exit1=input ('\nAre you sure you want to exit? Enter yes or no\n')
            if exit1.lower() == 'yes':
                break
            
        


if __name__ == "__main__":
	main()
