import re

regexDNA = "[CTGA]+"

regexLabel = "[\w]+[\d]{4}"

file = open("input.txt", "r")

input = file.read().replace("\r","")
input = input.replace("\n","")

labels = re.findall(regexLabel, input)
dna = re.findall(regexDNA, input)

dnaDict = dict(zip(labels,dna))

highestPercent = 0
highestLabel = ""

for label,dna in dnaDict.iteritems():
    gcCount = dna.count("G") + dna.count("C")
    percentGC = round(1.0* gcCount/len(dna)*100,6)
    if(percentGC > highestPercent):
        highestPercent = percentGC
        highestLabel = label
    

    
print("{}\n{}").format(highestLabel,highestPercent)


