left = []
right = []
with open("data.txt", "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        left.append(num1)
        right.append(num2)

dist = sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))
print("The distance between the 2 lists is", dist)

sim = 0

for num in left:
    count_in_right = right.count(num)
    sim += num * count_in_right

print("The similarity score between the left and the right lists is", sim)