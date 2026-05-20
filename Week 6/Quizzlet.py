def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }

    correct = 0
    total = len(translations)

    for english_word in translations:
        answer = input(f"What is the Spanish translation for {english_word}? ")

        if answer == translations[english_word]:
            print("That is correct!")
            correct += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english_word} is {translations[english_word]}.")

        print()

    print(f"You got {correct}/{total} words correct, come study again soon!")


if __name__ == '__main__':
    main()