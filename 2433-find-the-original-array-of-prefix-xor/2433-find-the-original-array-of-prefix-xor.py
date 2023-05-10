class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref)<2:
            return pref
        new_pref = [0] * len(pref)

        for idx, num in enumerate(pref):
            if idx != 0:
                new_pref[idx] = num ^  pref[idx-1] 
            else:
                new_pref[idx] = num      
        return new_pref


            