from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_map = defaultdict(list)
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        string_sorted_s = "".join(sorted_s)
        string_sorted_t = "".join(sorted_t)
        print(string_sorted_s)
        print(string_sorted_t)
        if string_sorted_s == string_sorted_t:
            return True
        return False
        