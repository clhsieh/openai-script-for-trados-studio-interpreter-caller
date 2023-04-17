import argparse

import openai

from configs import OPENAI_API_KEY

parser = argparse.ArgumentParser(description="Openai translator for Trados Studio Interpreter Caller")
parser.add_argument("number", type=str)
parser.add_argument("source_text", type=str)
parser.add_argument("target_text", type=str)
parser.add_argument("status", type=str)
parser.add_argument("meta_data_list", type=str, nargs="*")

def main():
    args = parser.parse_args()
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Translate this into 1. Traditional Chinese 2. Simplified Chinese:\n\n{args.source_text}\n\n1.",
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    choices = response.get("choices", [])
    if not choices:
        print("Something error...")
    else:
        choice = choices[0]["text"]
        result = choice.split("\n")[0].strip()
        print(result)


if __name__ == "__main__":
    main()