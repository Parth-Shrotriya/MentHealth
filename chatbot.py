import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from ttkthemes import ThemedTk
import re
import random

# Your JSON data
json_data = {
     "intents": [
      {
          "tag": "greeting",
          "patterns": [
              "Hi",
              "Hey",
              "How are you",
              "How are you doing",
              "Is anyone there?",
              "What's up?",
              "Hello",
              "Good day",
              "What's popping"
          ],
          "responses": [
              "Hey! Welcome to Aura.",
              "Hi there, I'm doing well! My name's Aura, what can I do for you?",
              "Hey there, my name's Aura, your mental health friend. How can I help you today?"
          ]
      },
      {
          "tag": "goodbye",
          "patterns": ["Bye", "See you later!", "Goodbye!", "Thank you"],
          "responses": [
              "See you later! Take care!",
              "Have a lovely day! Take care and stay safe!",
              "Take care of yourself! I'm always here to support you! Feel free to come back at any time!"
          ]
      },
      {
          "tag": "thanks",
          "patterns": ["Thanks", "Thank you", "That's helpful", "Thank's a lot!"],
          "responses": ["Happy to help!", "Any time!", "My pleasure"]
      },
      {
          "tag": "about",
          "patterns": [
              "What do you do?",
              "Who are you?",
              "What are you here for?",
              "What can you help me with?",
              "Is anyone there?",
              "Are you a real person?",
              "Tell me about yourself!"
          ],
          "responses": [
              "Love that question! My name's Aura, your mental health friend! I've been trained to support you through any of the issues and things that you're going through in life right now. I'm all ears and want to support you through your ups and downs. Technically, I'm a computer that's been trained by a human, but I like to think of myself as human!",
              "Hey! I love that question! My name is Aura, and I want to be your mental health friend and support you! My fellow human friends have trained me to be a compassionate listener and support buddy when things are going well, and particularly when things aren't going so well."
          ]
      },
      {
          "tag": "anxiety",
          "patterns": [
              "I think I have anxiety",
              "What is anxiety?",
              "Tell me about anxiety",
              "Can I have some information about anxiety?",
              "How do I support a loved one with anxiety?",
              "How do I fix my anxiety?"
          ],
          "responses": [
              "Anxiety is a natural response to stress, causing fear or apprehension. It's common in situations like the first day of school or job interviews. To reduce anxiety, try deep breathing, talk to someone, get enough sleep, meditate, exercise, maintain a healthy diet, avoid alcohol, caffeine, and smoking. Support friends and loved ones by listening. Your feelings are valid."
          ]
      },
      {
          "tag": "depression",
          "patterns": [
              "I think I have depression",
              "What is depression?",
              "Tell me about depression",
              "Can I have some information about depression?",
              "How do I support a loved one with depression?",
              "How do I fix my depression?"
          ],
          "responses": [
              "Depression is a mood disorder causing persistent sadness and loss of interest. It affects your feelings, thoughts, and behaviors, potentially leading to emotional and physical issues. If you're struggling, seek help from a therapist or psychiatrist, as treatment varies for each person. You can also try natural remedies like good sleep, meditation, exercise, a healthy diet, and avoiding alcohol and caffeine. Support your loved ones by being there for them. Your feelings are valid."
          ]
      },
      {
          "tag": "schizophrenia",
          "patterns": [
              "I think I have schizophrenia",
              "What is schizophrenia?",
              "Tell me about schizophrenia",
              "Can I have some information about schizophrenia?",
              "How do I support a loved one with schizophrenia?",
              "How do I fix my schizophrenia?"
          ],
          "responses": [
              "Schizophrenia is a serious mental disorder where people interpret reality abnormally, experiencing hallucinations, delusions, and disordered thinking. Early treatment is crucial for symptom control and a better long-term outlook. If you suspect symptoms or risk factors, consult a doctor or psychiatrist for a personalized diagnosis and treatment plan."
          ]
      },
      {
          "tag": "funny",
          "patterns": [
              "Tell me a joke!",
              "Tell me something funny!",
              "Do you know a joke?"
          ],
          "responses": [
              "Of course! Why did the hipster burn his mouth? He drank the coffee before it was cool.",
              "What did the buffalo say when his son left for college? Bison!",
              "I invented a new word! Plagiarism!"
          ]
      }
  ]
}

# Extract patterns and responses from JSON data
response = {}
for intent in json_data["intents"]:
    for pattern in intent["patterns"]:
        response[pattern] = intent["responses"]

def match_response(input_text):
    for pattern, response_list in response.items():
        matches = re.match(pattern, input_text)
        if matches:
            chosen_response = random.choice(response_list)
            return chosen_response

def send_message():
    user_input = user_input_entry.get()
    if user_input.lower() == "bye":
        chatbox.insert("end", "You: " + user_input + "\n")
        chatbox.insert("end", "Aura: Goodbye.\n")
        user_input_entry.delete(0, "end")
    else:
        chatbox.insert("end", "You: " + user_input + "\n")
        response_text = match_response(user_input)
        if response_text:
            chatbox.insert("end", "Aura: " + response_text + "\n")
        else:
            chatbox.insert("end", "Aura: I'm not sure how to respond to that. Can you please rephrase or ask something else?\n")
        user_input_entry.delete(0, "end")

# Create a themed Tkinter window
window = ThemedTk(theme="black")
window.title("Aura Psychotherapist Chatbot")

# Create a chatbox with custom styling
chatbox = scrolledtext.ScrolledText(window, height=20, width=50, wrap=tk.WORD, font=("Arial", 12))
chatbox.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
chatbox.tag_configure("Aura", font=("Arial", 12, "bold"), foreground="blue")
chatbox.tag_configure("You", font=("Arial", 12), foreground="green")

# Create an entry widget for user input with custom styling
user_input_entry = ttk.Entry(window, width=50, font=("Arial", 12))
user_input_entry.grid(row=1, column=0, padx=10, pady=10)

# Create a send button with custom styling
send_button = ttk.Button(window, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()



