# method one:
with open("learning_python.txt") as file_object:
    content = file_object.read()

print(content)
print("\n")

# method two:
with open("learning_python.txt") as files:
    for file in files:
        print(file.strip())
print("\n")

# method three:
with open("learning_python.txt") as f:
    lines = f.readlines()

for line in lines:
    print(line)