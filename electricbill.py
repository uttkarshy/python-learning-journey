name=input("Enter your name: ")
unit=int(input("Enter the number of units consumed: "))
if unit<=100:
    bill=unit*5
    print("Hello", name + ", your electricity bill is: Rs.", bill)
elif unit>100 and unit<=300:
    bill=unit*7
    print("Hello", name + ", your electricity bill is: Rs.", bill)
else:
    bill=unit*10
    print("Hello", name + ", your electricity bill is: Rs.", bill)