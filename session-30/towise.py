import sys

class towise:
    def __init__(self,t_colour,t_price,t_type,t_):
        self.colour = t_colour
        self.price = t_price
        self.type = t_type

def main():
    M = towise("green", 300, "car", "small")
    print(M.__dict__)

main()