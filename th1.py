def sumFromTo(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i
    return result 

startValue = int(input("Start value: "))
endValue = int(input("End value: "))
total = sumFromTo(startValue, endValue)
print("The total: " + str(startValue) + " and " + str(endValue) + ":" + str(total))