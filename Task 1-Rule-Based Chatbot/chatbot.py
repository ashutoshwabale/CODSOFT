import random
from datetime import datetime

# Function to load jokes
def load_jokes():
    try:
        with open("jokes.txt", "r") as file:
            return [joke.strip() for joke in file.readlines()]
    except:
        return ["Sorry, I don't have any jokes right now!"]

# Function to load motivation quotes
def load_motivation():
    try:
        with open("motivation.txt", "r") as file:
            return [quote.strip() for quote in file.readlines()]
    except:
        return ["Keep going, success is near!"]

print("----- Smart Rule-Based Chatbot -----")
print("Type 'exit' anytime to stop\n")

name = input("Chatbot: Hello! What is your name?\nYou: ")
print(f"Chatbot: Welcome {name}! How can I help you today?")

jokes_list = load_jokes()
motivation_list = load_motivation()

while True:
    user_input = input("\nYou: ").lower().strip()

    if user_input == "exit":
        print(f"Chatbot: Goodbye {name}! See you soon 😊")
        break

    # Greeting detection (improved)
    elif any(word in user_input for word in ["hi", "hello", "hey"]):
        print("Chatbot:", random.choice([
            f"Hello {name}!",
            "Hi there!",
            "Hey! Nice to chat with you."
        ]))

    elif "how are you" in user_input:
        print("Chatbot: I'm functioning perfectly! Thanks for asking.")

    elif "thank" in user_input:
        print("Chatbot: You're welcome!")

    elif "your name" in user_input:
        print("Chatbot: I am your advanced rule-based chatbot.")

    elif "time" in user_input:
        print("Chatbot: Current time is",
              datetime.now().strftime("%H:%M:%S"))

    elif "date" in user_input:
        print("Chatbot: Today's date is",
              datetime.now().strftime("%d-%m-%Y"))

    # Combined Math Section
    elif any(op in user_input for op in ["add", "subtract", "multiply", "divide"]):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if "add" in user_input:
                print("Chatbot: Result =", a + b)

            elif "subtract" in user_input:
                print("Chatbot: Result =", a - b)

            elif "multiply" in user_input:
                print("Chatbot: Result =", a * b)

            elif "divide" in user_input:
                if b == 0:
                    print("Chatbot: Cannot divide by zero!")
                else:
                    print("Chatbot: Result =", a / b)

        except:
            print("Chatbot: Please enter valid numeric values.")

    elif "joke" in user_input:
        print("Chatbot:", random.choice(jokes_list))

    elif "motivate" in user_input or "motivation" in user_input:
        print("Chatbot:", random.choice(motivation_list))

    elif "help" in user_input:
        print("\nChatbot: I can help you with:")
        print("• Greetings")
        print("• Time and Date")
        print("• Basic Calculations (add, subtract, multiply, divide)")
        print("• Telling jokes")
        print("• Giving motivation")
        print("• Type 'exit' to quit\n")

    else:
        print("Chatbot: Sorry, I didn’t understand that. Type 'help' to see options.")
