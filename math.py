def read():
    #print("Enter a: ") # method 1
    a= int(input("Enter a: ")) # metthod 2
    #print("Enter b: ")
    b= int(input("Enter b: "))

    return a, b

def add(a, b):
    c= a + b

    return c

def subtract(a, b):
    c= a - b

    return c

def divide(a, b):
    c= a / b

    return c

def multiply(a, b):
    c= a * b

    return c

def choice(a, b):
    m= input("Enter a, s, m, d for addition, subtraction, mulitplication and division: ")

    if(m == "a"):
        return add(a, b)
    elif(m == "s"):
        return subtract(a, b)
    elif(m == "m"):
        return multiply(a, b)
    elif(m == "d"):
        return divide(a, b)
    else:
        print("\nOnly enter a, s, m, or d!!")

def solution(c):
    print(c)

def main():
    while True:
        a, b= read()
        c= choice(a, b)
        solution(c)
        print("\n")

if __name__ == '__main__':
    main()