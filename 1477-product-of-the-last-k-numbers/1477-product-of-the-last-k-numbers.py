class ProductOfNumbers:

    def __init__(self):
        self.prod=[1]
        

    def add(self, num: int) -> None:
        if num==0:
            self.prod=[1]
        else:
            self.prod.append(num*self.prod[-1])
    def getProduct(self, k: int) -> int:
        n=len(self.prod)
        if k>=n:
            return 0
        return self.prod[-1] // self.prod[-k-1]

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)