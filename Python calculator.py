def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    if y==0:
        return("Division with 0 is not possible")
    else:
        return x/y
print("Enter your choice \n1. Addition\n2. Substract\n3. Multiply\n4. Division")

while True:
    choice=input("Enter your choice: ")
    if choice in('1','2','3','4'):
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        
        if choice=='1':
            print("Result: ", add(num1,num2))
        elif choice=='2':
            print("Result: ", sub(num1,num2))
        elif choice=='3':
            print("Result: ", multi(num1,num2))
        elif choice=='4':
            print("Result: ", div(num1,num2))
        else:
            print("Invalid input")
            
    nextcal=input("Do you want to perform another calculation (Y/N): ")
    if nextcal.lower()!='y':
        break