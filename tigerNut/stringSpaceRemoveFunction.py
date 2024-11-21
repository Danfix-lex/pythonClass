def get_message_space_remove(message):
    message = message.replace(" ", "")
    return message

message = "hello world"
result = get_message_space_remove(message)
print(result)

