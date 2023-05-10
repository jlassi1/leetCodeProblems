class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref)<2:
            return pref
        new_pref = [pref[0]] 
        for idx in range(1, len(pref)):
            new_pref.append(pref[idx] ^ pref[idx-1])
     
        return new_pref


            