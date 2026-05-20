from ai import call_gpt

def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    
    print("Creating your haiku...")
    print()
    
    prompt = f"Write a haiku (5-7-5 syllables) about {topic}, and include the name {name} in the poem."
    
    haiku = call_gpt(prompt)
    
    print(haiku)

if __name__ == "__main__":
    main()