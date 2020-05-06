print("What is My Mark???")
print(" ")
ku=float(input("Enter your K/U Mark: "))
kuO=float(input("What is K/U out of: "))
print(" ")
a=float(input("Enter your APP Mark: "))
aO=float(input("What is APP out of: "))
print(" ")
t=float(input("Enter your T Mark: "))
tO=float(input("What is T out of: "))
print(" ")
c=float(input("Enter your COM Mark: "))
cO=float(input("What is COM out of: "))

#Different for every course/school
kuw = (ku/kuO)*100*0.25
aw = (a/aO)*100*0.20
tw= (t/tO)*100*0.15
cw = (c/cO)*100*0.10
total = kuw + aw + tw + cw + 30
print(" ")
print("Your mark on the test is: ", "%.2f" % total, "%")
print("© 2019 Pragith Chenthuran")