class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        first_half = []
        if len(arr) >= 3:
            for j in range(len(arr)-1):
                if arr[j] < arr[j+1]:
                    first_half.append(arr[j])
                
                elif arr[j] > arr[j+1]:
                    if len(first_half) != 0 and arr[j] > max(first_half) and arr[j] != max(first_half):
                        midpoint = arr[j]
                        for r in range(j + 1, len(arr)):
                            if arr[r - 1] <= arr[r]:
                                return False
                        return True
                    return False

                elif arr[j] == arr[j+1]:
                    return False
                
        return False
    
        # find the biggest element in an array
        # compare the biggest element with previous element
        # if it is bigger, then move on next
        # repeat. 