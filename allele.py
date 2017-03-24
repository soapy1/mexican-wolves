# An allele is a number between 1 and 5
class Allele(object):
    def __init__(self, allele):
        if  allele not in [1,2,3,4,5]:
            raise ValueError("The allele should be between 1 and 5")
        self.allele = allele

