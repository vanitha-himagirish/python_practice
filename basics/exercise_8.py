# Given two list of numbers, write a program to create a new list
# such that the new list should contain odd numbers from the first list 
# and even numbers from the second list.
def create_lst(lst1,lst2): 
   res=[]
   for i in lst1:
       if (i%2!=0):
           res.append(i)
   for i in lst2:
       if (i%2==0):
        res.append(i)
   print(res)       
    
a=[10, 20, 25, 30, 35]
b=[40, 45, 60, 75, 90]
create_lst(a,b)
