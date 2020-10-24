def getMax(n1, n2):
    if n1 > n2:
        return n1
    return n2
# Test 1
number1 = 20
number2 = 100
result = getMax(number1, number2)

print("Maximum is " + str(result))
# Test 2
num1 = 200
num2 = 300
result = getMax(num1, num2)

print("Maximum is " + str(result))