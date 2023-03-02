import config
import openai
openai.api_key = config.api_key
COMPLETIONS_MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 500


class ChatGPT:

    def __init__(self) -> None:
        self.messages=[
            {"role": "system", "content": "You are a helpful assistant."},
        ]

    def request(self):
        completion_response = openai.ChatCompletion.create(
                                model="gpt-3.5-turbo",
                                temperature=0.2,
                                max_tokens = MAX_TOKENS,
                                messages=self.messages
                                )
        return completion_response

    def chat(self, prompt):
        message = {"role": "user", "content": f"{prompt}"}
        self.messages.append(message)
        output = self.request()
        system_response = output["choices"][0]["message"]["content"]
        self.messages.append({"role": "system", "content": f"{system_response}"})
        return system_response

if __name__ == "__main__":
    model = ChatGPT()
    print("Enter a prompt to generate text (type 'exit' to quit): ")
    while True:
        prompt = input("You: ")
        if prompt.lower() == "exit":
            break

        response = None 
        response = model.chat(str(prompt))

        print(f"ChatGPT: {response}")
        response = None




