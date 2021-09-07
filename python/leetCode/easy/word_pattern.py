class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        word = s.split(" ")
        if len(pattern) != len(word):
            return False
        for i in range(len(pattern)):
            if d.get(word[i]):
                if pattern[i] != d[word[i]]:
                    return False
            else:
                d[word[i]] = pattern[i]
        
        vl = d.values()
        if len(vl) != len(set(vl)):
            return False
        return True
        