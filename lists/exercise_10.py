# Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. 
# Only update the first occurrence of an item.

list1 = [5, 20, 15, 20, 25, 50, 20]
for i in list1:
    if (i==20):
        ind=list1.index(i)
        list1[ind]=200
print(list1)
