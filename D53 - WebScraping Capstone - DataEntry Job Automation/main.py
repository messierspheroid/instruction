from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

zillow_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.64275587988281%2C%22east%22%3A-122.22390212011719%2C%22south%22%3A37.66856657328628%2C%22north%22%3A37.88186249084342%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(zillow_url, headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")

# links
all_link_elements = soup.select(".list-card-top a")

listing_links = []
for link in all_link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        listing_links.append(f"https://www.zillow.com{href}")
    else:
        listing_links.append(href)

# addresses
all_address_elements = soup.select(".list-card-info address")
listing_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

# prices
all_price_elements = soup.select(".list-card-heading")
listing_prices = []
for element in all_price_elements:
    try:
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        print("Multiple listings for the card")
        price = element.select(".list-card-details li").contents[0]
    finally:
        listing_prices.append(price)

# use selenium to autofill the google forms
g_form_link = "https://forms.gle/m7kFtxE3pdWvGKW56"

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for n in range(len(listing_links)):
    driver.get(g_form_link)

    time.sleep(2)
    address = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_button = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div")

    address.send_keys(listing_addresses[n])
    price.send_keys(listing_prices[n])
    link.send_keys(listing_links[n])
    submit_button.click()

    driver.quit()

