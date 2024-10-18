from huggingface_hub import InferenceClient
from llm_axe import Agent, AgentType

client = InferenceClient(api_key="token")

class CustomLLM:
    # Your ask function will always receive a list of prompts
    # The prompts are in open ai prompt format
    # example: {"role": "system", "content": "You are a helpful assistant."}
    # If your model supports json format, use the format parameter to specify that to your model.

    def ask(self, prompts: list, format: str = "", temperature: float = 0.8):  # Corrected syntax here
        # Args:
        # prompts (list): A list of prompts to ask
        # format (str, optional): The format of the response. Use "json" for json.
        # temperature (float, optional): The temperature of the LLM. Defaults to 0.8

        # Assuming prompts is a list of dictionaries
        messages = [{"role": "user", "content": prompt} for prompt in prompts]  # Use prompts correctly

        response = client.chat_completion(
            model="meta-llama/Llama-3.2-38-Instruct",
            messages=messages,
            max_tokens=500,
            stream=False
        )

        return response.choices[0].content  # Indent this correctly

# Instantiate the class
llm = CustomLLM()  # Corrected class name

# Use a list of prompts instead of a single string
agent = Agent(llm, agent_type=AgentType.GENERIC_RESPONDER)

print(agent.ask(["Hi how are you today?"]))  # Pass a list of prompts

# Uncomment and corr
