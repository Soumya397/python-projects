def get_name():
    return input("Please enter your name: ")

def create_greeting(name):
    return f"Hello, {name}! Nice to meet you!"

def main():
    name = get_name()
    greeting = create_greeting(name)
    print(greeting)

if __name__ == "__main__":
    main()
