from tkinter import *
import pandas
import random

# google sheets translation list generator; col1 = fr, es...., col2 = Eng
#     col2 = googletranslate(*follow prompts*)

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_TITLE_FONT = ("Arial", 40, "italic")
LANGUAGE_CLUE_FONT = ("Arial", 60, "bold")
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_png)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_png)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# row 0
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_png = PhotoImage(file="images/card_front.png")
card_back_png = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_png)
card_title = canvas.create_text(400, 150, text="", fill="black", font=LANGUAGE_TITLE_FONT)
card_word = canvas.create_text(400, 263, text="", fill="black", font=LANGUAGE_CLUE_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# row 1
unknown_button_png = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_png, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

known_button_png = PhotoImage(file="images/right.png")
known_button = Button(image=known_button_png, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
