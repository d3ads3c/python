class Vector:
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def length(self):
        return (self.x ** 2 + self.z ** 2) ** 0.5


a = Vector(2, 2)
res = a.length()
print(res)
