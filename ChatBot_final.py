import tkinter as tk
from tkinter import scrolledtext
from groq import Groq

client = Groq(
    api_key="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"
)

def get_response(user_input):
    global message
    if user_input.lower() == "exit":
        root.destroy()
        exit()
    message+= "User: "+user_input+"\n"
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role":"user",
                "content":message
            },
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream = True,
        stop=None,
    )
    m=""
    for chunk in completion:
        m += chunk.choices[0].delta.content or ""
    message+= "AI Chatbot: " + m + "\n"
    return m

def send_message():
    user_message = user_entry.get()
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "You: " + user_message + '\n\n')
    user_entry.delete(0, tk.END)

    bot_response = get_response(user_message)
    chat_box.insert(tk.END, "Bot: " + bot_response + "\n\nEnter 'exit' to Close\n\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)

root = tk.Tk()
root.geometry("1000x600")
root.title("Your Friendly Neighbourhood ChatBot")
chat_box = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, height=30, width=500)
chat_box.pack(pady=10)
user_entry = tk.Entry(root, width=400)
user_entry.pack(pady=10, padx=10)
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=10)

message =""

root.mainloop()