class Temp:
    def __init__(self, cel):
        self.cel = cel

    def celsius(self):
        return self.cel

    @property
    def fahrenheit(self):
        return self.cel
    @fahrenheit.setter
    def fahrenheit(self, value):
        return (self.cel * 9.5) + 32


i = Temp(10)
i.fahrenheit
print(i)
