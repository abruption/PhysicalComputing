# Loop
lists = list()
for i in range(1, 101):
    if i % 2 ==0:
        lists.append(i)
print(lists)

# List Comprehension 1
print([x*2 for x in range(1, 51)])

# List Comprehension 2
print([j for j in range(1, 101) if j % 2 == 0])