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
    city = 'temp'

    while city.lower() != 'chicago' and city.lower() != 'new york city' and city.lower() != 'washington':

	    city = str(input('What city would you like to analyze (please enter Chicago, New York City, or Washington? '))
    
    city = city.lower() # convert to lowercase for input as function args
    # TO DO: get user input for month (all, january, february, ... , june)
    month = 'temp'

    while month.lower() != 'all' and month.lower() != 'january' and month.lower() != 'february' and month.lower() != 'march' and month.lower() != 'april' and month.lower() != 'may' and month.lower() != 'june':

	    month = str(input('What month would you like to analyze (please enter a month between January and June, or \'All\' if you do not wish to filter)? '))
    
    month = month.lower() # convert to lowercase for input as function args
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = 'temp'

    while day.lower() != 'all' and day.lower() != 'monday' and day.lower() != 'tuesday' and day.lower() != 'wednesday' and day.lower() != 'thursday' and day.lower() != 'friday' and day.lower() != 'saturday' and day.lower() != 'sunday':

	    day = str(input('What day of the week would you like to analyze (please enter a day between Monday and Sunday, or \'All\' if you do not wish to filter)? '))
    
    day = day.lower() # convert to lowercase for input as function args
    print('-'*40) # print a spacer of dashes

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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day # get the weekday names
    
    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day = days.index(day) + 1
        df = df[df['day_of_week'] == day] # get the weekday names
    
    return df

def raw_data(df):
    """Prints 5 rows of raw data at user's request."""
    
    row_count = df.shape[0] # get the row count
    start_rows = 0
    end_rows = 5
    user_input = 'yes'
    while (user_input.lower() != 'no' and end_rows < row_count):
        user_input = str(input('Would you like to see 5 rows of raw data? Please enter yes or no: '))
        print(df.iloc[start_rows:end_rows]) # display the raw data
        start_rows += 5
        end_rows += 5

def time_stats(df,months,days): # changed this function to display the month and weekday name
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', months[common_month-1].capitalize()) # display the actual name of the month
    # TO DO: display the most common day of week
    common_dow = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', days[common_dow-1].capitalize()) # display the actual name of the weekday

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    if (common_hour % 12 > 0): # formula to display AM vs PM time
        print('Most Common Start Hour: {} PM'.format(common_hour % 12))
    else:
        print('Most Common Start Hour: {} AM'.format(common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_sstation = df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_sstation)
    # TO DO: display most commonly used end station
    common_estation = df['End Station'].mode()[0]
    print('Most Common End Station:', common_estation)
    # TO DO: display most frequent combination of start station and end station trip
    common_stations = (df['Start Station'] + ' to ' + df['End Station']).mode()[0] # concatenate the columns to get the combined mode for both columns
    print('Most Frequent Station Combination Trip:', common_stations)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total Travel Time: %.2f minutes' % (total_travel/60)) # divide by 60 to get trip time in minutes

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean Travel Time: %.2f minutes'% (mean_travel/60)) # divide by 60 to get trip time in minutes

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender
    if city == 'washington':
        print('No Gender data for Washington') # take into account missing data for Washington
    else:
        genders = df['Gender'].value_counts()
        print('Gender counts:\n', genders)

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print('No Birth Year data for Washington') # take into account missing data for Washington
    else:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print('Earliest Year of Birth:', int(earliest_year))
        print('Most Recent Year of Birth:', int(most_recent_year))
        print('Most Common Year of Birth:', int(most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        months = ['january', 'february', 'march', 'april', 'may', 'june'] # list used to display the month name
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday'] # list used to display the weekday name
        raw_data(df) # new function to print out the raw data
        time_stats(df,months,days) # changed the function to display the month name
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()