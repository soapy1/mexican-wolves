from wolf import Wolf
from allele import Allele
from pack import Pack
from random import randrange

def generate_random_wolf():
    alleles = [Allele(randrange(1,5)) for i in range(0,5)]
    return Wolf(alleles)

def generate_pack(num_wolves):
    return Pack([generate_random_wolf() for i in range(0,num_wolves)])

