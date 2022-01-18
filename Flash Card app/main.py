import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Random word generator
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
    canvas.itemconfig(Title, text="French", fill="black")
    canvas.itemconfig(new_card, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(Title, text="English", fill="white")
    canvas.itemconfig(new_card, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# window
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# canvas
canvas = tkinter.Canvas(height=526, width=800)
card_front = tkinter.PhotoImage(file="images/card_front.png")
card_back = tkinter.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
Title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
new_card = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# buttons
right_tick = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_tick, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=0)
wrong_tick = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_tick, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()
window.mainloop()
