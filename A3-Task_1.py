#Task 1: Calculate Factorial Using a Function


n=int(input("Enter the Number: "))
def factorial(n):
    fact=1
    for i in range(1,n+1) :
       fact *= i
    print(f"The Factorial of {n} is :",fact)
factorial(n)

