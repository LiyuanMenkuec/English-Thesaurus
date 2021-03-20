import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()
#Start
word=input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()
if len(results) == 0:
    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word.title())
    results = cursor.fetchall()
if len(results) == 0:
    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word.upper())
    results = cursor.fetchall()
#if len(results) == 0:
#    query = cursor.execute("SELECT Expression FROM Dictionary")
#    print(cursor.fetchall())
#    possibleWords=get_close_matches(word, cursor.fetchall())
#    if len(possibleWords) > 0:
#        yOrN = input("Did you mean %s instead? Enter Y if yes, or N if no: " % possibleWords[0])
#        if yOrN == "Y":
#            query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % possibleWords[0])
#            results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("The word doesn't exist. Please double check it.")