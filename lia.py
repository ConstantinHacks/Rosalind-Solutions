import math
import numpy as np # np is an alias pointing to numpy, but at this point numpy is not linked to numpy.f2py

n = 19 # AT LEAST
K = 6 # GENERATION

numOffspringInGenK = 2 ** K

prob = .25 ** K

probAtLeastN = 0

def binomialProb(numAaBb,n):
    return (math.factorial(n)/(math.factorial(numAaBb)*math.factorial(n-numAaBb)))*(.25**numAaBb)*(1-.25)**(n-numAaBb)

for num in range(n,numOffspringInGenK+1):
    probAtLeastN += binomialProb(num,numOffspringInGenK)

print("Final Answer: {}".format(round((probAtLeastN), 3)))