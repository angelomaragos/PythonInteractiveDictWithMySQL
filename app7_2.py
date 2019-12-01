import mysql.connector

from difflib import get_close_matches

con = mysql.connector.connect(
    user='***',
    password='***',
    host='***',
    database='***'
)

cursor = con.cursor()


def translate():
    word = input("Enter word: ")
    x = word
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
    results = cursor.fetchall()
    if (len(results)) == 0:
        print("I didn't find a word in the dictionary with that spelling. Searching for a close match")
        print('..........')
    if results:
        print("")
        for result in results:
            print(result[1])
        print("")
    elif (len(results)) == 0:
        query = cursor.execute("SELECT * FROM Dictionary")
        results = cursor.fetchall()
        results2 = []
        for result in results:
            results2.append(result[0])
        if len(get_close_matches(word, results2)) > 0:
            yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, results2)[0])
            x = get_close_matches(word, results2)[0]
            if yn.upper() == 'Y':
                print("")
                query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % x)
                results = cursor.fetchall()
                for result in results:
                    print(result[1])
                print("")
            elif yn.upper() == 'N':
                print("The word doesn't exist. Please double check it")
            else:
                print("Invalid input. Try again")


translate()
