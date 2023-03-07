class Date:
    def __init__(self, init_day, init_month, init_year):
        self.day = init_day
        self.month = init_month
        self.init_year = init_year

    def get_day(self):
        return self.day

    def set_day(self, new_day):
        self.day = new_day

def main():                     
    D = Date(31, 1, 2023)                  # STEP IN
    dd = D.get_day()    # Date.get_day(D)  # STEP IN
    print("dd=", dd)                       # STEP OVER
    D.set_day(24)   # Date.set_day(D, 24)  # STEP IN
    dd = D.get_day()                       # STEP IN
    print("dd=", dd)                       # STEP OVER

main()


