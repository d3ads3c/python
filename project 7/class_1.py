import math


class Motasavi:
    def __init__(self, a, b, alpha):
        self.a = a
        self.b = b
        self.alpha = alpha

    def height(self):
        c = math.radians(self.alpha)
        return math.sin(c) * self.b

    def area(self):
        return self.b * self.height()

    def perimeter(self):
        return (self.a + self.b) * 2


s1 = Motasavi(5, 5, 30)
res_1 = s1.area()
res_2 = s1.perimeter()
print(res_1, res_2)
