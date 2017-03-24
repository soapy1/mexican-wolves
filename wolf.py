# A Wolf should have 5 alleles

from allele import Allele

class Wolf(object):
    def __init__(self, alleles):
        if len(alleles) > 5:
            raise ValueError("Too many alleles specified")
        self.alleles = alleles
    
