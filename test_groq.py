import os
from groq import Groq


def test_groq():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return "GROQ_API_KEY is missing."

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "user",
                "content": "Reply with exactly: Groq is working."
            }
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print(test_groq())
