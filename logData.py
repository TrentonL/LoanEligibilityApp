# Appends to data.txt document
# Used for documenting input from form
def write_file(sentence):
    with open("data.txt", "a") as myfile:
        myfile.write(sentence + '; ')


# Appends to data.txt document
# Used for documenting input from form
def new_line():
    with open("data.txt", "a") as myfile:
        myfile.write('\n')
