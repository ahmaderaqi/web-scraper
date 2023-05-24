


import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_needed_elements = soup.find_all(text='citation needed')
    return len(citation_needed_elements)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_needed_elements = soup.find_all(text='citation needed')
    report = ""
    
    for element in citation_needed_elements:
        citation = element.find_parent('p')
        if citation:
            passage = citation.text.strip()
            report += f"Citation needed for: \"{passage}\"\n"
    
    return report

def save_report_to_file(report, filename):
    with open(filename, 'w') as file:
        file.write(report)

# Example usage:
wikipedia_url = 'https://en.wikipedia.org/wiki/History_of_Mexico'

count = get_citations_needed_count(wikipedia_url)
print(f"Number of citations needed: {count}")

report = get_citations_needed_report(wikipedia_url)
print(report)

filename = 'citations_report.txt'
save_report_to_file(report, filename)
print(f"Report saved to {filename}.")
