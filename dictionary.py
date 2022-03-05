import random

prompt = "AST"
words = []
impressive_words = []
simple_words = []
wordDict = {}
impWordDict = {}
simpWordDict = {}

def makeLists():
    with open("englishwords.txt", "r") as file:
        word = file.readline()
        while word:
            word = word.strip()
            words.append(word.lower())
            if len(word) >= 10:
                impressive_words.append(word.lower())
            if len(word) <= 5:
                simple_words.append(word.lower())
            word = file.readline()
    file.close()
    
def findAnswer(sub):
    if sub in wordDict:
        return wordDict[sub].pop()
    else:
        subList = []
        for word in words:
            if sub in word:
                subList.append(word)
        random.shuffle(subList)
        wordDict[sub] = subList
        return wordDict[sub].pop()

def findAnswerImp(sub):
    if sub in impWordDict:
        return impWordDict[sub].pop()
    else:
        subList = []
        for word in impressive_words:
            if sub in word:
                subList.append(word)
        random.shuffle(subList)
        impWordDict[sub] = subList
        return impWordDict[sub].pop()
    
def findAnswerSimple(sub):
    if sub in simpWordDict:
        return simpWordDict[sub].pop()
    else:
        subList = []
        for word in simple_words:
            if sub in word:
                subList.append(word)
        random.shuffle(subList)
        simpWordDict[sub] = subList
        return simpWordDict[sub].pop()

makeLists() 
print(findAnswerSimple(prompt))






