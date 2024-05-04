# Check if the first and last number of a list is the same
def print_div_five(lst):
    print("Divisible by 5:")
    for i in lst:
        if (i%5 == 0):
            print(i)
a=[10, 20, 33, 46, 55]
print_div_five(a)
