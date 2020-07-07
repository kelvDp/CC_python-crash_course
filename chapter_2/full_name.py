first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"  #this is how to format a string in order to place a variable inside without concatenating

print(f"Hello,{full_name.title()}")

#another way of doing the above is to assign everything to a var and simply print the var name:

message = f"Hello, {full_name.title()}"

print(message)  