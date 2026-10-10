class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s={}
        map_t={}
        for i in range(len(s)):
            map_s[s[i]]=map_s.get(s[i],0)+1
        for i in range(len(t)):
            map_t[t[i]]=map_t.get(t[i],0)+1
        return map_s==map_t
        