"Count Even numbers From 1 to N" "Counting approach"  
'''def count_even(n):
    count=0
    for i in range(1,n+1):
        if i%2==0:
            count+=1
    return count

def main():
    n=int(input("Enter a number:"))
    print("Even count:", count_even(n))
main()'''


#count Digits in numbers
#input: 12345
#output:5

def count_digits(num):
    count=0
    while num > 0:
        num=num//10
        count+=1
    return count
def main():
    num=int(input("Enter number:"))
    print("Digits count:" , count_digits(num))
main()
