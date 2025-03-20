class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first, second = 0, 0
        merged = ""
        while first < min(len(word1), len(word2)):
            merged += word1[first]
            merged += word2[second]
            first += 1
            second += 1
        
        if len(word1) > len(word2):
            merged += word1[first:]
        elif len(word1) < len(word2):
            merged += word2[first:]

        return merged