# Print the sum of the current number and the previous number
prev=0
for i in range(10):
    sum=prev+i
    print("Current Number " + str(i) + " Previous Number " + str(prev) + " Sum " + str(sum))
    prev=i
