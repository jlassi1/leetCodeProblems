class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]

        for i, num in enumerate(encoded):
            result.append(result[i]^num)
        
        return result