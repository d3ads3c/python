height = 1.75
weight = 90
bmi = weight / (height * height)
if bmi < 18:
    print("under - weight")
elif 18 <= bmi < 25:
    print("normal")
else:
    print("over-weight")
