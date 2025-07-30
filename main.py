# import openai
import configparser
import requests
import json
import tkinter as tk

config = configparser.ConfigParser()
config.read("config.ini")
# api_key = config.get("chatgpt", "apikey")

# tkinter GUI
root = tk.Tk()
root.title("Chatbot Window")
root.mainloop()

ollama_host = config.get("ollama", "host")
ollama_url = config.get("ollama", "url")
ollama_model = config.get("ollama", "model")
context = """
The apartment community is called Baxter Court Luxury Apartment Homes\
There are 300 units\
The community consists of one bedroom, two bedroom, and three bedroom apartment homes\
The one bedroom floor plan is 700 squarefeet\
The two bedroom floor plan is 900 squarefeet\
The three bedroom floor plan is 1150 squarefeet\
All units have a full-size washer and dryer included\
The community features a resort style swimming pool, pickleball court, and a fitness center\
Pets are allowed with certain breed restrictions\
Max of 2 pets per home\
The pet fee is a one-time fee of $150\
The pet rent is $25 per month per pet\

"""

# create function to query the ollama server with a chat prompt
def query_ollama(prompt):
    # notify user of host and model, will act as a test
    print(f'We are using Ollama and the model {ollama_model}')
    # calls the ollama server's chat function
    url = f'{ollama_url}/api/chat'
    # create a dictionary with the model and the message, payload is what is sent to the server
    payload = {
        "model": ollama_model,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful apartment community leasing agent, use the context to brifly answer any user queries.\n\nCONTEXT:\n" + context
            },
            {
                 "role": "user",
                 "content": prompt
            }
        ],
        "temperature": .2
    }
    # send a post to the server, assign response to variable
    response = requests.post(url, json=payload, stream=True)
    # checks for an http error
    response.raise_for_status()

    # create a new variable to look for json and handle errors in response
    full_reply = ""
    for line in response.iter_lines(decode_unicode=True):
        if line:
            try:
                data = json.loads(line)
                if "message" in data and "content" in data["message"]:
                    full_reply += data["message"]["content"]
            except json.JSONDecodeError as e:
                print("Skipping invalid JSON line:", line)
    return full_reply


def main():
    prompt = "Tell me about your 1 bedroom apartments"
    result = query_ollama(prompt)
    print(result)

'''
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
   
'''
'''
messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'}]
'''



if __name__ == "__main__":
    main()
