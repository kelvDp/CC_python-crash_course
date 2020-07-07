python_glossary = {
    "KEYWORD": "A reserved word the meaning of which cannot be changed by the user.",
    "OPERATOR": "A reserved symbol that indicates an action to be performed.",
    "OBJECT": "An individual thing you can interact with.",
    "VALUE": "An OBJECT that represents a single, concrete thing.",
    "COLLECTION": "An OBJECT that groups together or contains other OBJECTS",
    "CALLABLE":"An OBJECT that represents some action to perform: it performs that action when you call it with some "
               "number of arguments then it returns (or gives back) an OBJECT.",
    "NAME":"Any word that is not a KEYWORD, and that is used as an alias to refer to some specific OBJECT.",
    "EXPRESSION":"Any composite form of one or more of the above that can be evaluated to an OBJECT.",
    "STATEMENT":"Any single line of code that is composed of at least one of the above."
}

for name,defenition in python_glossary.items():
    print(f"{name} :\n\t{defenition}")