from allele import Allele
from math import pow, floor, sqrt
from random import randrange, normalvariate

class Wolf(object):
    def __init__(self, alleles, can_mate=False):
        # A wolf should have 5 alleles [1]
        if len(alleles) > 5:
            raise ValueError("Too many alleles specified")
        self.alleles = alleles
        self.age = 0
        # Average life span is 6-8 years [5]
        self.lifespan = floor(normalvariate(7, 1)) 
        self.can_mate = can_mate

    # Note: max variance is 2
    def genetic_variance(self):
        num_alleles = len(self.alleles)
        mean = sum(self.alleles[i].allele for i in 
            range(0, num_alleles))/num_alleles
        var = sum(pow(self.alleles[i].allele-mean,2) for i in
            range(0, num_alleles))/num_alleles
        return var


    def genetic_std_dev(self):
        return sqrt(self.genetic_variance())
 
def generate_random_wolf(can_mate=False):
    alleles = [Allele(randrange(1,5)) for i in range(0,5)]
    return Wolf(alleles, can_mate)

