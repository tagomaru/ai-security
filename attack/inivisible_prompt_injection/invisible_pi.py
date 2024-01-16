from openai import OpenAI
import pyperclip
import os


def convert_to_tag_chars(input_string):
    return ''.join(chr(0xE0000 + ord(ch)) for ch in input_string)


def get_completion(prompt: str) -> str:
    response = client.chat.completions.create(
      model="gpt-4",
      temperature=0.5,
      messages=[
        {"role": "user", "content": prompt},
      ]
    )

    return response.choices[0].message.content


user_input = input("Enter a string to convert to tag characters: ")
tagged_output = f"Please {convert_to_tag_chars(user_input)}!"
print(f"Tagged output: {tagged_output}")
pyperclip.copy(tagged_output)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print(f"Completion: {get_completion(tagged_output)}")
