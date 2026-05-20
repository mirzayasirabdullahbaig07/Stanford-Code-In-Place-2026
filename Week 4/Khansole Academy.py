import random

def main():
    print("Khansole Academy")
    
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    total = num1 + num2 
    
    print("What is " + str(num1) + " + " + str(num2) + "?") 
    answer = int(input("Your answer: "))
    
    # True if answer is not equal to total
    if answer != total:
        print("Incorrect.")
        print("The expected answer is " + str(total)) 
    else:
        print("Correct!")
    
if __name__ == '__main__':
    main()