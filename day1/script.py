with open("input.txt") as f:    
    content = [int(i.strip()) for i in f.readlines()]

print("part 1")
index1=0
index2=1
input1=content[index1]
input2=content[index2]
while input1 + input2 != 2020:
    if index2 != len(content) - 1:
        index2 += 1
        input2 = content[index2]
    else:
        index1 +=1
        index2 = index1+1
        input1 = content[index1]
        input2 = content[index2]


print(input1)
print(input2)
print(input1 * input2)

print("part 2")

index1=0
index2=1
index3=2
input1=content[index1]
input2=content[index2]
input3=content[index3]
while input1 + input2 + input3 != 2020:
    if index3 != len(content) - 1:
        index3 += 1
        input3 = content[index3]
    elif index2 != len(content) - 2:
        index2 += 1
        index3 = index2+1
        input2 = content[index2]
        input3 = content[index3]
    else:
        index1 +=1
        index2 = index1+1
        index3 = index2+1
        input1 = content[index1]
        input2 = content[index2]
        input3 = content[index3]

print(input1)
print(input2)
print(input3)
print(input1 * input2 * input3)