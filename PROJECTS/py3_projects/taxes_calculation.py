import math

def revenue():
    user_input= input("Biweekly or Yearly revenue[B/Y] ?: ")
    if user_input == "Y".lower() or user_input == "Yearly".lower(): 
        rvn = int(input("Enter your annual revenue: $"))
        return rvn
    elif user_input == "B".lower() or user_input == "Biweekly".lower():
        rvn = int(input("Enter your biweekly salary: $"))
        rvn *=26
        return rvn
    else:
        return revenue()
    

salary = revenue()
print("Your annual revenue is $",salary, "\n")

def calculate_tax(my_salary):
    if my_salary <= 18200:
        my_tax = 0
        tax_rate = 0

    elif my_salary >= 18201  and my_salary <= 45000:
        my_tax = (my_salary-18200)*0.19
        tax_rate = 19

    elif my_salary >= 45001  and my_salary <= 120000:
        my_tax = 5092 + ((my_salary - 45000)*0.325)
        tax_rate = 32.5

    elif my_salary >= 120001  and my_salary <= 180000:
        my_tax = 29467 +((my_salary-120000)*0.37)
        tax_rate = 37

    else: 
        my_tax = 51667 + ((my_salary-180000)*0.45)
        tax_rate = 45
    
    print( "Your tax is $",math.ceil(my_tax), "per year or $",
    math.ceil(my_tax/12),"per month. Your tax rate is",tax_rate,"%")

calculate_tax(salary)



