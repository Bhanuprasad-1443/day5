while True:
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    choice=input("enter operation(+ or -):")
    if choice=="+":
        print("result:",a+b)
    elif choice=="-":
        print("result:",a-b)
    else:
        print("invalid operation")
    again = input("do you want to continue?(y/n)")
    if again == "n":
        print("exit")
        break  

        
while True:
    age=int(input("enter your age:"))
    if age<18:
        print("eligible for half ticket:")
        print("happy journey:")
    elif age>=18 and age < 60:
        print("eligible for full ticket:")
        
        print("happy Journey")
    elif age>=60:
        print("eligible for free ticket:")
        print("Take care,Happy Safe Journey:")
    else:
        print("invalid:")
    again=input("do you want to continue?(y refers to yes/n refers to no):")
    if again=="n":
      print("thank you")
      break  
            