class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m+1)]
        idx_p = 0
        for idx, value in enumerate(queries):
            idx_p = p.index(value)
            queries[idx] = idx_p
            p = [value] + p[0:idx_p] + p[idx_p+1:]
            

        
        return queries