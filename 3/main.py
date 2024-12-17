import re

PATTERN = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

with open("data.txt", "r") as file:
    content = file.read()

matches = re.findall(PATTERN, content)

sum = 0
enabled_sum = 0
flag = True

for match in matches:
    if match != "do()" and match != "don't()":#
        x, y = map(int, match[4:-1].split(','))
        sum += x * y

for match in matches:
    if match == "do()":
        flag = True
    elif match == "don't()":
        flag = False
    else:
        if flag:
            x, y = map(int, match[4:-1].split(","))
            enabled_sum += x * y

print("The corrupted sum is", sum)
print("The corrupted enabled sum is", enabled_sum)