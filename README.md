# web-scraper
calculate the number of citation paragraphs and  print them
# whiteboard
![lab177](https://github.com/ahmaderaqi/web-scraper/assets/118004544/fa03fe07-b765-424b-98f2-4e3aa37e87ad)


## Approach & Efficiency
calculate the number of citation paragraphs and  print them

# algorithms
## Algorithm for get_citations_needed_count:

1. Send a GET request to the specified URL.
2. Parse the HTML content of the response using BeautifulSoup.
3. Find all paragraph elements that contain the text 'citation needed' using the find_all method.
4. Count the number of elements found in step 3.
5. Return the count as the result.


## Algorithm for get_citations_needed_report:

1.Send a GET request to the specified URL.
2. Parse the HTML content of the response using BeautifulSoup.
3. Find all elements that contain the text 'citation needed' using the find_all method.
4. For each element found in step 3:
5. Find its parent paragraph element using the find_parent method.
6. If a parent element is found, extract its text content and strip any leading/trailing whitespace.
7. Append the extracted passage to a report string, along with the appropriate formatting.
8. Return the report string as the result.

# big O
time complexity of O(n)
space complexity of O(n)

## Solution

|Code challenge15  |    [code1](./scraper.py)
