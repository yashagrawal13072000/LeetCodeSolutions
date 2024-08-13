# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n=len(candidates)
        res = []

        def backtrack(start,target,path):
            if target == 0:
                res.append(path.copy())
                return
            if target < 0:
                return
            
            for i in range(start,n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                backtrack(i+1, target-candidates[i], path + [candidates[i]])
        
        backtrack(0,target,[])
        return res