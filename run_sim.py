from pack import Pack, generate_pack
from random import normalvariate
from math import ceil

def main():
    # start simulation at year 0
    year = 0
    # Pack sizes for gray wolves range from about 2 to 8 members [4]
    packs = [generate_pack(ceil(normalvariate(5,3))) for i in range(0,3)]
    
    for i in range(0,50):
        year += 1;
        for p in packs:
            p.age()
            p.mate()
            p.deaths()


def ages_lsp(p):
    alsp = [{'age': p.wolves[i].age, 'lsp': p.wolves[i].lifespan} for i in range(0,len(p.wolves))] 
    return alsp


if __name__=='__main__':
    main()

