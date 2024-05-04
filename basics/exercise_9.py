# Write a Program to extract each digit from an integer in the reverse order.
def print_reverse(lst1): 
   c=str(lst1)
   res=c[::-1]
   for i in res:
       print(i)
a=234
print_reverse(a)
