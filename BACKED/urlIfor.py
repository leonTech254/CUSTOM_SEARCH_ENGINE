import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage's URL and retrieve its HTML content


class previewUrl:
    def search(url):
        try:
            response = requests.get(url)
            html_content = response.content

            # Parse the HTML content using Beautiful Soup
            soup = BeautifulSoup(html_content, "html.parser")

            # Find the title of the webpage
            title = soup.title.text

            # Find all links on the webpage and store them in a list
            links = []
            for link in soup.find_all("a"):
                href = link.get("href")
                links.append(href)

            # find paragraphs
            paragraphs = []
            for paragraph in soup.find_all("p"):
                text = paragraph.get_text()
                paragraphs.append(text)

            item_with_most_words = max(paragraphs, key=len)

            # Printing the item with the most words
            return item_with_most_words
        except:
            return False
