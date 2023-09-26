# Write a Python program to create a histogram from a given list of integers.

n1 = [1, 3, 4, 5, 7]


def hist1(n1):
    for i in n1:
        for j in range(i):
            print(f"*", end=" ")
        print(f"\n")


hist1(n1)
