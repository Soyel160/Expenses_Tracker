#Expense tracker project

expensesList=[] #list of expences in the form of dictionaries
print(" Welcome to Expense Tracker : ")

while True:
    print("======Menu======")
    print("1. Add Expense ")
    print("2. View All Expenses ")
    print("3. View Total Spent ")
    print("4. Exit ")

    choice=int(input("Please enter your choice: "))

#Add Expense
    if(choice==1):
        date=input("Enter the date of spenting that expense: ")
        category=input("Enter the type of the expense (Food,Travel,Makeup,Books,Movie): ")
        description=input("Give some more details: ")
        amount=float(input("Enter the amount: "))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expensesList.append(expense)
        print("\n Expense is added succesfully ")

#View all expenses
    elif(choice==2):
        if(len(expensesList)==0):
            print("No expenses added.First go and spent some money ")
        else:
            print("=====These are all your expenses=====")
            count=1
            for eachSpent in expensesList:
                print(f"Expense Number {count} -->{eachSpent["date"]},{eachSpent["category"]},{eachSpent["description"]},{eachSpent["amount"]}")
                count+=1

# View Total spending
    elif(choice==3):
        total=0
        for eachSpent in expensesList:
            total+=eachSpent["amount"]

        print("\n TOTAL SPENT = ",total)

#exit
    elif(choice==4):
        print("Thanks for using our System ")
        break
    else:
        print("Invalid choice,try again")    
