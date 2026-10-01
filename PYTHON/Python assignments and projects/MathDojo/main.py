class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        
        self.result += num
        for i in nums:
            self.result += i
        return self

    def subtract(self, num, *nums):
        
        self.result -= num
        for i in nums:
            self.result -= i
        return self
    
md = MathDojo()
cd= MathDojo()
bd= MathDojo()


x = md.add(2).add(2,5,1).subtract(3,2).result
print(x) 

y = cd.add(1).add(11,51,10).subtract(2,2).result
print(y)

z = bd.add(6).add(1,2,1).subtract(1,2).result
print(z)


