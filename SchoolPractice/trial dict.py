d = {}
l = int(input("enter the number of students whose marks you want to enter: "))
for x in range(l):
    print("Enter the details of students")
    roll = int(input("Enter the roll: "))
    name = (input("Enter the std name: "))
    mark = int(input("Enter the marks receieved by the student: "))
    d[roll] = [name, mark]
print(d)
for std in d:
    if d[std][1] > 0:
        print("Student secured more than 2 is", d[std][0])