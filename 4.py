# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.


def string_copy(n, str1):

    for i in range(n):
        print(f"{i} : {str1}\n")


out = string_copy(5, "say")
