import sys

class chear:
    def __init__(self,chear_company,chear_size,chear_colour,chear_price):
        self.company = chear_company
        self.size = chear_size
        self.colour = chear_colour
        self.price = chear_price
    
def main():
    T = chear("A_one", "Midiam", "black", 1200)
    print(T.__dict__)

main()

