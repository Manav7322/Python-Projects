import tkinter as tk
import pyjokes

def get_jokes():
    joke = pyjokes.get_joke()
    joke_label.config(text=joke)

root = tk.Tk()
root.title("programming joke generator")
root.geometry("500x200")

joke_label=tk.Label(root,text="Click the Button for a Joke!", wraplength=400,justify="center",font=("Arial",12))
joke_label.pack(pady=20)

joke_button=tk.Button(root, text="Tell me a Joke", command=get_jokes,font=("Arial", 12))
joke_button.pack()

root.mainloop()