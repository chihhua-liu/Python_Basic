#demo54

import csv

sampleFile1 = open('data/demo54.csv')
sampleReader = csv.reader(sampleFile1)
sampleData = list(sampleReader)
sampleFile1.close()
print(type(sampleData))
for r in sampleData:
    print("get a row", [col for col in r])