import sys

class book:
    def __init__(self,language,size,name,verssion,author):
        self.languageage = language
        self.size = size
        self.name = name
        self.verssion = verssion
        self.author = author

def main():
    B = book("marathi", "midiam", "sanegurugi", 2000, "sanegurugi")
    print(B.__dict__)

main()

n =10
m= n 