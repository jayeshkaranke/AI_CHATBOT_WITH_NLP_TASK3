import tkinter as tk
from tkinter import scrolledtext
import openai

# 🔐 Your OpenAI API Key (REPLACE this with your actual key)
openai.api_key = "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"

# Function to get response from OpenAI GPT
def get_gpt_response(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # You can use "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful and friendly AI chatbot."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Function to handle message sending
def send_message():
    user_msg = user_input.get()
    if not user_msg.strip():
        return
    chat_window.insert(tk.END, "You: " + user_msg + "\n", "user")
    user_input.delete(0, tk.END)

    bot_response = get_gpt_response(user_msg)
    chat_window.insert(tk.END, "Bot: " + bot_response + "\n", "bot")
    chat_window.see(tk.END)

# GUI setup
root = tk.Tk()
root.title("CodTech Smart Chatbot (GUI)")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_window.pack(padx=10, pady=10)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

user_input = tk.Entry(root, width=50, font=("Arial", 12))
user_input.pack(padx=10, pady=(0, 10), side=tk.LEFT, expand=True, fill=tk.X)

send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(padx=10, pady=(0, 10), side=tk.RIGHT)

root.mainloop()
