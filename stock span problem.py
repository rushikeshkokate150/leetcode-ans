class StockSpanner(object):
    def _init_(self):
        self.arr = []  # instance variable
        self.indx=-1

    def next(self, price):
        self.indx=self.indx+1
        while len(self.arr)!=0 and self.arr[-1][0]<=price:
            self.arr.pop()
        ans=self.indx-(-1 if len(self.arr)==0 else self.arr[-1][1])
        self.arr.append([price,self.indx])

        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)