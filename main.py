#This is a simple calculator 
print("Enter 1 for sum.\nEnter 2 for subtraction \nEnter 3 for mul .\nEnter 4 for div")
user_input=int(input("Enter your choice"))
if user_input==1:
    a=float(input("Enter your number "))
    b=float(input("Enter your number "))
    sum=a+b
    print(f"The sum of two number is {sum}")
