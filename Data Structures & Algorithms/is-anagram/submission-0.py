class Solution:
    def wordToDict(self, word):
        dict={}
        for letter in word:
            dict[letter]=dict.get(letter,0)+1
        return dict
    def isAnagram(self, s: str, t: str) -> bool:
        return self.wordToDict(s)==self.wordToDict(t)
        