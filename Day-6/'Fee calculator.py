'''Fee calculator
calculating the  based on the course
vonditional logic in real projects
validation
edge case handling'''

def calculate_fee(course,marks):
    if course=="AI":
        fee=50000
    elif course=="WEB":
        fee=30000
    elif course=="DataScience":
        fee=40000
    else:
        return None 
    #Discount Condition
    if marks>90:
        fee-=5000
    return fee
def main():
    course=input("Enter course:")
    marks=int(input("Enter marks: "))
    fee=calculate_fee(course,marks)
    if fee is None:
        print("Invalid courde selected")
    else:
        print("Final Fee:",fee)
main()