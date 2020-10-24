def removeMinuses(word):
    newWord = ""
    for i in range(len(word)):
        char = word[i]
        if char != "-":
            newWord += char
    return newWord
toContinue = True 
while toContinue:
    text = str(input("Enter word: "))
    result = removeMinuses(text)
    print("Word without minus: " + result)
    question = str(input("Do you want to continue (Y/N)? :"))
    if question.upper() != "Y":
        toContinue = False