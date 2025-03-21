class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        
        max_seen = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_seen
            
            if i == len(arr) - 1:
                arr[i] = max_seen
            
            arr[i] = max_seen
            
            if current > max_seen:
                max_seen = current
            
                
        return arr