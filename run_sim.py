from pack import Pack, generate_pack
from random import normalvariate

def main():
    # Pack sizes for gray wolves range from about 2 to 8 members [4]
    packs = [generate_pack(normalvariate(5,3)) for i in range(0,3)]

if __name__=='__main__':
    main()

