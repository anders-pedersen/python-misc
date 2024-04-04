import requests
session = requests.Session()

def fetch_joke():
  url = "https://api.chucknorris.io/jokes/random"
  r = session.get(url)
  return r.json()['value']

# random_joke = fetch_joke()
# print("Random Chuck Norris Joke:")
# print(random_joke)

def fetch_categories():
  url = "https://api.chucknorris.io/jokes/categories"
  r = session.get(url)
  return r.json()

# categories = fetch_categories()
# print("Available joke categories:")
# print(categories)

def fetch_joke_by_category(category):
  url = f"https://api.chucknorris.io/jokes/random?category={category}"
  r = session.get(url)
  return r.json()['value']

random_joke = fetch_joke_by_category("dev")
print("Random Chuck Norris Dev Joke:")
print(random_joke)
