from bs4 import BeautifulSoup
import requests
from urlIfor import previewUrl


class Scrapper:
    def search_google(query, num_results=10, lang="en"):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/61.0.3163.100 Safari/537.36'
        }
        escaped_query = query.replace(' ', '+')
        google_url = f'https://www.google.com/search?q={escaped_query}&num={num_results}&hl={lang}'
        response = requests.get(google_url, headers=headers)
        response.raise_for_status()
        results = Scrapper.parse_google_results(response.text)
        return results

    def parse_google_results(html):
        soup = BeautifulSoup(html, 'html.parser')
        result_block = soup.find_all('div', attrs={'class': 'g'})

        results = []
        for result in result_block:
            link = result.find('a', href=True)
            if link:
                title = result.find('h3')
                snippet = result.find('span', attrs={'class': 'aCOpRe'})

                if title:
                    title = title.text.strip()
                else:
                    title = ''

                if snippet:
                    snippet = snippet.text.strip()
                    # get the first 30 words of the snippet
                    snippet_words = snippet.split()[:30]
                    snippet = ' '.join(snippet_words) + \
                        '...' if len(snippet_words) == 30 else snippet
                else:
                    snippet = ''
                snippet = previewUrl.search(link['href'])
                if snippet:
                    results.append({
                        'title': title,
                        'url': link['href'],
                        'snippet': snippet
                    })

        return results

    def query(user_query):
        results_array = []
        results = Scrapper.search_google(user_query)
        for result in results:
            results_array.append(result)
            print(
                f"{result['title']}\n{result['url']}\n{result['snippet']}\n\n")
        return results_array
