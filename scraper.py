import requests
from bs4 import BeautifulSoup
import urllib.request

# Send a GET request to the URL
response = requests.get("https://www.nike.com/w/shoes-y7ok")

# Parse the content of the request with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find the first 5 product cards on the page
product_cards = soup.find_all("div", {"class": "product-card__body"}, limit=5)

# For each product card, extract the product name, link, image source, and price
for i, product_card in enumerate(product_cards):
    # Product name
    product_name = product_card.find("div", {"class": "product-card__title"}).text

    # Product link
    product_link = product_card.find("a", {"class": "product-card__link-overlay"})[
        "href"
    ]

    # Image source
    image_src = product_card.find("img", {"class": "product-card__hero-image"})["src"]

    # Download the image
    urllib.request.urlretrieve(image_src, f"product_{i}.jpg")

    # Product price
    product_price = product_card.find("div", {"class": "product-price"}).text

    # Make a request to the individual product page
    product_response = requests.get(product_link)

    # Parse the content of the product page
    product_soup = BeautifulSoup(product_response.text, "html.parser")

    # Find the product description
    product_description = product_soup.find(
        "div", {"class": "description-preview"}
    ).text

    print(f"Product Name: {product_name}")
    print(f"Product Link: {product_link}")
    print(f"Image Link: {image_src}")
    print(f"Product Price: {product_price}")
    print(f"Product Description: {product_description}")
    print("\n-----\n")
