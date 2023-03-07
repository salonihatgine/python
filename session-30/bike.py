import sys

class bike:
    def __init__(self,b_company,b_model,b_colour,b_gear):
        self.company = b_company
        self.model = b_model
        self.colour = b_colour
        self.gear = b_gear

def main():
    H = bike("hero", 2022, "black", "gear")
    print(H.__dict__)

main()
