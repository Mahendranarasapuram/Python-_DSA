#finding the sum of array elements
def count_sum(arr):
    total=0
    for num in arr:
        total+=num
    return total
arr=[1,2,3,4,5]
print("Sum:",count_sum(arr))
#counting the digits in array
def count_digits(arr):
    count=0
    for num in arr:
        count+=1
    return count
arr=[1,2,3,4,5]
print("digits count", count_digits(arr))
#counting the even digits
def Even_count(arr):
    count=0
    for num in arr:
        if num%2==0:
            count+=1
    return count
arr=[1,2,3,4,5]
print("Even count:", Even_count(arr))
#finding the maximum value in array
def max_num(arr):
    max_value=arr[0]
    for num in arr:
        if num>max_value:
            max_value=num
    return max_value
arr=[1,2,3,4,5]
print("Max number",max_num(arr))
#File handling expense tracker system
expenses=[]
def export_expenses(expenses):
    with open("expenses.txt","w") as file:
        file.write(expenses["name"+ " " + expenses["amount"] + "\n"])
        
def main():
    while True:
        print("\n1.Add Expense")
        print("2.View Expenses")
        print("3.Export to file")
        print("4. Exit")
        choice=input("Enter your choice")
        if choice=='1':
            name=input("Enter the expense name")
            amount=int(input("Enter amount"))
            expenses.append({"name": name,"amount":amount})
        elif choice=="2":
            for expense in expenses:
                print(expense["name"],"-", expense["amount"])
        elif choice=="3":
            export_expenses(expenses)
        elif choice=="4":
            print("Exiting th program")
            break
        else:
            print("Invalid choice. try Again")
main()
                
    
    
        