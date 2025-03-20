class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1  
                    flowers += 1

                    if flowers >= n:
                        return True

        return flowers >= n