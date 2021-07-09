import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "bjornbergchad@gmail.com"
MY_PASSWORD = "5hoKV2kwo6cw"

# TODO find an amazon product to track
amazon_product_url = "https://www.amazon.com/Sony-WH-1000XM4-Canceling-Headphones-phone-call/dp/B0863TXGM3/ref=sr_1_1_sspa?crid=364HXJHKT4CWA&dchild=1&keywords=sony+wh-1000xm4&qid=1616697845&sprefix=sony%2Caps%2C241&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMEJJS0ZDWTZYSVUwJmVuY3J5cHRlZElkPUEwMTY3NDk1MTRRT0dQT1ZITjFNTSZlbmNyeXB0ZWRBZElkPUEwODA4MjY1MjVEWVdBQ1VSVDBXNCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

# TODO use the requests library to request the HTML page of the amazon product
header = {
    # "Request Line": "GET / HTTP/1.1",
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(amazon_product_url, headers=header)

# TODO use bs4 to scrap the amazon page for the price
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(id="priceblock_dealprice").get_text()
product_name = soup.find(id="productTitle").get_text()
product_name_formatted = product_name.split("\n")[8]
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

# print(price_as_float)
# print(product_name_formatted)

# TODO use SMTP module to send an email
buy_price = float(300.0)
if price_as_float < buy_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:{product_name} is listed lower than {buy_price}."
        )