import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

print("Status code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

books = []

for book in soup.select("article.product_pod"):
    title = book.h3.a["title"]
    price = book.select_one(".price_color").text.strip()
    availability = book.select_one(".availability").text.strip()

    rating_tag = book.select_one("p.star-rating")
    rating = rating_tag.get("class")[1]

    # Remove the currency symbol and keep only the numeric price
    price = price.replace("Â£", "").replace("£", "").strip()

    books.append({
        "Title": title,
        "Price": float(price),
        "Availability": availability,
        "Rating": rating
    })

df = pd.DataFrame(books)

df.to_csv("books_dataset.csv", index=False, encoding="utf-8-sig")

print("Dataset created successfully!")
print("Number of records:", len(df))

print("\nFirst 5 records:")
print(df.head())