import re
while(True):
    statement = input("Enter a statement:\n")
    matches = re.findall(r"(?P<position>\w+)\sletter\sis\s(?P<letter>\w)", statement)
    print(matches)
    # positions = [index for index, word in enumerate(match) if word == "letter"]
    # print(positions)
    letter_dict = {}
    for match in matches:
        postition, letter = match
        letter_dict[postition] = letter
    
    for letter_dict_pass in letter_dict.values():
        print(letter_dict_pass)