from anytree import LevelOrderIter, Node, PreOrderIter, RenderTree
import re

with open("input-3.txt") as f:
    content = [i.strip() for i in f.readlines()]


def first_two_words(words):
    return ' '.join(words.split()[:2])

def build_list(start):
    end = start.copy()

    if len(start) == 0:
        for j in content:
            if j.find('shiny gold', 3) != -1:
                if not first_two_words(j) in end:
                    end.append(first_two_words(j))

    for i in end:
        for j in content:
            if j.find(i, 3) != -1:
                if not first_two_words(j) in end:
                    end.append(first_two_words(j))
    if (len(end) == len(start)):
        return end
    else:
        return build_list(end)

listy = build_list([])
# print(listy)

# y = Node("test")
# w = Node("test1", parent=y)
# z = Node("test1", parent=y)
# x = Node("test2", parent=y)
#
# for pre, fill, node in RenderTree(y):
#     print("%s%s" % (pre, node.name))
# print(y.children)

# print(first_two_words(content[0]))
print(len(content))
print(len(listy))

p = re.compile(r"\d\W\w+\W\w+\Wbag")

matches = p.findall(content[0])
print(matches)

root = Node('shiny gold')
for node in LevelOrderIter(root):
    # node = root
    for line in content:
        if first_two_words(line) == first_two_words(node.name):
            if line.find('no other bags') == -1:
                matches = p.findall(line)
                for match in matches:
                    words = match.split()
                    # print(words)
                    for i in range(0, int(words[0])):
                        a = Node(" ".join(words[1:3]) + " " + f"{i}", parent=node)

for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))

for i in range(0,2):
    print(i)

print(len(root.descendants))