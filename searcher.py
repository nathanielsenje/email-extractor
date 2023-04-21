from googlesearch import search
import requests
from bs4 import BeautifulSoup

company_name = input("Enter the name of the company: ")

# perform Google search for the company name
search_results = search(company_name, num_results=10)

# loop through search results and find the website for the company
for result in search_results:
    if 'www.' in result and 'http' in result:
        website = result
        break

# extract links to all pages on the website
response = requests.get(website)
soup = BeautifulSoup(response.text, 'html.parser')
links = [link.get('href') for link in soup.find_all('a')]

# filter links to find the contact page
contact_page = None
for link in links:
    if 'contact' in link.lower():
        contact_page = link

    elif 'contact-us' in link.lower():
        contact_page = link

    elif 'contactus' in link.lower():
        contact_page = link
        break

print("Website for", company_name, "is:", website)
print("Contact page for", company_name, "is:", contact_page)
