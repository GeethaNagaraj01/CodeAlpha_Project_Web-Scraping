# CodeAlpha_Project_Web-Scraping

🕸️ Web Scraping Project - Quotes to Scrape

## 📌 Objective

The goal of this project is to make web scrape with tools provided by Python, such as `requests` and `BeautifulSoup`. The target website is [quotes.toscrape.com](http://quotes.toscrape.com/), a site that has been created exclusively for the purpose of practicing web scraping.

The script collects:
- Quotes
- Authors

The collected information is stored in a structured `.csv` file, to be used at a later stage for analysis or any text-based project.

---

## 🌐 Website Scraped

- **URL**: [http://quotes.toscrape.com](http://quotes.toscrape.com)
- **Description**: A mock site created for web scraping practice. This site has pages of famous quotes with their authors and additional metadata such as tags and author links. 

---

## 📊 Data Collected

Each dataset has a row in `quotes.csv` that follows the structure of:

- **Quote**: This is the text of the quote.
- **Author**: The person who uttered the quote.

The Python script traverses all pages available in the website and stores each corresponding quote/author pair.

---

## 📁 Files in this Repo

| File Name        | Description                                |
|------------------|--------------------------------------------|
| `scrape_quotes.py` | Python script to scrape the quotes        |
| `quotes.csv`     | Output CSV containing quotes and authors   |
| `README.md`      | Project overview and submission description |

---

## ⚙️ Tools Used

- Python
- `requests` - to send HTTP requests
- `BeautifulSoup` - to parse HTML content
- `csv` - to save data to a CSV file

---

## ⚠️ Challenges Faced

- **Pagination Handling**: The site has quotes spread across multiple pages. A loop had been implemented to keep scraping until the message "No quotes found!" appeared, signaling an end.
- **Character Encoding**: Some quote text includes curly quotes and special characters, which demanded UTF-8 encoding when saving to the CSV.
- **Consistent Structure**: Fortunately, the HTML structure is clean and consistent throughout the website and allows easy scraping. 

---

## ✅ Output Example

Sample rows from `quotes.csv`:

| Quote                                                                                       | Author           |
|---------------------------------------------------------------------------------------------|------------------|
| “The world as we have created it is a process of our thinking...”                          | Albert Einstein  |
| “It is our choices, Harry, that show what we truly are, far more than our abilities.”      | J.K. Rowling     |

---

## 📌 Future Work

- Add tags associated with quotes as a third column
- Call the author bio pages and scrape additional information (birthplace, date, etc.)
- Perform sentiment analysis or keyword extraction on the quotes

---

> Made for educational purposes using the practice site [Quotes to Scrape](http://quotes.toscrape.com/).

![Screenshot from 2025-04-24 21-42-26](https://github.com/user-attachments/assets/e35ffe62-b545-4504-ba8b-f9bac2624ccd)

![Screenshot from 2025-04-24 21-42-26-1](https://github.com/user-attachments/assets/1a5ba129-9e7a-4220-8937-664bab8d9370)


![Screenshot from 2025-04-24 21-42-39](https://github.com/user-attachments/assets/77eb5832-866a-4b1b-b937-9552176a38e3)


![Screenshot from 2025-04-24 21-42-54](https://github.com/user-attachments/assets/d5aace2d-c5bc-4650-9ac5-675c25c1727c)

![Screenshot from 2025-04-24 21-43-06](https://github.com/user-attachments/assets/99d92eeb-f258-4794-951e-72beab57fd05)

![Screenshot from 2025-04-24 21-43-47](https://github.com/user-attachments/assets/d807d85a-2961-44f6-b73f-7582ae6fc9e2)


![Screenshot from 2025-04-24 21-44-02](https://github.com/user-attachments/assets/03e4769d-db67-4e50-a430-18488b921d0c)
![Screenshot from 2025-04-24 21-44-13](https://github.com/user-attachments/assets/980c189d-54e5-445f-89e4-948614693c2a)


![Screenshot from 2025-04-24 21-44-30](https://github.com/user-attachments/assets/bc1446fd-0084-4f48-868e-5279193508da)

![Screenshot from 2025-04-24 21-44-23](https://github.com/user-attachments/assets/08c681a0-7a48-45fa-ab1c-3c3a52e00f2f)
[Screencast from 2025-05-12 19-27-13.webm](https://github.com/user-attachments/assets/4f2ce6c9-9cbe-41a0-a7f7-74e571bef414)
