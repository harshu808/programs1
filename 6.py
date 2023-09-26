# Write a Python program to count the number 4 in a given list.

def num_count(num):
    count = 0
    for i in num:
        if i == 4:
            count += 1
    return count


num = [2, 4, 5, 6, 4, 4]
count2 = num_count(num)
print(count2)
