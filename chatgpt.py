import os
from openai import OpenAI

def chat_with_gpt4():
    """
    This function initializes the OpenAI client using an API key from the environment variables
    and starts a command-line chat session with GPT-4. Users can input their messages and receive
    responses from GPT-4. Typing 'quit' will end the chat session.
    """
    # Initialize the OpenAI client with the API key
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    # Check if the API key is set
    if not client.api_key:
        print("OpenAI API key is not set in the environment variables.")
        return

    # Inform the user that they can start chatting with GPT-4
    print("You can start chatting with GPT-4. Type 'quit' to exit.")

    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit the chat if the user types 'quit'
        if user_input.lower() == 'quit':
            break

        try:
            # Send the user's message to GPT-4 and get the response
            response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are an assistant that helps me code fully functional and efficient code in python. You only respond with code."},
                    {"role": "user", "content": user_input}
                ],
                model="gpt-4-turbo-2024-04-09",  # Adjust the model as necessary
                temperature=0.1,  # Controls the randomness of the response
                max_tokens=1200,  # Maximum number of tokens in the response
                top_p=1,  # Controls the diversity of the response
                frequency_penalty=0,  # Penalizes repeated tokens
                presence_penalty=0,  # Penalizes new tokens
            )

            # Extract the content of the response
            message_content = response.choices[0].message.content.strip()

            # Print the response from GPT-4
            print("GPT-4:", message_content)
        except Exception as e:
            # Print any errors that occur
            print(f"An error occurred: {e}")

# Call the function to start the chat session with GPT-4
chat_with_gpt4()
