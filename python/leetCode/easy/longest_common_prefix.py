class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        strs.sort(key=len)
        word = strs[0]
        for i in range(len(word)):
            for compare in strs[1:]:
                if word[i] != compare[i]:
                    return answer
            answer += word[i]
        return answer
