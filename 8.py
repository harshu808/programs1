# Write a Python program to test whether a passed letter is a vowel or not.

def vowels(n, str1):
    if n in str1:
        print(f"{n} one of vowel")
    else:
        print(f"{n} is not a vowel")


str1 = ['a', 'e', 'i', 'o', 'u']
vowels('c', str1)
