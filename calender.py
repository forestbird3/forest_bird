DAYS_IN_MONTH = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

MONTH_STRING = [None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
WEEKDAY_STRING = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

def is_leap(year: int):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year: int, month: int):
    if month == 2 and is_leap(year):
        return 29
    return DAYS_IN_MONTH[month]


def days_before_year(year: int):
    y = year - 1
    return y*365 + y//4 - y//100 + y//400


def days_before_month(year: int, month: int):
    dbm = sum(DAYS_IN_MONTH[1:month])
    if month > 2 and is_leap(year):
        dbm += 1
    return dbm


def weekday(year: int, month: int, day: int):
    ordinal = days_before_year(year) + days_before_month(year, month) + day
    return ordinal % 7


def make_month(year: int, month: int):

    month_calendar = MONTH_STRING[month] + ' ' * 24 + '\n'
    month_calendar += ' '.join(WEEKDAY_STRING) + '\n' 

    calendar = ['-'] * 42
    dim = days_in_month(year, month) 
    offset = weekday(year, month, 1)  
    calendar[offset:offset+dim] = map(str, range(1,dim+1)) 

    for start_x in range(0, 42, 7): 
        week = calendar[start_x: start_x+7] 
        month_calendar += ' '.join(map(lambda d: '{day:>3s}'.format(day=d), week)) + '\n'

    return month_calendar.split('\n')


if __name__ == "__main__":
    year, columns = map(int, input().split())

    month_calendars = [None] + [make_month(year, m) for m in range(1, 13)]

    print('{year} calendar'.format(year=year))
    for month in range(1, 13, columns): 
        for y in range(8): 
            for x in range(month, month+columns): 
                print(month_calendars[x][y], end='     ')
            print()
        print()
        print()
        print()