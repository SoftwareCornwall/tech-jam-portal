import os
current_folder = os.getcwd()

def list_items(html_file , desc_file):
    with open(html_file , "r") as file:
        with open(desc_file, "r") as desc:
            list_file = str(file.read())
            file = desc.readlines()
            desc_added = list_file.format(description = file[0])
        with open("list_placeholder", "w") as output:
            output.write(desc_added)


file_path = "worksheets/Microbit/microbit_gravity/gravity_microbit_description.txt"
html_file = ("partials/list_item.html")
list_items(html_file , file_path)