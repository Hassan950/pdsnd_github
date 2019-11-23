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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Enter City "Chicago", "New York City", "Washington": ').lower()
        if city in CITY_DATA.keys():
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter month to filter by month 'january', 'february', 'march', 'april', 'may', 'june'\nor 'all' for no filter: ").lower()
        if month.lower() in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter month to filter by month 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'\nor 'all' for no filter: ").lower()
        if day.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    m = df['Start Time'].dt.month.mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('Most common Month', months[m - 1])

    # TO DO: display the most common day of week
    d = df['Start Time'].dt.weekday_name.mode()[0]
    print('\nMost common Day', d)

    # TO DO: display the most common start hour
    h = df['Start Time'].dt.hour.mode()[0]
    print('\nMost common Hour', h)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    startst = df['Start Station'].mode()[0]
    print('Most common Start Station', startst)

    # TO DO: display most commonly used end station
    endst = df['End Station'].mode()[0]
    print('\nMost common End Station', endst)

    # TO DO: display most frequent combination of start station and end station trip
    df['st_concat'] = pd.concat([df['Start Station'], df['End Station']], ignore_index = True)
    st = df['st_concat'].mode()[0]
    print('\nMost common Station', st)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time:", df["Trip Duration"].sum())

    # TO DO: display mean travel time
    print("\nTotal travel time:", df["Trip Duration"].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of User Type")
    print(df["User Type"].value_counts())

    # TO DO: Display counts of gender
    print("\ncounts of gender")
    print(df["Gender"].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    print("\nearliest year of birth")
    print(df["Birth Year"].min())
    
    print("\nmost recent year of birth")
    print(df["Birth Year"].max())
    
    print("\nmost common year of birth")
    print(df["Birth Year"].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
