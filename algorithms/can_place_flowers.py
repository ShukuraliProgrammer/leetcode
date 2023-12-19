from typing import List
def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    if flowerbed[n] == 1:
        return True
    else:
        return False

res = canPlaceFlowers(flowerbed=[1,0,0,0,1], n=1)
