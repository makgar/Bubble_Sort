#!/usr/bin/python3.6

values = []
wrong_values = []

for value in input("Please provide values you wish to sort separated with spaces:\n").split(" "):
    try:
        value = int(value)
        values.append(value)
    except:
        wrong_values.append(value)

print()

if len(wrong_values) > 0:
    print("The following values are not integers, so they will be skipped:")
    print(wrong_values)
    print()

print("The following values will be sorted:")
print(values)
print()

length = len(values)
for i in range(length-1):
    #print("i = %d" % i) # uncomment for debugging
    swaps = 0
    for j in range(length-1-i):
        #print("first = %d" % values[j]) # uncomment for debugging
        #print("second = %d" % values[j+1]) # uncomment for debugging
        if values[j] > values[j+1]:
            elem = values.pop(j)
            values.insert(j+1, elem)
            swaps = swaps + 1
            #print(values) # uncomment to see the elements after every swap
    if swaps == 0:
        break # if not a single elment was swapped during a loop, it means that elemets are already placed correctly. No need to continue

print("Result:")
print(values)