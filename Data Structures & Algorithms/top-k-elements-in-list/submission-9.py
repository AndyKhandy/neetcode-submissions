class Solution:
     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}

        for num in nums:
            myMap[num] =  1 + myMap.get(num,0)

        heap = []

        for num,freq in myMap.items():
            heapq.heappush(heap,(freq,num)) # 2 : 2 and 3 : 3
            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res




        