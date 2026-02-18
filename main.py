#This is a simple calculator 
print("Enter 1 for sum.\nEnter 2 for subtraction \nEnter 3 for mul .\nEnter 4 for div")
user_input=int(input("Enter your choice"))
if user_input==1:
    a=float(input("Enter your number "))
    b=float(input("Enter your number "))
    sum=a+b
    print(f"The sum of two number is {sum}")
elif user_input==2:
    a=float(input("Enter your number "))
    b=float(input("Enter your number "))
    sub=a-b
    print(f"The subtraction of two number is {sub}")
elif user_input==3:
    a=float(input("Enter your number "))
    b=float(input("Enter your number "))
    if b==0:
        print("cannot divide by zero ")
    else:
        div=a/b
        print(f"The division of two number is {div}")
elif user_input==4:
    a=float(input("Enter your number "))
    b=float(input("Enter your number "))
    mul=a*b
    print(f"The subtraction of two number is {mul}")

else:
    print("Invalid choice..try again ")

        
    
