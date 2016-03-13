"""
    session 14:10
"""

import easygui


def input_data():
    with open("cal_data.txt", "a") as data:
        msg = "Here you can enter some basic information"
        title = "Get the DATA!"
        fields = ["Fornavn", "Etternavn", "Fødselsdato"]
        data_string = str(easygui.multenterbox(msg, title, fields))
        data_string = data_string.replace("'", "")
        data.write(data_string + ",\n")


def show_data():
    data = open("cal_data.txt", "r")
    easygui.textbox("Here is the data recorded so far:", "Get the data!", data)
    print(data)

    if easygui.ynbox("Do you want to enter more information?", "Get the data!"):
        input_data()
    else:
        pass


input_data()
show_data()


input()




