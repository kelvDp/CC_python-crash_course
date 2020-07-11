with open("learning_python.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.lower().replace("python","C")
    print(line.strip())