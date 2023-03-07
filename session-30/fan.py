import sys

class fan:
    def __init__(self,fan_company,fan_size,fan_price,fan_colour):
        self.company = fan_company
        self.size = fan_size
        self.price = fan_price
        self.colour = fan_colour

def main():
        G = fan("cromptan", "midiam", 10000, "pink")
        print(G.__dict__)

main()
    