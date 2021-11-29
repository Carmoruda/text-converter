import json
from typing import final

with open(
    "/home/carmen/Documents/Programación/Repos/ascii-traductor/characters.json",
    "r",
) as file:
    ascii_dic = json.load(file)


input_text = input()
final_text = [str(ascii_dic[char]) for char in input_text]
print(" ".join(final_text))