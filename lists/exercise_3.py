# Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# Expected output - ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list3=[]

for i in list1:
    for j in list2:
        list3.append(i+j)
        
print(list3)
