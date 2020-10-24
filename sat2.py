def reverseString(text):
    lastIndex = len(text) - 1
    for i in range(len(text)):
        result += text[lastIndex - i]
    return result

# Test 1
text1 = "Hello PNC"
result = reverseString(text1)
print(result)

# Test 2
text2 = "Welcome 2021"
result = everseString(text2)

print(result)