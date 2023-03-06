# TLinternship2020

To find pages from the Common Crawl archive that discuss or are relevant to COVID-19's economic impact, we can use the following approach:
Identify the index of the 2020 archives of Common Crawl.
1. Use a web crawler to search through the pages in the archives for content related to COVID-19's economic impact.
2. Store the URLs of pages that meet the requirement in a list and note the month of the archive they were found in.
3. heck the list for duplicate URLs and remove them.
4. If the list has more than 1000 URLs, randomly select 1000 URLs from the list. If the list has less than 1000 URLs, try searching through additional archives to find more relevant pages.
5. Submit the final list of 1000 unique URLs along with the months of the archives they were found in.

In the Python code, we first define the search terms and economic keywords that we will use to filter URLs. We then define a function filter_urls that takes a list of URLs, filters them based on their relevance to COVID-19's economic impact, and returns a list of unique URLs with a maximum length of 1000. The function also notes the month of the archive that each URL was found in. We use the commoncrawl library to search for pages in the 2020 archives of Common Crawl and apply the filter_urls function to the search results. Finally, we print the list of relevant URLs and their months.
