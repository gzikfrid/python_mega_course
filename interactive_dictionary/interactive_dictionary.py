import json
from difflib import get_close_matches

data  = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        answer = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0])
        answer = answer.lower()
        if answer == "y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "The word does not exist. Please try again."
    else:
        return "The word does not exist. Please try again."

word = input("Enter word: ")

result = translate(word)

if type(result) == list:
    for i in result:
        print(i)
else:
    print(result)
