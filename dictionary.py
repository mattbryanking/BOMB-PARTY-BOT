import random
import frenchWords as frenchWords
import englishWords as englishWords

class Dict:
    def __init__(self, lang):
        self.lang = lang
        self.prompt = ""
        self.words = []
        self.impressive_words = []
        self.simple_words = []
        self.wordDict = {}
        self.impWordDict = {}
        self.simpWordDict = {}

    def makeLists(self):
        if self.lang == 1:
            self.words = englishWords.words
        if self.lang == 2:
            self.words = frenchWords.words

    def findAnswer(self, sub):
        if sub in self.wordDict:
            if len(self.wordDict[sub]) > 0:
                return self.wordDict[sub].pop()
            else:
                return  "no more words :("
        else:
            subList = []
            for word in self.words:
                if sub in word.lower():
                    subList.append(word)
            random.shuffle(subList)
            self.wordDict[sub] = subList
            return self.wordDict[sub].pop()

    def findAnswerImp(self, sub):
        if sub in self.impWordDict:
            if len(self.impWordDict[sub]) > 0:
                return self.impWordDict[sub].pop()
            else:
                return  "no more words :("
        else:
            subList = []
            for word in self.impressive_words:
                if sub in word:
                    subList.append(word)
            random.shuffle(subList)
            self.impWordDict[sub] = subList
            return self.impWordDict[sub].pop()

    def findAnswerSimple(self, sub):
        if sub in self.simpWordDict:
            if len(self.simpWordDict[sub]) > 0:
                return self.simpWordDict[sub].pop()
            else:
                return  "no more words :("
        else:
            subList = []
            for word in self.simple_words:
                if sub in word:
                    subList.append(word)
            random.shuffle(subList)
            self.simpWordDict[sub] = subList
            return self.simpWordDict[sub].pop()
