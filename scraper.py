# Imports
import requests
from bs4 import BeautifulSoup
import csv

# Setup
URL = "https://en.wikipedia.org/wiki/List_of_programming_languages"
req = requests.get(URL)
soup = BeautifulSoup(req.text, "html.parser")
all_languages = soup.find_all(class_="div-col")

#Create CSV file
csv_file = open("scraper.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Language", "Link", "Paradigm", "First Appeared", "Number of Headers", "Number of links/url"])

for language in all_languages:
  #For Language Name and Link
  language_name = language.find("a").contents
  link = language.find("a")["href"]
  full_link = f"https://en.wikipedia.org/{link}"
  print(language_name)
  print(full_link)

  #For Paradigm, First Appeared, and File Extensions
  new_links = requests.get(full_link)
  soup = BeautifulSoup(new_links.content, "html.parser")

  try:
    def paradigm():
      return soup.find(title="Multi-paradigm programming language") or soup.find(title="Functional programming") or soup.find(title="Imperative programming") or soup.find(title="Object-oriented programming") or soup.find(title="Procedural programming") or soup.find(title="Modular programming") or soup.find(title="Prototype-based programming") or soup.find(title="Array programming") or soup.find(title="Reflective programming") or soup.find(title="Structured programming")

    print(paradigm())

    first_appeared = soup.find("span", class_="noprint").get_text().replace("; ",  "")
    print(first_appeared)

    #Amount of header in each wikipedia article
    def headers_amount():
      all_headers = soup.find("h1") and soup.find("h2") and soup.find("h3")
      return len(all_headers)
    print(headers_amount())

    #Amount of links/urls on the webpage
    link_amount = len(soup.find_all("a"))
    print(link_amount)

    
  except:
    pass

  csv_writer.writerow([language_name, full_link, paradigm(), first_appeared, headers_amount(), link_amount])

csv_file.close()