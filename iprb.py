k = 24.0 #Dominant HOMO
m = 16.0 #Hetero
n = 28.0 #Recessive HOMO

population = k+m+n

domdom = (k/population)*((k-1)/(population-1))
domhet = (k/population)*(m/(population-1)) + m/population * (k/(population-1))
domrec = (k/population)*(n/(population-1)) + n/population * (k/(population-1))

hethet = (m/population)*((m-1)/(population-1))
hetrec = (m/population)*(n/(population-1)) + n/population * (m/(population-1))

total = (domdom+domhet+domrec) + hethet * .75 + hetrec * .5

print(total)