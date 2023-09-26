# Write a Python program that checks whether a specified value is contained within a group of values.

n1 = [1, 3, 4, 5]
n2 = [2, 4, 6, 7, 8]


def check_value(n1, n2, n):
    if (n in n1) or (n in n2):
        return True
    else:
        return False


see = check_value(n1, n2, 1)
print(see)
