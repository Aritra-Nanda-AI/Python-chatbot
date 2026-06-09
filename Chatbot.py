user = input("You: ")

if "hello" in user.lower():
    print("Bot: Hello!")
elif "name" in user.lower():
    print("Bot: My name is Aritra Bot")
elif "bye" in user.lower():
    print("Bot: Goodbye!")
else:
    print("Bot: Sorry, I don't understand.")
