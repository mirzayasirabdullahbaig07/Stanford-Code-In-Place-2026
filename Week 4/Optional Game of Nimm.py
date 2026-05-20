def main():
    stones = 20
    player = 1

    # Milestone 1 & 2: Loop until stones run out, track players
    while stones > 0:
        print("There are", stones, "stones left.")

        # Milestone 2: Show whose turn it is
        remove = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))

        # Milestone 3: Validate input — only 1 or 2 allowed
        while remove != 1 and remove != 2:
            remove = int(input("Please enter 1 or 2: "))

        # Handle edge case: only 1 stone left, can't take 2
        if stones == 1 and remove == 2:
            remove = int(input("Please enter 1 or 2: "))
            while remove != 1:
                remove = int(input("Please enter 1 or 2: "))

        stones -= remove

        # Milestone 4: Announce winner when stones run out
        if stones <= 0:
            print()
            # The player who took the last stone loses
            if player == 1:
                print("Player 2 wins!")
            else:
                print("Player 1 wins!")
        else:
            print()
            # Switch player
            if player == 1:
                player = 2
            else:
                player = 1

if __name__ == '__main__':
    main()