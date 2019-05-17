height = float(input("enter your height : "))
weight = int(input("enter your weight :"))
bmi = weight / (height * height)
if bmi <= 18:
    print("under - weight")
elif bmi <= 25:
    print("normal")
else:
    print("over-weight")
