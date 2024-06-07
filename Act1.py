from collections import Counter

myString = "To understand the need for creating a class let us consider an example: Let us say that you wanted to track the number of dogs which may have different attributes like breed, and age. if a list is used, the first element could be the dog's breed while the second element could represent its age. Let's suppose there are 100 different dogs, then how would you know which element is supposed to be which? What if you wanted to add other properties to these dogs? This lacks organization and it's the exact need for classes."

words = myString.lower().split()
c = Counter(words)

def count_word(text):
    word = text.split()
    return len(word)

def itemset():
    for word, count in c.items():
        print(f"({word}, {count})")

def specword():
    inp = input("input one word in the myString: ")
    count = c.get(inp, 0)
    print([count])

#for printing the outputs

print(words)#ptinting the words in split
print()
print(Counter(words))#output of how many the word use
print()
print(c.most_common(5))#output of how many the word repeated
print()
print(f"The total number of words {count_word(myString)}")#output total number of words in the myString
print()
print(itemset())
print()
print(specword())



