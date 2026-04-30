class Solution:
    def wordToDict(self, word):
        dict={}
        for letter in word:
            dict[letter]=dict.get(letter,0)+1
        return dict
    def isAnagram(self, s: str, t: str) -> bool:
        # return self.wordToDict(s)==self.wordToDict(t)
        d1,d2=self.wordToDict(s), self.wordToDict(t)
        for letter in s:
            if d1.get(letter)!=d2.get(letter,0):
                return False
        for letter in t:        
            if d2.get(letter)!=d1.get(letter,0):
                return False
        return True