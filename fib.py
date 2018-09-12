n, k = 30,4

rabbits = [1]

for num in range(1,n):
    toAdd = 0
    if num == 1:
        toAdd = 1
    else:
        toAdd = rabbits[num-2]*k + rabbits[num-1]
    
    rabbits.append(toAdd)

print(rabbits[-1])