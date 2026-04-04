class TimeMap:

    def __init__(self):

        self.keyStore={} # key : list of [val, timestamp]

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.keyStore:
            return ""

        else:

            values = self.keyStore.get(key)
            left, right = 0, len(values)-1

            while left <= right:
                mid = (left+right)//2

                if values[mid][0] == timestamp:
                    return values[mid][1]

                if values[mid][0] < timestamp:
                    left = mid+1
                else:
                    right = mid -1

            if right < 0:
                return ""
            else:
                return values[right][1]




        
