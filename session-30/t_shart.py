import sys

class t_shart:
    def __init__(self,t_company,t_size,t_price,t_colour):
        self.company = t_company
        self.size = t_size
        self.price = t_price
        self.colour = t_colour

def main():
    K = t_shart("Linenking", 40, 1000, "blue")
    print(K.__dict__)

main()

