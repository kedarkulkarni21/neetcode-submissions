class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_chars = [0] * 26
        s2_chars = [0] * 26

        for i in range(len(s1)):
            s1_chars[ord(s1[i]) - ord('a')] += 1
            s2_chars[ord(s2[i]) - ord('a')] += 1     

        if s1_chars == s2_chars:
            return True  

        for j in range(len(s1), len(s2)):
            s2_chars[ord(s2[j]) - ord('a')] += 1
            s2_chars[ord(s2[j - len(s1)]) - ord('a')] -= 1

            if s1_chars == s2_chars:
                return True
            
        return False
            
            
            

