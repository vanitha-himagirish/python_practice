# Print characters from a string that are present at an even index number
def prnt_even_char(str):
    for i in range(0,len(str)):
        if (i%2 == 0):
            print(str[i])

a="Exercise"
prnt_even_char(a)
