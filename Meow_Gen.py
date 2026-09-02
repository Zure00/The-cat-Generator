import random

# List of cat jokes
cat_jokes = [
    "Why don't cats play poker in the jungle?",
    "What do cats eat for breakfast?",
    "Why did the cat sit on the computer?",
    "What's a cat's favorite color?",
    "How do cats end a fight?",
    "What do you call a cat that lives in the desert?",
    "Why was the cat sitting on the baseball player?",
    "What did the cat say when it lost?",
    "Why do cats go down the street at night?",
    "What do cats have that no other animals have?"
]

# Punchlines for the jokes
punchlines = [
    "Too many cheetahs!",
    "Mice Krispies!",
    "Because it wanted to keep an eye on the mouse!",
    "Purr-ple!",
    "They call a truce!",
    "A meow-age!",
    "He wanted to catch a fly ball!",
    "It was a cat-astrophe!",
    "Because the steaks are high!",
    "Kittens!"
]

# Cat endings
cat_endings = ["meo-ow!", "mreow!", "meo-ow!", "mreow!", "MREOW!", "meo-ow~"]

def generate_cat_joke():
    """Generate a random cat joke with meo-ow ending"""
    joke_index = random.randint(0, len(cat_jokes) - 1)
    
    joke = cat_jokes[joke_index]
    punchline = punchlines[joke_index]
    ending = random.choice(cat_endings)
    
    print(f"\n😸 {joke}")
    print(f"   {punchline} {ending}")

def main():
    """Main program"""
    print("\n" + "="*50)
    print("🐱 CAT JOKE GENERATOR 🐱")
    print("="*50)
    
    while True:
        print("\nWhat do you want to do?")
        print("1. Generate a cat joke")
        print("2. Generate 5 random cat jokes")
        print("3. Exit")
        
        choice = input("\nChoose (1-3): ").strip()
        
        if choice == "1":
            generate_cat_joke()
        elif choice == "2":
            print("\n" + "🐱"*15)
            for i in range(5):
                generate_cat_joke()
            print("🐱"*15)
        elif choice == "3":
            print("\n👋 Thanks for the cat jokes! Have a purr-fect day! 🐱")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()