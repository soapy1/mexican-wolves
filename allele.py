class Allele(object):
    def __init__(self, allele):
        # An allele is a number between 1 and 5 [1]
        if  allele not in [1,2,3,4,5]:
            raise ValueError("The allele should be between 1 and 5")
        self.allele = allele

