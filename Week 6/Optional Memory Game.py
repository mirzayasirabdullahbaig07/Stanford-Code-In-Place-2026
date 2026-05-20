import random

NUM_PAIRS = 3

def main():
    # Create truth list
    truth_list = []

    for i in range(NUM_PAIRS):
        truth_list.append(i)
        truth_list.append(i)

    # Shuffle truth list
    random.shuffle(truth_list)

    # Create displayed list
    displayed_list = []

    for i in range(len(truth_list)):
        displayed_list.append('*')

    # Game loop
    while '*' in displayed_list:
        print(displayed_list)

        index1 = get_valid_index(displayed_list)

        index2 = get_valid_index(displayed_list, index1)

        # Check for match
        if truth_list[index1] == truth_list[index2]:
            displayed_list[index1] = truth_list[index1]
            displayed_list[index2] = truth_list[index2]

            print("Match!")
            clear_terminal()

        else:
            print(f"Value at index {index1} is {truth_list[index1]}")
            print(f"Value at index {index2} is {truth_list[index2]}")
            print("No match. Try again.")

            input("Press Enter to continue...")
            clear_terminal()

    # Game finished
    print(displayed_list)
    print("Congratulations! You won!")


def get_valid_index(displayed_list, first_index=None):
    while True:
        user_input = input("Enter an index: ")

        # Check if number
        if not user_input.isdigit():
            print("Not a number. Try again.")
            continue

        index = int(user_input)

        # Check bounds
        if index < 0 or index >= len(displayed_list):
            print("Invalid index. Try again.")
            continue

        # Check same index twice
        if first_index is not None and index == first_index:
            print("You entered the same index twice. Try again.")
            continue

        # Check already matched
        if displayed_list[index] != '*':
            print("This number has already been matched. Try again.")
            continue

        return index


def clear_terminal():
    for i in range(20):
        print('\n')


if __name__ == '__main__':
    main()