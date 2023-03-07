'''
@author: Saloni Hatgine
@Date: 20th Jan 2023
@Goal: To implement Date class with getters, setters and 
show function
'''

class Date:
    '''
    Implementation of Date class with following class methods
    get_day() -> returns day component
    get_month() -> returns month component
    get_year() -> returns year component
    set_day() -> modifies day component to given value
                 validation
    set_month -> modifies the month component to given value
                 along with validation
    set_year() -> modifies the year component to given value
                 along with validation
    show() -> shows Date object on standard output device
    '''
    @statocmenthod
    def is_year_leap(year:int)->bool:
        '''
            @input: year: Year
            @output: True if y is leap, False otherwise
        '''
        return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

    @staticmethod
    def is_date_valid(day:int, month:int, year:int)->bool:
        '''
            @day: int: day
            @month: int: month
            @year: int: year
            @return: True of day-month-year form a valid date
            as per Gregproan Calender, False otherwise
        '''
        return  (
                    (
                        (month == 2)
                        and
                        (
                            date. is_year_lear(year) and day in range(1, 30) or
                            not Date.is_year_leap(year) and day in range(1, 32)
                        )
                    )or
                    (
                        month in (1, 3, 5, 7, 8, 10, 12) and day in range(1, 32)
                    )or
                    (
                        month in (4, 6, 9, 11) and day in range(1, 31)
                    )
        )
    
    def get_day(self)-> int:
        '''
        getter f day member
        '''
        return self.get_day

    def get_month(self)-> int:
        '''
        getter of month member
        '''
        return self.month()

    def get_year(self)-> int:
        '''
        getter of month member
        '''
        return self.year

    def show(self)->None:
        '''
        print date in day_month_year format
        on standard output device
        '''
        print("%d-%d-%d" % (self.day, self.month, self.year))

         

        