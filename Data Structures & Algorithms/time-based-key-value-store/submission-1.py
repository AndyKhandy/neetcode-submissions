class TimeMap:

    def __init__(self):
        self.store = {} #key,value = str, List: (value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value,timestamp));

    def get(self, key: str, timestamp: int) -> str:
        res = "";
        values = self.store.get(key,[]);

        l,r = 0, len(values) - 1

        while l <= r:
            m = (l+r)//2
            currValue,currTimestamp = self.store[key][m]
            if currTimestamp <= timestamp:
                res = currValue
                l = m + 1
            else:
                r = m - 1

        return res
