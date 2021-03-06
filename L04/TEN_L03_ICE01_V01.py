#init
terminate = False
#program greeting
print("This program will display a calendar month between 1800 and 2099")

while not terminate:
    #get month and year
    month = int(input("Enter month 1-12 (-1 to quit):"))

    if month == -1:
        terminate = True;
    else:
        while month < 1 or month > 12:
            month = int(input("INVALID - Enter month (1-12):"))

        year = int(input("Enter year (YYYY): "))

        while year < 1800 or year > 2099:
            year = int(input("INVALID - Enter year (1800-2099): "))

        #determine if leap year
        if(year%4 == 0) and (not(year%100 == 0)) or (year%400 == 0)):
            leap_year = True
        else:
            leap_year = False

        #determine num of days in month
            if month in (1,3,5,7,8,10,12):
                num_days_in_month = 31
            elif month in (4,6,9,11):
                num_days_in_month = 30
            elif leap_year:
                num_days_in_month = 29
            else:
                num_days_in_month = 28

            #determine days of the week
            century_digits = year // 100
            year_digits = year % 100

            value = year_digits + (year_digits // 4)

            if century_digits == 18:
                value = value + 2
            elif century_digits == 20:
                value = value + 6

            if month == 1 and not leap_year:
                value = value + 1
            elif month == 2:
                if leap_year:
                    value = value + 3
                else:
                    value = value + 4
            elif month == 3 or month == 11:
                value = value + 4
            elif month == 5:
                value = value + 2
            elif month == 6:
                value = value + 5
            elif month == 8:
                value = value + 3
            elif month == 9 or month == 12:
                value = value + 6
            elif month == 10:
                value = value + 1

            day_of_week = (value + 1) % 7 #sun-Saturday
            #determine month name
            if month == 1:
                month_name = 'January'
            elif month == 2:
                month_name = 'Februrary'
            elif month == 3:
                month_name = 'March'
            elif month == 4:
                month_name = 'April'
            elif month == 5:
                month_name = 'May'
            elif month == 6:
                month_name = 'June'
            elif month == 7:
                month_name = 'July'
            elif month == 8:
                month_name = 'August'
            elif month == 9:
                month_name = 'September'
            elif month == 10:
                month_name = 'October'
            elif month == 11:
                month_name = 'November'
            else:
                month_name = 'December'
