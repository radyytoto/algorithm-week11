def getPrice(fruitName):
    if fruitName == "banana":
        return 2
    elif fruitName == "apple":
        return 5
    elif fruitName == "orange":
        return 1
print("banana price is: " + str(getPrice("banana")) + " dollars")
print("orange price is: " + str(getPrice("orange")) + " dollars")