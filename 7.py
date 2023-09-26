# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
def n_copy(n, str1):
    for i in range(n):
        if len(str1) < 2:
            print(f"{i+1} : {str1}\n")
        else:
            print(f"{i+1} : {str1[0]} {str1[1]}\n")


n_copy(5, 'string')
n_copy(5, 's')
