import openai

my_key = "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"

openai.api_key = my_key

def chating(prompt="Hello"):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0
    )
    
    return response.choices[0].text.strip()