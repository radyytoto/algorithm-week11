def numberOfUpperCases(word):
    count = 0
    for i in range(len(word)):
        if word[i] == word[i].upper() and word[i] != " ":
            count += 1 
    return count
text = str(input("Word: "))
print("The uppercase number: " + str(numberOfUpperCases(text)))
