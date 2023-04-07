

class Test:
    def __init__(self):
        print("In Test.__init__")

t = Test()
print("t.__dict__:", t.__dict__)

class Test:
    def __init__(self):
        self.a = 100
        self.b = 200
        self.c = 300
        
t = Test()
print(t.__dict__)

class Test:
    def __init__(self, init_a, init_b, init_c):
        self.a = init_a
        self.b = init_b
        self.c = init_c

t = Test(100, 200, 300)

class Date:
    def __init__(self, init_day, init_month, init_year):
        self.day = init_day
        self.month = init_month
        self.year = init_year

    def get_day(self):
        return self.day

    def set_day(self, new_day):
        self.day = new_day
