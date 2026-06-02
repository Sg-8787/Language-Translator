from tkinter import *
from tkinter import ttk
from googletrans import Translator

translator = Translator()

languages = {
    "Hindi": "hi",
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-cn"
}

def translate_text():
    text = input_text.get("1.0", END)

    if text.strip():
        lang_name = lang_var.get()
        lang_code = languages[lang_name]

        translated = translator.translate(
            text,
            dest=lang_code
        )

        output_text.delete("1.0", END)
        output_text.insert(
            END,
            translated.text
        )

def clear_text():
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)

root = Tk()
root.title("Language Translator")
root.geometry("750x550")
root.config(bg="#EAF4FF")

# Heading
Label(
    root,
    text="🌍 Language Translator",
    font=("Arial", 22, "bold"),
    bg="#EAF4FF"
).pack(pady=15)

# Input Label
Label(
    root,
    text="Enter Text",
    font=("Arial", 12, "bold"),
    bg="#EAF4FF"
).pack()

# Input Box
input_text = Text(
    root,
    height=8,
    width=70,
    font=("Arial", 12)
)
input_text.pack(pady=10)

# Language Dropdown
lang_var = StringVar()
lang_var.set("Hindi")

ttk.Label(
    root,
    text="Select Language"
).pack()

dropdown = ttk.Combobox(
    root,
    textvariable=lang_var,
    values=list(languages.keys()),
    state="readonly",
    width=20
)
dropdown.pack(pady=10)

# Buttons Frame
frame = Frame(root, bg="#EAF4FF")
frame.pack()

Button(
    frame,
    text="Translate",
    command=translate_text,
    font=("Arial", 11, "bold"),
    padx=20
).grid(row=0, column=0, padx=10)

Button(
    frame,
    text="Clear",
    command=clear_text,
    font=("Arial", 11, "bold"),
    padx=20
).grid(row=0, column=1, padx=10)

# Output Label
Label(
    root,
    text="Translated Text",
    font=("Arial", 12, "bold"),
    bg="#EAF4FF"
).pack(pady=10)

# Output Box
output_text = Text(
    root,
    height=8,
    width=70,
    font=("Arial", 12)
)
output_text.pack()

root.mainloop()