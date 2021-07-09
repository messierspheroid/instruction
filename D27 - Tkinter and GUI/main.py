import tkinter
# http://tcl.tk/man/tcl8.6/TkCmd/contents.htm

def button_clicked():
    # print("I got clicked")
    new_text = user_input.get()
    my_label.config(text=new_text)

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="New Text", font=("Arial", 24, "bold"))
# my_label.pack() <-- not many positional args
# my_label.place(x=100, y=0) <-- specific coordinates
my_label.grid(column=0, row=0) # similar to designating cells in an excel document
my_label.config(padx=50, pady=50)


button_1 = tkinter.Button(text="Click Me", command=button_clicked)
button_1.grid(column=1, row=1)

button_2 = tkinter.Button(text="Click Me", command=button_clicked)
button_2.grid(column=2, row=0)

# # advanced arguments, create arguments that have default values
# def my_function(a=x, b=y, c=z):
# # if you want to change the variables, do so when you call the function
# my_function(b=w)

# # unlimited arguments (*args is a tuple), this for loop will allow as many variables as you want
# def add(*args):
#     for n in args:
#         print(n)
# add(3, 5, 7, 8)

user_input = tkinter.Entry(width=10)
user_input.grid(column=3, row=2)


window.mainloop()
