import tkinter

FONT = ("Arial")


def calculate():
    miles = float(user_input.get())
    km = miles * 1.609
    miles_input_label.config(text=f"{km}")


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# row 1
blank_label = tkinter.Label()
blank_label.grid(column=0, row=0)

user_input = tkinter.Entry(width=10)
user_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

# row 2
is_equal_to_label = tkinter.Label(text="is equal to", font=FONT)
is_equal_to_label.grid(column=0, row=1)

miles_input_label = tkinter.Label(text=0, justify="center", font=FONT)
miles_input_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

# row 3
calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()
