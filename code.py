import requests
from bs4 import BeautifulSoup
import re

# URL of the website to crawl
url = 'https://www.kamaka.co.tz/contact-us/'

# Send a request to the website and get the HTML content
response = requests.get(url)
html = response.content

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find all email addresses in the HTML using a regular expression
emails = re.findall(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', str(soup))

# Print the email addresses
print(emails)
