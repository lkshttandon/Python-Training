for i in range(0, 4):
    print("* " * i)
print()
for i in range(3, -1, -1):
    print("* " * i)

k = -1
for i in range(3, -1, -1):
    for j in range(k, -1, -1):
        print(end=" ")
    k = k + 2
    for j in range(0, i):
        print("* ", end="")
    print()

k = 4
for i in range(0, 3):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print()

print()
k = 4
for i in range(0, 3):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i+1):
        print("* ", end="")
    print()

