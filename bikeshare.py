import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['jan','feb','mar','april','may','june']

def validate_inputs():
    """
    Asks user to specify a city, month, and day then validates they are 3 inputs to meet the project reqiurements.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        user_input = input("Please enter with the same order sperarating them with a ',' \n 1) a city from (chicago, new york city , washington) \n then enter time frame:\n      2)month from (jan to june) \n      3)specific day     \n or all , all for all months and all days period analysis: \n")
        if "," in user_input:
            parametrs = user_input.split(",")
            if len(parametrs) > 3:
                print("Please use the input directions above to be valid inputs")
                continue
            elif len(parametrs) < 3:
                print("you have missing input/n Please use the input directions above to be valid inputs")
                continue
            else:
                city = parametrs[0].strip().lower()
                month = parametrs[1].strip().lower()
                day = parametrs[2].strip().lower()
                city , month , day = validate_names(city,month,day)
                break
        else:
            city = user_input.strip().lower()
            month = input("please enter month name from (jan,feb,mar,april,may,june) or all for whole duration analysis:\n").strip().lower()
            day = input("please enter day name from (saturday,sunday,monday,tuesday,wedensday,thursday,friday) or all for all days").strip().lower()
            city , month , day = validate_names(city,month,day)
            break

    return city,month,day

def validate_names(city,month,day):
    """
    validate user inputs (city, month, and day) to be as expected names with no typos.
    """
    while city not in CITY_DATA:
        city = input("please enter correct city name from (chicago, new york city , washington)").lower()
    while month not in ['all','jan','feb','mar','april','may','june']:
            month = input("please enter correct month name from (jan,feb,mar,april,may,june) or all for the all period analysis").lower()
    while day not in ['all','saturday','sunday','monday','tuesday','wedensday','thursday','friday']:
        day = input("please enter valid day name (saturday,sunday,monday,tuesday,wedensday,thursday,friday) or all for all days").lower()
    print('-'*40)  
    return city , month , day

#replaced thie function with two functions one for accepts user inputs and the other to validate them
#def get_filters():
#    """
#    Asks user to specify a city, month, and day to analyze.
#
#    Returns:
#        (str) city - name of the city to analyze
#        (str) month - name of the month to filter by, or "all" to apply no month filter
#        (str) day - name of the day of week to filter by, or "all" to apply no day filter
#    """
#    print('Hello! Let\'s explore some US bikeshare data!')
#    try:
#        while True:
#    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
#           city=input("please enter a city from these cities (chicago, new york city, washington): ")
#           if city not in ['chicago','new york city', 'washington']:
#                print("Please enter city exactly as one of (chicago, new york city, washington)")
#                continue
#           else:
#               break
#    # TO DO: get user input for month (all, january, february, ... , june)
#        while True:    
#            month=input("please enter month name or 'all' if you want all months: ").lower()
#            if month not in ['all','jan','feb','mar','april','may','june']:
#                print("please enter valid month name as follows (all,jan,feb,mar,april,may,june)")
#                continue
#            else:
#                break
#    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
#        while True:
#            day=input("please enter day name or all for all week days: ").lower()
#            if day not in ['all','saturday','sunday','monday','tuesday','wedensday','thursday','friday']:
#                print("please enter valid day name")
#                continue
#            else:
#                break
#    except:
#            print("Error with your inputs")
#    print('-'*40)
#    return city, month, day

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
    
    df = pd.read_csv(CITY_DATA.get(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month = months.index(month)+1
        df = df[df['month']==month]
    if day != 'all':
        df = df[df['day_of_week']==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #used idxmax() instead of mode()[0] , get that from stackoverflow..
    # TO DO: display the most common month
    print("the most common month for bikeshare is {}.".format(months[df['month'].value_counts().idxmax()-1]))

    # TO DO: display the most common day of week
    print("the most common day of week for bikeshare is {}.".format(df['day_of_week'].value_counts().idxmax()))

    # TO DO: display the most common start hour
    print("the most common hour for bikeshare is {}.".format(df['hour'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the  most commonly used start station is: {}".format(df['Start Station'].value_counts().idxmax()))

    # TO DO: display most commonly used end station
    print("the  most commonly used end station is: {}".format(df['End Station'].value_counts().idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    print("the  most commonly used start and end station is: {}".format(df.groupby(['Start Station','End Station']).size().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("the total travel time  is: {}".format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("the mean travel time is: {}".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("count of user types: \n{}".format(df['User Type'].value_counts()))
    print('-'*40)
    # TO DO: Display counts of gender
    if 'Gender' in df:
        print("count of each gender: \n{}".format(df['Gender'].value_counts()))
    else:
        print("the dataset of that city does not contain Gender column")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("the earliest year  is: {} .".format(df['Birth Year'].min()))
        print("the most recent year is: {} .".format(df['Birth Year'].max()))
        print("the most common year is: {} .".format(df['Birth Year'].value_counts().idxmax()))
    else:
        print("the dataset of that city does not contain Birth Year column")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    view_data = input("Do you want to view 5 rows of data?: ").lower()
    start_loc = 0
    while True:
        print(df.iloc[start_loc:start_loc+5])
        start_loc+=5
        view_data = input("do you want to display more 5 rows?: ").lower()
        if view_data.lower() !="yes":
            break

def main():
    while True:
        city, month, day = validate_inputs()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
