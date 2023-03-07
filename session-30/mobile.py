import sys

class mobile:
    def __init__(self,mob_company,mob_size, mob_price,mob_ram,mob_version,mob_harddisk):
        self.company = mob_company
        self.size = mob_size
        self.price = mob_price
        self.ram = mob_ram
        self.version = mob_version
        self.harddisk = mob_harddisk

def main():

    s = mobile("vivo", "5ench", 12000, "4GB","vivo-Y-15", "64GB")
    print(s.__dict__)

main()


