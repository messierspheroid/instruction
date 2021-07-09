# read a file
with open("../../Desktop/my_file.txt", ) as file:
    contents = file.read()
    print(contents)

# # write to a file
# # mode="w" == erase all and write new text, ="a" == append to current text
# # if you are in the "w" mode and you want to create a new file
# with open("new_file.txt", mode="w") as file:
#     file.write("New text")

# absolute file path always starts from the root /folder/..../folder/file
# relative file path always starts from the working directory
# ./folder/file

# access a file towards the root ../file
