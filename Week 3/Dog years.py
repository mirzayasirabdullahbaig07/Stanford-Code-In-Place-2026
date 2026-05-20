# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    # Get user input
    age = float(input("Enter an age in calendar years: "))
    
    # Convert to dog years
    dog_years = age * DOG_YEARS_MULTIPLIER
    
    # Print result
    print(f"That's {dog_years} in dog years!")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()