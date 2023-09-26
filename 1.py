# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

def numbers(num):
    seen = set()
    for i in range(0, num):
        if i in seen:
            print(f"{i} is duplicate number.")
        else:
            seen.add(i)
            print(f"{i} is unique numbers.")
    return seen


a = numbers(10)
print(f"unique number is {a}")
