with open("input-3.txt") as f:
    content = [int(i.strip()) for i in f.readlines()]

for i, v in enumerate(content):
    if i < 25:
        continue
    candidates = content[i - 25:i]
    match = False
    for j, value in enumerate(candidates):
        for k in range(j + 1, 25):
            if candidates[k] + value == v:
                match = True
                break
        if match is True:
            break
    if match is False:
        print(i)
        print(v)
        goal = v
        break

i = 0
j = 1

while sum(content[i:j]) != goal:
    if (sum(content[i:j]) > goal) or (j == len(content) - j):
        i += 1
        j = i + 1
    else:
        j += 1

sequence = content[i:j]
sequence.sort()
print(sequence)
print(sequence[0] + sequence[len(sequence) - 1])
