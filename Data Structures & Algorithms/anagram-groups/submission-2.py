class Solution:
    def wordToTuple(self, word):
        list_of_word=[0]*26
        for letter in word:
            list_of_word[ord(letter)-ord('a')]+=1
        return tuple(list_of_word)   

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            tuple_str = self.wordToTuple(word)
            if tuple_str in d:
                d[tuple_str].append(word)
            else:
                d[tuple_str]=[word]  
        return [arr for arr in d.values()]          

        