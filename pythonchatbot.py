
def simple_chatbot():
    
    print("Chatbot: Hello! Type something (e.g., 'hello', 'how are you', 'bye')")

    while True:
        user_input = input("You: ").lower()  

        if user_input == "hello,sir":

        elif user_input == "how are you":
            print("Chatbot: i m fine, thanks!")

        elif user_input == "bye":
            print("Chatbot: goodbye!")
            break  

        else:
            print("Chatbot: Sorry, I don't understand.")


simple_chatbot()
































