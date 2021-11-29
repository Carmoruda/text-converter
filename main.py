import json
from typing import final
from tkinter import *

with open(
    "/home/carmen/Documents/Programación/Repos/ascii-traductor/characters_dictionary.json",
    "r",
) as file:
    char_dict = json.load(file)
    char_keys = list(char_dict.keys())
    char_values = list(char_dict.values())

root = Tk()


def clear_entries():
    ascii_entry.delete(0, END)
    text_entry.delete(0, END)


def convert_to_text():
    input_list = ascii_entry.get().split()
    final_text = []
    for element in input_list:
        dict_postion = char_values.index(int(element))
        final_text.append(char_keys[dict_postion])
    text_entry.insert(0, "".join(final_text))


def convert_to_ascii():
    final_text = [str(char_dict[char]) for char in text_entry.get()]
    ascii_entry.insert(0, " ".join(final_text))


def menu(action):
    print(action)
    if action == "Text":
        convert_to_text()
    elif action == "ASCII":
        convert_to_ascii()


text_label = Label(root, text="Text: ")
text_label.grid(row=0, column=0)
text_entry = Entry(root, borderwidth=5)
text_entry.grid(row=0, column=1, columnspan=2)

ascii_label = Label(root, text="ASCII: ")
ascii_label.grid(row=1, column=0)
ascii_entry = Entry(root, borderwidth=5)
ascii_entry.grid(row=1, column=1, columnspan=2)

mode_label = Label(root, text="Convert to: ")
mode_label.grid(row=2, column=0)

convert_button = Button(
    root,
    text="Convert",
    command=lambda: menu(mode.get()),
)
convert_button.grid(row=3, column=1)

mode = StringVar()
to_text_action = Radiobutton(root, text="Text", variable=mode, value="Text")
to_ascii_action = Radiobutton(root, text="ASCII", variable=mode, value="ASCII")
mode.set("Text")
to_text_action.grid(row=2, column=1)
to_ascii_action.grid(row=2, column=2)

clear_button = Button(root, text="Clear", command=clear_entries)
clear_button.grid(row=4, column=1)

root.mainloop()