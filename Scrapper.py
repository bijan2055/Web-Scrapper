# Web Scrapping Project...

import requests
from bs4 import BeautifulSoup
import json

# URL to scrape...
url = "https://books.toscrape.com/"

# scrape book named function..

def scrape_book(url):
    response = requests.get(url)
    if response.status_code != 200:
        return 
    
    response.encoding = response.apparent_encoding # yo lekhe pachi ananda le rendering garna sakyo... 

    print (response.text)
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_ = "product_pod" )


    book_list = [] # to store book data.. 

    for book in books:
        title = book.h3.a['title']
        price_text = book.find("p",class_ = "price_color").text
        currency = price_text[0]
        price = price_text[1:]
        # aaba katai store garnu paryonta jhikeko data, we now store the data.. 
        # We store it in JSON format... 
        # save to JSON file...
        book_data = {'Title':title,'Currency':currency,'Price':price}
        book_list.append(book_data)
    # Save to JSON file.. 
 
    with open("books.json","w",encoding = "utf-8") as f:
        json.dump(book_list,f, ensure_ascii=False, indent = 4)

    print (f"Saved{len(book_list)} books to books.json")


# scrape_book(url) # Response [200] bhanya chai data paye bhanya hoo..
# # status code 200 bhayo bhane matra kaam suru garne..
scrape_book(url)