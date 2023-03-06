from commoncrawl import CommonCrawl
import re
import random

# Define the search terms and keywords
search_terms = ['COVID-19', 'coronavirus', 'pandemic']
economic_keywords = ['economic', 'finance', 'business', 'unemployment', 'recession', 'job loss']

def filter_urls(urls):
    filtered_urls = []
    url_counts = {}
    for url in urls:
        if any(term in url for term in search_terms):
            content = cc.get_page(url)
            if any(keyword in content for keyword in economic_keywords):
                month = re.search(r'\d{6}', url).group()[:4]
                filtered_urls.append((url, month))
                url_counts[url] = url_counts.get(url, 0) + 1
    unique_urls = [url for url, count in url_counts.items() if count == 1]
    return random.sample(unique_urls, min(len(unique_urls), 1000))

# Search for pages in the 2020 archives
cc = CommonCrawl()
urls = cc.search('2020', 'warc', filter_urls)

# Print the list of relevant URLs and their months
for url, month in urls:
    print(url, month)
