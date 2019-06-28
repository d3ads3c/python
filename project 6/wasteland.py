poem = open("C:/Users/Student/Desktop/poem.txt").read()
out_file = open("C:/Users/Student/Desktop/output.txt", mode='w')
lower_Case = poem.lower()
out_file.write(len(poem.split()))

# print(len(poem.split()))
# print(len(set(lower_Case.split())))
