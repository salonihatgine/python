import sys

class headphone:
    def __init__(self,H_company,H_size,H_price,H_colour,H_vayrless):
        self.company = H_company
        self.size = H_size
        self.price = H_price
        self.colour = H_colour
        self.vayrless = H_vayrless

def main():
        V = headphone("sony", "L", 5000, "Red", "Yes")
        print(V.__dict__)

main()