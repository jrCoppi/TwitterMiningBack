class Anagram():
    isAnagram = False
    
    def __init__(self):
        self.isAnagram = False

    def setWords(self,firstWord,secondWord):
        self.firstWord = firstWord
        self.secondWord = secondWord

    def run(self):
        self.firstWord = self.firstWord.replace(' ','').lower()
        self.secondWord = self.secondWord.replace(' ','').lower()
    
        if(len(self.firstWord)!=len(self.secondWord)):
            self.isAnagram = False
            return False
        
        self.checkAnagram()

    
    def checkAnagram(self):
        counter = {}
        
        for letter in self.firstWord:
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1

        for letter in self.secondWord:
            if letter in counter:
                counter[letter] -= 1
            else:
                self.isAnagram = False
                return False

        for k in counter:
            if counter[k]!=0:
                self.isAnagram = False
                return False
        
        self.isAnagram = True

    
anagram = Anagram()
anagram.setWords("subi no onibus","subi no onibus")
anagram.run()

print(anagram.isAnagram)

anagram.setWords("ovo","ovo")
anagram.run()

print(anagram.isAnagram)

anagram.setWords("este é um teste","eteste")
anagram.run()

print(anagram.isAnagram)


anagram.setWords('hi man','hi     man')
anagram.run()

print(anagram.isAnagram)
