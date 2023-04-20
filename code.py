import requests
from bs4 import BeautifulSoup

# Function to extract email and phone number from a website


def extract_contact_info(url):
    # Send a GET request to the website and get the response
    response = requests.get(url)

    # Use BeautifulSoup to parse the HTML content of the website
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the email and phone number HTML tags and extract their content
    email_tag = soup.find('a', href='mailto:')
    email = email_tag.text if email_tag else None

    phone_tag = soup.find('a', href='tel:')
    phone = phone_tag.text if phone_tag else None

    # Return the extracted email and phone number as a tuple
    return (email, phone)


# List of company names to search for contact information
companies = ['Kamaka', 'ALAF Limited']

# Loop through the list of companies and search for their websites
for company in companies:
    # Make a GET request to Google to search for the company's website
    search_url = f'https://www.google.com/search?q={company}'
    response = requests.get(search_url)

    # Use BeautifulSoup to parse the HTML content of the search results
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the URL of the first search result and extract the contact information from the website
    try:
        first_result = soup.find('div', {'class': 'g'}).find('a')['href']
        contact_info = extract_contact_info(first_result)

        # Print the extracted contact information
        print(f'{company}: {contact_info}')

    except AttributeError:
        print("No search results found")
