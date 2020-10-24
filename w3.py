def sum(x, y):
    return x + y 

numberOfValue = int(input("number of value: "))
total  = 0
for i in range(numberOfValue):
    value = int(input("Value " + str(i + 1) + ": "))    
    total = sum(total, value)
print("The sum is:" + str(total))