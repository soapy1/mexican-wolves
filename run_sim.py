from pack import Pack, generate_pack
from random import normalvariate
from math import ceil

def main():
    # start simulation at year 0
    year = 0
    # Pack sizes for gray wolves range from about 2 to 8 members [4]
    packs = [generate_pack(ceil(normalvariate(5,3))) for i in range(0,3)]
     
    for i in range(0,5):
        year += 1;
        next_iter_packs = []
        for p in packs:
            p.age()
            p.mate()
            p.deaths()
            if len(p.wolves) > 8:
                next_iter_packs.extend(split_pack(p))
            else:
                next_iter_packs.append(p)
        packs = next_iter_packs

    print("pack sizes: ", [len(p.wolves) for p in packs])
    print("genetic variances: ", [p.average_genetic_variance() for p in packs])
    print("number packs: ", len(packs))

def split_pack(p):
    len_new_pack = ceil(len(p.wolves)/2)
    new_packs = [Pack(p.wolves[0:len_new_pack]), Pack(p.wolves[len_new_pack:len(p.wolves)])]
#    if len(new_packs[0].wolves) > len_new_pack:
#        pa = new_packs.pop(new_packs[0])
#        new_packs.extend(pa)
#    if len(new_packs[1].wolves) > len_new_pack:
#        pa = new_packs.pop(new_packs[1])
#        new_packs.extend(pa)
    for np in new_packs:
        np.ensure_two_mating_wolves()
    return new_packs


def ages_lsp(p):
    alsp = [{'age': p.wolves[i].age, 'lsp': p.wolves[i].lifespan} for i in range(0,len(p.wolves))] 
    return alsp


if __name__=='__main__':
    main()

