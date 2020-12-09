with open("input.txt") as f:
    content = [i.strip() for i in f.readlines()]

content = [s.replace('F', '0') for s in content]
content = [s.replace('B', '1') for s in content]
content = [s.replace('L', '0') for s in content]
content = [s.replace('R', '1') for s in content]

content = [int(s, 2) for s in content]
content.sort()

# print(content)

for (i, value) in enumerate(content):
    if i != value - 85:
        print(i)
        print(value)
        break

print(content[446])