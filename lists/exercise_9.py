# Replace list’s item with new value if found
# Given a Python list, write a program to remove all occurrences of item 20.

list1 = [5, 20, 15, 20, 25, 50, 20]
for i in list1:
    if (i==20):
        list1.remove(i)
print(list1)
