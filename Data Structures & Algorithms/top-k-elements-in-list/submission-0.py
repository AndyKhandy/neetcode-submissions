class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        myMap = {}

        for num in nums:
            myMap[num] = myMap.get(num, 0) + 1
        
        newMap = sorted(myMap.items(), key=lambda x: x[1], reverse=True)

        return [element[0] for element in newMap[:k]]




        