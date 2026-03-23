expenses=[]
def add_expenses():
    name=input("Enter th expenses name")
    amount=int(input("Enter expense amount"))
    expense={
        "name:name"
        "amount:amount"
    }
def view_expenses():
    for expense in expenses():
        print(expense["name"], "-",expense['amount'])
def show_menu():
    print("\n Expense Tracker")
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Exit")
def main():
    while True:
        show_menu()
        choice=input("Enter your choice:")
        if choice=="1":
            add_expenses()
        elif choice=="2":
            view_expenses()
        elif choice=="3":
            print("exiting the program")
            break
        else:
            print("Invalid choice .Try again")
main()
        