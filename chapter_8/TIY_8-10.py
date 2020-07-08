def send_message(list):
    while list:
        new_list = list.pop()
        print(new_list)
        sent_messages.append(new_list)



messages = ["Hello","World","Ily", "Yolo","eeewDavid"]
print(messages)

sent_messages = []

send_message(messages)
print(f"\n{sent_messages}")