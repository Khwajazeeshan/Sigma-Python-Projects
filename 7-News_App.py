# Making App In Python......../////////////
"""
Using requests Module, json Module And API Key Of News App.
"""
import requests
import json

query = input("What Type Of News U Want To Learn: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-07-24&sortBy=publishedAt&apiKey=260b825adbbb4c62803c972376f941f5"
result = requests.get(url)
news = json.loads(result.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("\t-------------------------------")
