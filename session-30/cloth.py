import sys

class cloth:
    def __init__(self,c_type,c_colour,c_price):
        self.type = c_type
        self.colour = c_colour
        self.price = c_price

def main():
    S = cloth("Saree", "pink", 1000)
    print(S.__dict__)

main()

