class Solution:
     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}

        for num in nums:
            myMap[num] = myMap.get(num,0) + 1

        heap = []

        for num,count in myMap.items():
            heapq.heappush(heap, (count,num))
            if(len(heap) > k):
                heapq.heappop(heap)

        res = []

        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
            if(len(res) == k):
                return res
        return res


        