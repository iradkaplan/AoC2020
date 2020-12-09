with open("input-3.txt") as f:
    content = [i.strip() for i in f.readlines()]

index = 0
visited_lines = []
instruction_list = []
acc = 0

print(content[0][0:3])
print(content[0][3:])
print(len(content))

while index not in visited_lines:
    visited_lines.append(index)
    line = content[index]
    instruction_list.append(line)

    if (line[0:3] == 'nop'):
        index += 1
        # continue
    elif (line[0:3] == 'acc'):
        acc += int(line[3:])
        index += 1
    else:  # jmp
        index += int(line[3:])

print(acc)
print(index)
# print(visited_lines)
# print(instruction_list)

for instruction in visited_lines:
    visited_lines2 = []
    index = 0
    acc = 0

    while index not in visited_lines2:
        visited_lines2.append(index)

        if index == 622:
            print("success!")
            print(acc)
            break

        line = content[index]
        # instruction_list.append(line)

        if index == instruction:
            if (line[0:3] == 'nop'):
                index += int(line[3:])
            else:  # jmp
                index += 1
        else:

            if (line[0:3] == 'nop'):
                index += 1
                # continue
            elif (line[0:3] == 'acc'):
                acc += int(line[3:])
                index += 1
            else:  # jmp
                index += int(line[3:])