# import openai
import configparser
import requests
import json
import tkinter as tk
# from tkinter import messagebox
from tkinter import Label, Tk
from tkinter import Text,Tk
from tkinter import Button

config = configparser.ConfigParser()
config.read("config.ini")
# api_key = config.get("chatgpt", "apikey")


'''
# function to display chatbot response in GUI
def show_chatbot_response():
    user_input = user_input_box.get("1.0", END)
    user_input_box.delete("1.0", END)

    if user_input.lower() in ["exit", "quit", "bye"]:
        chat_history.insert(tk.END, "Chatbot: Goodbye!\n")
        return
    
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    chatbot_response = get_chatbot_response(user_input)
    chat_history.insert(tk.END, "Chatbot: " + chatbot_response + "\n")
'''

# tkinter GUI
root = tk.Tk()
root.title("Chatbot Window")
root.geometry("500x300")
root.configure(bg= "light blue")

# Heading text
heading = Label(root, 
                text = "Hi! I'm a customer service agent. I can help with your questions.",
                font = ("Arial", 12, "bold")
)
heading.place(x=10, y=5)

# chat history box
chat_history = Text(root, fg='black', border= 2, bg='white', height=10, width=50)
chat_history.place(x=10, y=60)

'''
#scroll bar
scrollbar = scrollbar(chat_history)
scrollbar.place(relheight =1, relx =.974)
scrollbar = (command= chat_history.yview)
'''

# bottom chat entry box

user_input_box = Text(root,height = 3, width = 50, padx=.5)
user_input_box.place(x=10, y= 235)

# send button
send_button = Button(root, text = "Send", font ="bold", bg="grey", command= show_chatbot_response)
send_button.place(x= 430, y= 242)


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
Current rental rates are available on our website or by contacting the community directly.\
The community features a resort style swimming pool, pickleball court, and a fitness center\
Finish your responce by asking what else you can help with.\
If you can not help invite them to contact the office directly.\
If they ask about pets you can give them the below pet info\
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
                "content": "You are an apartment manager. Use the context to very briefly answer user queries. No more than 2 sentences. \n\nCONTEXT:\n" + context
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
    prompt = "Do you have 1 bedroom apartments?"
    result = query_ollama(prompt)
    print(result)




if __name__ == "__main__":
    main()
