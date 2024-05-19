# GPT-4 Chatbot

This project allows you to interact with OpenAI's GPT-4 model through a simple command-line interface. You can ask questions or request code snippets, and the model will respond accordingly.

## Features

- Interact with GPT-4 through the command line.
- Provide custom prompts to GPT-4.
- Exit the chat by typing 'quit'.

## Requirements

- Python 3.6 or later
- OpenAI API key
- `openai` library

## Installation

1. **Clone the repository or download the script files.**

2. **Install the required Python packages:**

    ```sh
    pip install openai
    ```

3. **Set your OpenAI API key as an environment variable:**

    - On Windows:
        ```sh
        set OPENAI_API_KEY=your_openai_api_key
        ```
    - On macOS and Linux:
        ```sh
        export OPENAI_API_KEY=your_openai_api_key
        ```

## Usage

1. **Run the script:**

    ```sh
    python gpt4_chatbot.py
    ```

2. **Interact with the chatbot:**

    - You can start chatting with GPT-4. Type your questions or requests.
    - To exit the chat, type `quit`.

## Code Explanation

### `chat_with_gpt4()`

This function initializes the OpenAI client and starts a command-line chat session with GPT-4.

- **Initialize the OpenAI client:**
    ```python
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    ```

- **Check for API key:**
    ```python
    if not client.api_key:
        print("OpenAI API key is not set in the environment variables.")
        return
    ```

- **Start the chat loop:**
    ```python
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        ```

- **Send the message to GPT-4 and get the response:**
    ```python
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an assistant that helps me code fully functional and efficient code in python. You only response with code."},
            {"role": "user", "content": user_input}
        ],
        model="gpt-4-turbo-2024-04-09",
        temperature=0.1,
        max_tokens=1200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    message_content = response.choices[0].message.content.strip()
    ```

- **Print the response:**
    ```python
    print("GPT-4:", message_content)
    ```

## Notes

- Ensure you have set your OpenAI API key as an environment variable before running the script.
- Adjust the `model`, `temperature`, `max_tokens`, `top_p`, `frequency_penalty`, and `presence_penalty` parameters as needed to customize the chatbot's responses.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
