
# For Loop
n = 4
for i in range(0, n): # [0,1,2,3]
    print(i)

# Iterating by Index of Sequences
a = ["geeks", "for", "geeks"]
for idx in range(len(a)):
    print(a[idx])


# While Loop
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")


# Nested Loops
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()