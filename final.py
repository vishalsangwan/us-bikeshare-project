# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:38:42 2018

@author: vishal sangwan
"""
import csv
import time
import datetime
## Filenames


def get_day():
    day = input("which day ?  monday write 1,  tuesday write 2 so on till 7")
    return day


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    
    return time_period



def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    # TODO: handle raw input and complete function
    if city.title() == "Chicago":
        data = "chicago"
    elif city.title() == "New York":
        data = "new_york_city"
    else:
        data = "washington"
        
    return data
    
def get_month():
    month_input_raw = input('\nWhich month? January, February, March, April, May, or June?\n')
    if month_input_raw == "january":
        month_input = "01"
    elif month_input_raw =="febuary":
        month_input = "02"
    elif month_input_raw == "march":
        month_input ="03"
    elif month_input_raw == "april":
        month_input ="04"
    elif month_input_raw == "may":
        month_input ="05"
    else:
        month_input = "06"
    return month_input
# what is the most popular month for start time

#def popular_month(file)
#file is the city for which most popular data is to be founded out
def popular_month(file):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)

        best_month_dict =  {"january": 0,"febuary": 0,"march": 0, "april":0, "may": 0,"june":0}
        most_rides = 0
        best_month = ""
        
        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            if month == "01":
                best_month_dict["january"] += 1
            elif month == "02":
                best_month_dict["febuary"] += 1
            elif month =="03":
                best_month_dict["march"] += 1
            elif month =="04":
                best_month_dict["april"] += 1
            elif month =="05":
                best_month_dict["may"] += 1
            elif month =="06":
                best_month_dict["june"] += 1
            
        
            
        for i in best_month_dict:
            while most_rides < best_month_dict[i]:
                most_rides = best_month_dict[i]
                best_month = i
    
    return best_month

 #What is the most popular hour of day for start time?
def popular_start_time(file,the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)
        best_hour_dict = {"00":0,"01":0,"02":0,"03":0,"04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,"11":0,"12":0,"13":0,"14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"20":0,"21":0,"22":0,"23":0,"24":0}
        popular_hour_count = 0
        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            hour = datetime.datetime.strftime(dt_obj, "%H")
            weekday = dt_obj.isoweekday()
            month = datetime.datetime.strftime(dt_obj, "%m")
            
            if the_month == month:
               for i in best_hour_dict:
                   if hour == i:
                       best_hour_dict[i] +=1
                 
                   if popular_hour_count < best_hour_dict[i]:
                       popular_hour_count = best_hour_dict[i]
                       most_popular_hour = i
            
            if the_month == "all":
               for i in best_hour_dict:
                   if hour == i:
                       best_hour_dict[i] +=1
                 
                   if popular_hour_count < best_hour_dict[i]:
                       popular_hour_count = best_hour_dict[i]
                       most_popular_hour = i
            
        popular_hour = most_popular_hour     
    return popular_hour
      
           
         
         
        
             

 

def duration_stats(file,the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)
    # What is the total trip duration and average trip duration?
    #file is city data
    #the_month = month_input(input from user)
    
        total_count = 0
        total_trip_duration = 0
        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            weekday = dt_obj.isoweekday()
            
            if the_month == month:
                total_count += 1
                trip = int(rows["Trip Duration"])
                
                total_trip_duration += trip
            
            elif the_month == "all":
                total_count += 1
                trip = int(rows["Trip Duration"])
                total_trip_duration += trip
                
            
                
                
    return total_trip_duration, total_count







    # What is the most popular day of week for start time?
def most_popular_day_of_week(file, the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)
        weekday_dict = {"monday":0,"tuesday":0,"wednesday":0,"thursday":0,"friday":0,"saturday":0,"sunday":0}
        popular_weekday = ""
        count = 0
        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            weekday = dt_obj.isoweekday()
            if month == the_month:
                if weekday == 1:
                    weekday_dict["monday"] += 1
                elif weekday == 2:
                    weekday_dict["tuesday"] += 1
                elif weekday == 3:
                    weekday_dict["wednesday"] += 1
                elif weekday == 4:
                    weekday_dict["thursday"] += 1
                elif weekday == 5:
                    weekday_dict["friday"] += 1
                elif weekday == 6:
                    weekday_dict["saturday"] += 1
                else:
                    weekday_dict["sunday"] += 1
            elif the_month == "all":
                if weekday == 1:
                    weekday_dict["monday"] += 1
                elif weekday == 2:
                    weekday_dict["tuesday"] += 1
                elif weekday == 3:
                    weekday_dict["wednesday"] += 1
                elif weekday == 4:
                    weekday_dict["thursday"] += 1
                elif weekday == 5:
                    weekday_dict["friday"] += 1
                elif weekday == 6:
                    weekday_dict["saturday"] += 1
                else:
                    weekday_dict["sunday"] += 1
            
                
                
        for i in weekday_dict:
                if count < weekday_dict[i]:
                    count = weekday_dict[i]
                    popular_weekday = i
                
    return popular_weekday

#city_file = get_city()
#month = get_month()
#print(most_popular_day_of_week(city_file,month))
#what is the most popular start station and end station
def most_popular_start_and_end_station(file,the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)
        start_station_dict = {}
        most_popular_start_station = ""
        most_popular_end_station = ""
        end_station_dict = {}
        start_station_count = 0
        end_station_count = 0
        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            weekday = dt_obj.isoweekday()
            start_station = rows["Start Station"]
            end_station = rows["End Station"]
            if the_month == month:
                    if end_station in end_station_dict:
                        count = end_station_dict[end_station]
                        end_station_dict[end_station] = count +1
                    else:
                        end_station_dict[end_station] = 1
                    
                    if start_station in start_station_dict:
                        count = start_station_dict[start_station]
                        start_station_dict[start_station] = count + 1
                    else:
                        start_station_dict[start_station] = 1
            elif the_month == "all":
                    if end_station in end_station_dict:
                        count = end_station_dict[end_station]
                        end_station_dict[end_station] = count +1
                    else:
                        end_station_dict[end_station] = 1
                    
                    if start_station in start_station_dict:
                        count = start_station_dict[start_station]
                        start_station_dict[start_station] = count + 1
                    else:
                        start_station_dict[start_station] = 1
            
                
                
                 
    
        for i in start_station_dict:
            if start_station_count < start_station_dict[i]:
                start_station_count = start_station_dict[i]
                most_popular_start_station = i
                
        for j in end_station_dict:
            if end_station_count < end_station_dict[j]:
                end_station_count = end_station_dict[j]
                most_popular_end_station = j
    
        
    return most_popular_start_station, most_popular_end_station
    
        
                

#print(most_popular_start_and_end_station(city_file,month))
#print(most_popular_day_of_week(city_file,month))





    


#what are the counts of each user type
def gender_count(file,the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)
        female = 0
        male = 0
        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            weekday = dt_obj.isoweekday()
            gender = rows["Gender"]
            if the_month == month:
                if gender == "Female":
                    female +=1
                elif gender == "Male":
                    male += 1
            elif the_month == "all":
                if gender == "Female":
                    female +=1
                elif gender == "Male":
                    male += 1
            
                
                
    return female, male

#print(gender_count(city_file, month_input))




#what are the counts of each user type
def user_type(file, the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)
        subscriber = 0
        customer = 0
        for rows in file:
            user = rows["User Type"]
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            weekday = dt_obj.isoweekday()
            if the_month == month:
                if user == "Subscriber":
                    subscriber += 1
                elif user == "Customer":
                    customer += 1
            elif the_month == "all":
                if user == "Subscriber":
                    subscriber += 1
                elif user == "Customer":
                    customer += 1
                
                
    return subscriber, customer


#what are the earliest(oldest), most recent(young) and most popular birth years

def birth_years(file,the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)
        birth_dict = {}
        birth_year_count = 0
        count = 0
        birth_years_list = []
        popular_years = ""
        
        
        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            weekday = dt_obj.isoweekday()
            if the_month == month:
                birth = rows["Birth Year"]
                
                if birth in birth_dict:
                    birth_year_count = birth_dict[birth]
                    birth_dict[birth] = birth_year_count + 1
                else:
                    birth_dict[birth] = 1
        
                    if birth not in birth_years_list and birth != "":
                        birth_years_list.append(birth)
            if the_month == "all":
                birth = rows["Birth Year"]
                
                if birth in birth_dict:
                    birth_year_count = birth_dict[birth]
                    birth_dict[birth] = birth_year_count + 1
                else:
                    birth_dict[birth] = 1
        
                    if birth not in birth_years_list and birth != "":
                        birth_years_list.append(birth)
        
                
                
                
        for i in birth_dict:
            if count < birth_dict[i] and i != "":
                count = birth_dict[i]
                popular_years = i
        earliest_year = min(birth_years_list)
        most_recent = max(birth_years_list)
        
    return earliest_year, most_recent, popular_years
            
def most_popular_trip(file,the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)
        count = 0
        trip_count = 0
        trip_dict = {}
        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            st_station = rows["Start Station"]
            en_station = rows["End Station"]
            trip = st_station +" -- "+ en_station
            if the_month == month:
                if trip in trip_dict:
                    count += 1
                    trip_dict[trip] = count
                else:
                    trip_dict[trip] = 1
            elif the_month == "all":
                if trip in trip_dict:
                    count += 1
                    trip_dict[trip] = count
                else:
                    trip_dict[trip] = 1
            
                
        for i in trip_dict:
            if trip_count < trip_dict[i]:
                trip_count = trip_dict[i]
                popular_trip = i
    return popular_trip

                
    



def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    if time_period == "month":
        month_input = get_month()
        day = "ads"
    elif time_period == "none":
        month_input = "all"
        day = "ads"
    elif time_period == "day":
        month_input = "ads"
        day = get_day()
        
        
    print('Calculating the first statistic...')
    start_time = time.time()

    # What is the most popular month for start time?
    if time_period == 'none':
        most_popular_month = popular_month(city) 
        print("The most popular month for start time :{}".format(most_popular_month))
        
        # TODO: call popular_month function and print the results

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        popular_day = most_popular_day_of_week(city,month_input)
        print("The most popular_day for start time:{}".format(popular_day))
        # TODO: call popular_day function and print the results
        
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_day function and print the results
    hour = popular_start_time(city,month_input)
    print("The most popular hour is:{}".format(hour))
        

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

#     What is the total trip duration and average trip duration?
 #    TODO: call trip_duration function and print the results
    trip_duration, total = duration_stats(city,month_input)
    print("The total trip duration is :{}".format(trip_duration))
    print("The total trip duration is :{}".format(trip_duration/total))
    
    

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    starting_station, ending_station = most_popular_start_and_end_station(city,month_input)
    print("The most popular start station is:{}".format(starting_station))
    print("The most popular end station is:{}".format(ending_station))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    popular_trip = most_popular_trip(city,month_input)
    print("most_popular_tripis:{}".format(popular_trip))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    subscriber, customer = user_type(city,month_input)
    print("The total customers are:{}".format(customer))
    print("The total subscriber are:{}".format(subscriber))
    

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results
    if city == "chicago" or city == "new_york_city":
        female, male = gender_count(city,month_input)
        print("total female:{}".format(female))
        print("toal male:{}".format(male))
        

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        earliest, most_recent, most_popular = birth_years(city,month_input)
        print("The earliest birth year is:{}".format(earliest))
        print("The most recent birth year is:{}".format(most_recent))
        print("The most popular birth year is:{}".format(most_popular))
    # What are the earliest, most recent, and most popular birth years?
    # TODO: call birth_years function and print the results

        print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    

     #Restart?
    restart = input('Would you like to restart? Type \'yes\' or \'no\'.')
    if restart.lower() == 'yes':
        statistics()

if __name__ == "__main__":
	statistics()
















