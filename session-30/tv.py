import sys

class tv:
    def __init__(self,tv_company,tv_size,tv_price,tv_LCD):
        self.company = tv_company
        self.size = tv_size
        self.price = tv_price
        self.LCD = tv_LCD

def main():
    T = tv("samsung", "15ench", 20000, "Yes")
    print(T.__dict__)

main()



