import re

with open("input-2.txt") as f:    
    content = [i.strip() for i in f.readlines()]

# print(content)

firstline = content[0]
print(firstline)

p = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

results = []
for line in content:
    results.append(p.findall(line)[0]) 
print(results[0:4])

firstline = results[0]
print(firstline)
print(firstline[3][0])

validpws1 = 0
validpws2 = 0

for line in results:
# character = firstline[2]

    p=re.compile(line[2])
    instances = len(p.findall(line[3]))
    if(int(line[0]) <= instances <= int(line[1])):
        validpws1 += 1
    i = int(line[0])
    j = int(line[1])
    if((line[3][i-1] == line[2]) ^ (line[3][j-1] == line[2])):
        validpws2 += 1
# print(instances)
print(validpws1)
print(validpws2)