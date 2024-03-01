name =input("please enter your name ")
student = input("Are you a true or false student? ")
condition = input("What is your marital status? (married / divorced / orphan) ")
city = input("What is your city? (egypt / usa / ksa) ")  
price = 100

if  city == "egypt":
    if student == "true":
        if condition == "orphan":
            print(f"hi {name} Because you are from {city} and student and orphan")
            print(f"The price will be {price - 40}")
        else: 
            print(f"hi {name} Because you are from {city} and student")
            print(f"The price will be {price - 30}")
    else:
        print(f"hi {name} Because you are from {city}")
        print(f"The price will be {price - 20}")
elif city == "ksa":
        if student == "true":
            if condition == "orphan":
                print(f"hi {name} Because you are from {city} and student and orphan")
                print(f"The price will be {price - 30}")
            else: 
                print(f"hi {name} Because you are from {city} and student")
                print(f"The price will be {price - 20}")
        else:
            print(f"hi {name} Because you are from {city}")
            print(f"The price will be {price - 10}")
elif city == "usa":
        if student == "true":
            if condition == "orphan":
                print(f"hi {name} Because you are from {city} and student and orphan")
                print(f"The price will be {price - 30}")
            else: 
                print(f"hi {name} Because you are from {city} and student")
                print(f"The price will be {price - 20}")
        else:
            print(f"hi {name} Because you are from {city}")
            print(f"The price will be {price}")
else:
    print(f"The price will be {price}")

