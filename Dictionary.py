import json
from difflib import get_close_matches

#Data von Wörterbuch öffnen
data = json.load(open("data.json"))

#ein eingegebenes Wort in Data zu suchen
def translate(wordOfInput):
    wordOfInput = wordOfInput.lower()
    if wordOfInput in data:
        return data[wordOfInput]
    elif wordOfInput.title() in data:
        return data[wordOfInput.title()] 
    elif wordOfInput.upper() in data:  
        return data[wordOfInput.upper()]    
    elif len(get_close_matches(wordOfInput, data.keys())) > 0:
        yOrN = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(wordOfInput, data.keys())[0])
        if yOrN == "Y":
            return data[get_close_matches(wordOfInput, data.keys())[0]]
        elif yOrN == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

#Start des Programmes
word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
