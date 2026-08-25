class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}
        for element in s:
            if element in s_map:
                s_map[element] += 1
            else:
                s_map[element] = 1
        
        for element in t:
            if element in t_map:
                t_map[element] += 1
            else:
                t_map[element] = 1
    
        return s_map == t_map