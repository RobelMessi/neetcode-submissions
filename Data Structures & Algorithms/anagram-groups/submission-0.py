from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_map = defaultdict(list)
        for s in strs:
            sorted_letters = sorted(s)
            valid_letters = "".join(sorted_letters)
            anagram_map[valid_letters].append(s)
        final_result = (anagram_map.values())
        return list(final_result)