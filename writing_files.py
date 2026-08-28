# Python writing files (.txt, .json, .csv)

txt_data = "I like Chicken Biryani"
file_path = "C:\\Users\\adity\\Desktop\\output.txt"

try:
    with open(file = file_path, mode = "a") as file:
        file.write("\n" + txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")
