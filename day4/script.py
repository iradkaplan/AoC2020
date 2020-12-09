import re
import json

with open("input-3.txt") as f:
    content = f.read()

# print(content)

p = re.compile(r"\n\n")

content = [i.strip() for i in p.split(content)]
formatted = []

for i in content:
    i = "{" + i.strip() + "}"
    i = re.sub(r"\s", ",", i)
    i = re.sub(r"(?=.{3}:)", "\"", i)  # first quote for key
    i = re.sub(r":", "\":\"", i)  # second quote for key and first quote for value
    i = re.sub(",", "\",", i)  # second quote for all values except the last
    i = re.sub("}", "\"}", i)  # second quote for the last value
    # print(i)
    i = json.loads(i)
    formatted.append(i)

print(content[0])
print(formatted[0])

required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
count = 0
for i in formatted:
    if i.keys() >= required_keys:
        count += 1
print(count)
print(len(formatted))
print(len(content))

reformatted = []
for i in formatted:
    if not i.keys() >= required_keys:
        continue
    if not 1920 <= int(i['byr']) <= 2002:
        continue
    if not 2010 <= int(i['iyr']) <= 2020:
        continue
    if not 2020 <= int(i['eyr']) <= 2030:
        continue
    hgt = re.split(r"(?=cm|in)", i["hgt"])
    if not hgt or len(hgt) < 2:
        continue
    if hgt[1] == "cm" and 150 <= int(hgt[0]) <= 193:
        print(hgt)
    elif hgt[1] == "in" and 59 <= int(hgt[0]) <= 76:
        print(hgt)
    else:
        continue
    if not len(i["hcl"]) == 7:
        continue
    if not re.match(r"\#[abcdef0123456789]{6}", i["hcl"]):
        continue
    if not i["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue
    if not len(i["pid"]) == 9:
        continue
    if not re.match(r"[0123456789]{9}", i["pid"]):
        continue
    reformatted.append(i)

print(len(reformatted))