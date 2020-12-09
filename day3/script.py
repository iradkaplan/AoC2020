import math

with open("input-3.txt") as f:
    content = [i.strip() for i in f.readlines()]

# print(content)

width = len(content[0])



h_moves_array = [1, 3, 5, 7, 1]
v_moves_array = [1, 1, 1, 1, 2]
tree_array = []

for (index, h) in enumerate(h_moves_array):
    h_index = 0
    v_index = 0
    print(h)
    print(index)
    h_moves = h
    v_moves = v_moves_array[index]

    trees = 0

    while (v_index < len(content)):
        if(content[v_index][h_index] == '#'):
            trees += 1
        h_index = (h_index + h_moves) % width
        v_index += v_moves


    print(trees)
    tree_array.append(trees)
print(len(content))
print(width)

print(tree_array)

product = math.prod(tree_array)
print(product)