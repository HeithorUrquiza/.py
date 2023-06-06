from bs4 import BeautifulSoup
import requests

resp = requests.get("https://news.ycombinator.com/")
yc_web_page = resp.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles= soup.find_all(name="span", class_ = "titleline")
article_texts = []
article_links = []

for article in articles:
    article_texts.append(article.a.getText())
    article_links.append(article.a['href'])
    
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_value = max(article_upvotes)
index = article_upvotes.index(max_value)

print(article_texts[index]) 
print(article_links[index])
print(article_upvotes[index])







""" with open("Projects/Intermediate/bs4/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.prettify()) """

