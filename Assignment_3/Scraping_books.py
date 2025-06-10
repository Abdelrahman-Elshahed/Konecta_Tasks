import requests
import pandas as pd
from bs4 import BeautifulSoup


page = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(page.content, "html.parser")

# print(page.content)  # raw HTML
# print(soup.prettify()) # formatted HTML

def convert_rating(rating_class):
    rating_map = {
        "One": "1/5",
        "Two": "2/5", 
        "Three": "3/5",
        "Four": "4/5",
        "Five": "5/5"
    }
    return rating_map.get(rating_class, "0/5")

all_books = []
books = soup.find_all("article", {"class": "product_pod"})
for book in books:
    Book_Name = book.h3.a["title"]
    Book_Price = book.find("p", {"class": "price_color"}).text
    Book_State = book.find("p", {"class": "instock availability"}).text.strip()
    Book_Rating = convert_rating(book.p["class"][1])  # Rating is now [ x/5 format ]
    all_books.append({
        "Book Name": Book_Name,
        "Book Price": Book_Price,
        "Book State": Book_State,
        "Book Rating": Book_Rating
    })
df = pd.DataFrame(all_books)
print(df)
df.to_excel("Scraping_books.xlsx", index=False)