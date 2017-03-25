from allele import Allele
from math import pow
from random import randrange, normalvariate

class Wolf(object):
    def __init__(self, alleles):
        # A wolf should have 5 alleles [1]
        if len(alleles) > 5:
            raise ValueError("Too many alleles specified")
        self.alleles = alleles
        self.age = 0
        # Average life span is 6-8 years [5]
        self.lifespan = normalvariate(7, 1) 

    def genetic_variability(self):
        return pow(sum(
            pow(self.alleles[i].allele,2) for i in 
            range(0, len(self.alleles))), 0.5
        )
   
def generate_random_wolf():
    alleles = [Allele(randrange(1,5)) for i in range(0,5)]
    return Wolf(alleles)
 
