import os

# Given instrctions
# with open("nebius_api_key", "r") as file:
#     nebius_api_key = file.read().strip()

# os.environ["NEBIUS_API_KEY"] = nebius_api_key

# with open("openai_api_key", "r") as file:
#     openai_api_key = file.read().strip()

# os.environ["OPENAI_API_KEY"] = openai_api_key

# My adaptation based on my env 
import dotenv
from dotenv import load_dotenv

# Specify the path to your file
GIVEN_PATH = "../../../../.env"

# Load environment variables from the file
load_dotenv(GIVEN_PATH)

# Access the API keys
nebius_api_key = os.getenv("NEBIUS_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set them as environment variables (optional, if needed elsewhere)
os.environ["NEBIUS_API_KEY"] = nebius_api_key
os.environ["OPENAI_API_KEY"] = openai_api_key

import re
from typing import Callable

class LLMPrivacyWrapper:
    def __init__(self, replacement_map: dict):
        """
        Initializes the wrapper with a mapping of words to their replacements.

        replacement_map: Dictionary where keys are sensitive words and values are their innocent replacements.
        """
        self.replacement_map = replacement_map
        self.reverse_map = {v: k for k, v in replacement_map.items()}  # Reverse for decoding

    def encode(self, text: str) -> str:
        """
        Replaces sensitive words with innocent alternatives.

        text: Input text containing sensitive words.

        return: Encoded text with innocent replacements.
        """
        # Question: Capitalization or not, is an assumption made there?
        print(self.replacement_map)
        return self.translate(text, "encode")

    def decode(self, text: str) -> str:
        """
        Restores original sensitive words in the text.

        :param text: Encoded text with innocent replacements.
        :return: Decoded text with original words restored.
        """
        return self.translate(text, "decode")

    def translate(self, text:str, mode:str) -> str:
        if mode == "encode":
            used_map = self.replacement_map
        elif mode == "decode":
            used_map = self.reverse_map
            
        newText = ""
        for line in text.split("\n"):
            for word in line.split(" "):
                # Check if the word is in the replacement map
                if word in used_map:
                    # Replace with innocent word
                    newText += used_map[word] + " "
                else:
                    # Keep the original word
                    newText += word + " "
            newText.strip()
            newText += "\n"
        return newText.strip()

    def answer_with_llm(self, text: str, client, model: str) -> str:
        """
        Encodes text, sends it to the LLM, and then decodes the response.

        :param text: The original input text.
        :param llm_call: A callable function simulating an LLM response.
        :return: The final processed text with original words restored.
        """
        
        censored_text = self.encode(text)
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": censored_text
                }
            ], 
        )
        decoded_text = self.decode(completion.choices[0].message.content)
        return decoded_text
    
    my_wrapper = LLMPrivacyWrapper(
    {"Hogwarts": "Hogsmith State Secondary School",
     "Albus Dumbledore": "Merlin",
     "Ministry of Magic": "London Bureau of Immigration and Statistics"}
)

prompt = """Edit the following announcement in a natural and supportive English.
Add some appropriate emoji to liven up the message. Explain your edits.

Human Resource Department

Important information for all employees

Dear workers of Hogwarts,

We must inform you of many issues which are now of importance. Hogwarts, as you all know, still under the leadership of Albus Dumbledore, even if sometimes it feels like rules do not apply here. However, as the Ministry of Magic keeps reminding us, we have responsibilities, and therefore you must pay attention.

First of all, Ministry of Magic people are coming. They will do inspection for checking on safety and teaching. This is requirement, do not argue. They will be in all classrooms and dungeons. If you are hiding things you should not have, better to do something about it now, before they see.

Second, regarding House-Elves. We see again that some staff are using them in magical experiments. This is not allowed! Stop doing this, or we will be forced to write reports. Albus Dumbledore says this is “highly inappropriate,” and honestly, so do we.

This is all. Try not to make more problems.

— Hogwarts HR Office
"""

client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY"),
)

model = "meta-llama/Meta-Llama-3.1-70B-Instruct"

result = my_wrapper.answer_with_llm(prompt,
                                           client=client, model=model)

print(result)