def calculate_word_value(word):
    return sum(ord(char.lower()) - 96 for char in word if char.isalpha())

def main():
    print("Word Value Calculator")
    word = input("Enter a word: ").strip()
    
    if not word.isalpha():
        print("Please enter a valid word containing only letters.")
        return
        
    value = calculate_word_value(word)
    print(f"The value of '{word}' is: {value}")
    print("(Calculation: " + " + ".join(f"{ord(char.lower()) - 96}" for char in word) + f" = {value})")

if __name__ == "__main__":
    main()
