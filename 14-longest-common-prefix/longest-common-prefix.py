class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first = strs[0]
        for word in strs[1:]:
            lcp = ""
            for i in range(min(len(first), len(word))):
                if first[i] == word[i]:
                    lcp += first[i]
                else:
                    break
            
            first = lcp
            if not first:
                break
            
        return first
