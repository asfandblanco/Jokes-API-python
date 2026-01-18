import requests
jokes = requests.get("https://v2.jokeapi.dev/joke/Any?lang=en")

prueba = jokes.json()["type"]

if (prueba == "single"):
    meme = jokes.json()["joke"]
    print(meme)
elif (prueba == "twopart"):
    one = jokes.json()["setup"]
    print(one)
    two = jokes.json()["delivery"]
    print(two)