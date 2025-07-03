from tkinter import *
from tkinter import messagebox, ttk
from googletrans import Translator, LANGUAGES

# Translator object
translator = Translator()

# Create language name <-> code maps
language_dict = {name.title(): code for code, name in LANGUAGES.items()}
language_names = list(language_dict.keys())  # Full names for dropdown

# Translate Function
def translate_text():
    try:
        input_text = text_input.get("1.0"l, END).strip()
        src_lang_name = source_lang.get()
        dest_lang_name = target_lang.get()
        
        if input_text == "":
            messagebox.showwarning("Warning", "Please enter some text!")
            return
        
        src_lang = language_dict.get(src_lang_name)
        dest_lang = language_dict.get(dest_lang_name)

        translated = translator.translate(input_text, src=src_lang, dest=dest_lang)
        text_output.delete("1.0", END)
        text_output.insert(END, translated.text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Window
root = Tk()
root.title("Language Translator")
root.geometry("500x450")
root.config(bg="lightblue")

# Labels
Label(root, text="Enter Text:", font=("Arial", 12)).pack(pady=5)

# Text Input
text_input = Text(root, height=5, width=50)
text_input.pack(pady=5)

# Source Language Dropdown
Label(root, text="From Language:", font=("Arial", 12)).pack()
source_lang = ttk.Combobox(root, values=language_names)
source_lang.set("English")  # default
source_lang.pack()

# Target Language Dropdown
Label(root, text="To Language:", font=("Arial", 12)).pack()
target_lang = ttk.Combobox(root, values=language_names)
target_lang.set("Urdu")  # default
target_lang.pack()

# Translate Button
Button(root, text="Translate", command=translate_text, bg="green", fg="white", font=("Arial", 12)).pack(pady=10)

# Output Label
Label(root, text="Translated Text:", font=("Arial", 12)).pack()

# Text Output
text_output = Text(root, height=5, width=50)
text_output.pack(pady=5)

# Run the App
root.mainloop()
