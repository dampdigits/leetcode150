class RandomizedSet:

    def __init__(self):
        self.vals = list()
        self.idx = dict()

    def insert(self, val: int) -> bool:
        if val in self.idx: return False

        self.vals.append(val)
        self.idx[val] = len(self.vals) -1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx: return False

        index = self.idx[val]
        self.vals[index] = self.vals[-1]
        self.idx[self.vals[-1]] = index
        self.vals.pop()
        del self.idx[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
