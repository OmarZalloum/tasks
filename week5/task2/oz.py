import requests, time, random

def reqjoke(num):
    if num == 1:
        jid = int(input("Enter Joke ID: "))
        try:
            joke= requests.get(f"https://official-joke-api.appspot.com/jokes/{jid}")
            joke=joke.json()

            print(f"{joke['setup']}")
            time.sleep(2)
            print(f"{joke['punchline']}")
        except:
            print("Joke not found. Please try again with a valid ID.")
            
    elif num == 2:
        jct = int(input("Enter the number of jokes: "))
        for i in range(jct):
            i= random.randint(1,450)
            #print(i)
            try:
                joke= requests.get(f"https://official-joke-api.appspot.com/jokes/{i}")
                joke=joke.json()

                print(f"{joke['setup']}")
                time.sleep(2)
                print(f"{joke['punchline']}")
                print("##############################")
                time.sleep(3)
            except:
                print("Joke not found. Please try again with a valid ID.")

    else:
        print("Wrong option... Good bye")    



print("Choose from the menu:")
print("1. Request joke by ID.")
print("2. Request number of random jokes.")
x = int(input("Choice: "))
#print(x)
reqjoke(x)