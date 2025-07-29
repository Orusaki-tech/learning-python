# get details of loan from the user
money_owed = float(input("how much money do you owe in dollars?\n")) # $50000
apr = float(input("what is the annual percentage rate on the loan?\n"))# 3%
payement= float(input("how much will you pay off each month in dollars\n")) # $1000
months = int(input("How many months do you want to see the results for?\n")) #24

monthly_rate = apr/100/12


for i in range(months):
    #Calculate the interest to pay.
    interest_paid = money_owed * monthly_rate

    # Add interest to the money owed value
    money_owed = money_owed + interest_paid
    if (money_owed-payement <0):
        print("the last payment is ", money_owed)
        print("You paid off the last payement in ",i+1,"months")
        break
    #Make payment
    money_owed = money_owed - payement

    print("Now I owe", money_owed)