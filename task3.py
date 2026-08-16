message = "&&&**$gnirtS PLIO!!@1234"
core = message.strip("&*$!@0123456789")  
words = core.split()
first_word = words[0][::-1]  
second_word = words[1].replace("I", "E").replace("O", "U")  

final_message = f"{first_word} {second_word}"
print(final_message)