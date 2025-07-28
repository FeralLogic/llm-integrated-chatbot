import openai
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
api_key = config.get("chatgpt", "apikey")

def main():
    print(api_key)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'}]

def try1():
    response = get_completion_from_messages(messages, temperature=1)
    print(response)




if __name__ == "__main__":
    try1()
