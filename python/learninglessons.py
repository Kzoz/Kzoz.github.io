menu = "Arithmetics   geography"
menu2 = ("Addition  Substraction  Multiplication")
menu3 = ("Capitals   Country facts")
select_menu = input("What do you want to do today? ")

m1 = 0
while True:
    if select_menu.lower() == "arithmetics".lower() or select_menu.lower() == "A".lower():
        print(menu2)
        select_menu2 = input("What's your choice") 
        m2 = 0
        while True:
            if select_menu2 == "Addition chosen":
                print("Arithmetic")
                break
            elif select_menu2 == "Substraction chosen":
                print("Substraction")
                break
            elif select_menu2 == "Multiplication":
                print("Mutiplcation chosen")
                break
            else:
                print("Incorrect input")
                m2+= 1 
                if m2 >=3:
                    print("Restart from the beginning")
                    break
    elif select_menu.lower() == "geography".lower() or select_menu.lower() == "G".lower():
        print(menu3)
        select_menu3 = input("What's your choice")
        m3 = 0 
        while True:
            if select_menu3 == "Capitals":
                print("Capital chosen")
                break
            elif select_menu3 == "Country facts":
                print("Country Facts chosen")
                break
            else:
                print("Incorrect input")
                m3 += 1
                if m3 >= 3:
                    print("Restart from the beginning")
                    break

    else:
        print("Incorrect input")
        m1 += 1
        if m1 >= 3:
            print("Restart from the beginning")
            break

