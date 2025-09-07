from bs4 import BeautifulSoup as bs
import requests
import smtplib
import time

URL = "https://www.amazon.in/Apple-iPhone-Pro-128GB-Gold/dp/B0BDJKL7KY/ref=sr_1_5?keywords=iphone%2B14%2Bpro%2Bmax&qid=1674063459&sr=8-5&th=1"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}


def fetch_price(url=URL):
    page = requests.get(url, headers=HEADERS)
    soup1 = bs(page.content, "html.parser")
    soup2 = bs(soup1.prettify(), "html.parser")
    title = soup2.find(id="productTitle").get_text().strip()
    price = soup2.find(class_="a-price-whole").get_text().strip()
    price = int(price.replace(",", "")[:6])
    return title, price


def send_mail(url=URL):
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("sender_email_id", "sender_email_id_password")
    message = "Price is in the provided range, Hurry check the link " + url
    s.sendmail("sender_email_id", "receiver_email_id", message)
    s.quit()


if __name__ == "__main__":
    while True:
        title, price = fetch_price()
        print(title)
        print(price)
        if price < 120000:
            send_mail()
        time.sleep(17280)  # checks 5 times a day
