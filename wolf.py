from allele import Allele
from math import pow

class Wolf(object):
    def __init__(self, alleles):
        # A wolf should have 5 alleles [1]
        if len(alleles) > 5:
            raise ValueError("Too many alleles specified")
        self.alleles = alleles

    def genetic_variability(self):
        return pow(sum(
            pow(self.alleles[i].allele,2) for i in 
            range(0, len(self.alleles))), 0.5
        )
    
