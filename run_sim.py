from pack import Pack, generate_pack
from random import normalvariate
from math import ceil

def main():
    # start simulation at year 0
    year = 0
    max_population = 150
    # Pack sizes for gray wolves range from about 2 to 8 members [4]
    packs = [generate_pack(ceil(normalvariate(5,3))) for i in range(0,3)]
    time_data = [{
        'year':0,
        'stats':{
            'num_packs':len(packs),
            'wolf_pop':wolf_population(packs),
            'avg_genetic_var':wolf_pop_genetic_variance(packs)}
        }]
    for i in range(0,15):
        year += 1;
        next_iter_packs = []
        for p in packs:
            p.age()
            if wolf_population(packs) < max_population:
                p.mate()
            p.deaths()
            if len(p.wolves) > 8:
                next_iter_packs.extend(split_pack(p))
            elif len(p.wolves) > 0:
                next_iter_packs.append(p)
        packs = next_iter_packs
        time_data.append({
            'year':year,
            'stats':{
                'num_packs':len(packs),
                'wolf_pop':wolf_population(packs),
                'avg_genetic_var':wolf_pop_genetic_variance(packs)}
        })

#    print("pack sizes: ", [len(p.wolves) for p in packs])
#    print("genetic variances: ", [p.average_genetic_variance() for p in packs])
    print(time_data)
    print("number packs: ", len(packs))
    print("wolf population: ", wolf_population(packs))
    print("average variance: ", wolf_pop_genetic_variance(packs))


def split_pack(p):
    len_new_pack = ceil(len(p.wolves)/2)
    new_packs = [Pack(p.wolves[0:len_new_pack]), Pack(p.wolves[len_new_pack:len(p.wolves)])]
    for np in new_packs:
        np.ensure_two_mating_wolves()
    return new_packs


def wolf_population(packs):
    return sum(len(p.wolves) for p in packs)


def wolf_pop_genetic_variance(packs):
    return sum(p.average_genetic_variance() for p in packs)/len(packs)


def ages_lsp(p):
    alsp = [{'age': p.wolves[i].age, 'lsp': p.wolves[i].lifespan} for i in range(0,len(p.wolves))] 
    return alsp


if __name__=='__main__':
    main()

