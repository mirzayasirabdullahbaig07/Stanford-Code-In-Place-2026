import random

def main():
    # Ask user for number of sides
    sides = int(input("How many sides does your dice have? "))
    
    # Roll the dice
    roll = random.randint(1, sides)
    
    # Print result
    print(f"Your roll is {roll}")

if __name__ == '__main__':
    main()