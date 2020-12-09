import re

with open("input-3.txt") as f:
    content = f.read()

p = re.compile(r"\n\n")

content = [i.strip() for i in p.split(content)]

content = [i.replace("\n", "") for i in content]

content = ["".join(list(dict.fromkeys(i))) for i in content]  # dedupe

lengths = [len(i) for i in content]

print(sum(lengths))

# part 2

with open("input-3.txt") as f:
    content = f.read()

content = [i.strip() for i in p.split(content)]

p = re.compile(r"\n")

content = [p.split(i) for i in content]
intersects = []
# print(content)
for test in content:


    # test = content[0]
    test = [set(i) for i in test]
    # print(q)
    intersects.append(test[0].intersection(*test))
    # print(test[0].intersection(*test))
    # print(test)

intersects = [len(i) for i in intersects]

print(sum(intersects))