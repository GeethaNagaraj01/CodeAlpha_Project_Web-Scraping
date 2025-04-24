import requests
from bs4 import BeautifulSoup
import csv

# List to store all quotes and authors
all_quotes = []

# Start from page 1 and keep scraping until no more quotes are found
page = 1
while True:
    url = f"http://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)

    # Break loop if no more quotes are found (end of pagination)
    if "No quotes found!" in response.text:
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f"Quote: {text}\nAuthor: {author}\n")  # Print to console
        all_quotes.append([text, author])           # Store in list

    page += 1

# Save all quotes to a CSV file
with open('quotes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])  # CSV header
    writer.writerows(all_quotes)          # Write all rows

print("✅ All quotes saved to quotes.csv")
