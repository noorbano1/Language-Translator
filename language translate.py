from tkinter import *
from tkinter import messagebox, ttk
from deep_translator import GoogleTranslator

# Language list
languages = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Arabic": "ar",
    "Hindi": "hi",
    "Spanish": "es"
}

# Translate Function
def translate_text():
    try:
        input_text = text_input.get("1.0", END).strip()

        if input_text == "":
            messagebox.showwarning("Warning", "Please enter some text!")
            return

        src = languages[source_lang.get()]
        dest = languages[target_lang.get()]

        translated = GoogleTranslator(source=src, target=dest).translate(input_text)

        text_output.delete("1.0", END)
        text_output.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = Tk()
root.title("Language Translator")
root.geometry("500x450")
root.config(bg="lightblue")

Label(root, text="Enter Text:", font=("Arial", 12), bg="lightblue").pack()
text_input = Text(root, height=5, width=50)
text_input.pack(pady=5)

Label(root, text="From Language:", bg="lightblue").pack()
source_lang = ttk.Combobox(root, values=list(languages.keys()), state="readonly")
source_lang.set("English")
source_lang.pack()

Label(root, text="To Language:", bg="lightblue").pack()
target_lang = ttk.Combobox(root, values=list(languages.keys()), state="readonly")
target_lang.set("Urdu")
target_lang.pack()

Button(root, text="Translate", command=translate_text,
       bg="green", fg="white", font=("Arial", 12)).pack(pady=10)

Label(root, text="Translated Text:", bg="lightblue").pack()
text_output = Text(root, height=5, width=50)
text_output.pack(pady=5)

root.mainloop()
