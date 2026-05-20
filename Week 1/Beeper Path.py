from karel.stanfordkarel import *

def main():
    # Move while there are beepers ahead (on current or next cell)
    while beepers_present():
        move()
    # Move one more step past the end
   

if __name__ == '__main__':
    main()