sensitive_words = ["gun", "murder", "attack", "bomb", "kill"]

# take input
text = input("Enter a sentence: ")

# convert to lowercase
text = text.lower()

found = False

# check each word
for word in sensitive_words:
    if word in text:
        if found == False:
            print("Sensitive Content Detected")
            print("Detected words:")
            found = True
        print(word)

# if nothing found
if found == False:
    print("Safe Content")
    