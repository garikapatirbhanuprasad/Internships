import re

def get_response(user_input):
    user_input = user_input.lower()

    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hi there! How can I help you today?"

    elif re.search(r'\b(how are you|how\'s it going|what\'s up)\b', user_input):
        return "I'm just a computer program, but thanks for asking! How can I assist you?"

    elif re.search(r'\b(mood|feeling)\b', user_input):
        return "I'm a machine, so I don't have feelings. But thanks for asking! How about you? How are you feeling?"

    else:
        return "I'm sorry, I don't understand. Can you please rephrase or ask a different question?"

def main():
    print("Rule-Based Chatbot: Hello! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Rule-Based Chatbot: Goodbye!")
            break
        
        

        response = get_response(user_input)
        print("Rule-Based Chatbot:", response)

if __name__ == "__main__":
    main()
