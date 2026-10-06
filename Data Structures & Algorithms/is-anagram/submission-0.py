class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def count_ch(sent):
            count_map = {}
            for ch in sent:
                if ch in count_map:
                    count_map[ch] += 1
                else:
                    count_map[ch] = 1

            return count_map

        return count_ch(s) == count_ch(t)

        

        