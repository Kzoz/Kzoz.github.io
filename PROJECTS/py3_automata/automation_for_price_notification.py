import requests
from bs4 import BeautifulSoup
import smtplib

#Define the source of the research (or the website from which the info will be picked up from)
#URL = 'https://kakaku.com/item/J0000033539/' # Sony XM4
# URL = 'https://kakaku.com/item/K0001206017/' #Airpods Pro
URL = 'https://www.amazon.co.jp/gp/product/B08JFTKHF2/ref=ox_sc_saved_title_1?smid=A2A0GDJVUPL7UQ&psc=1' #For Protein

headers= {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

# Check price: Using Requests, 
# find which class or ID hold the title and price of the item we want to track.
#Convert the price(str) into num

def check_price():

    page = requests.get(URL,  headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    title = soup.find(id={'productTitle'}).get_text()
    price = soup.find(id={'sns-base-price'}).get_text()
    conv_price = float(price.strip()[1:6].replace(',',''))

    if(conv_price < 3500):
        send_mail()
    print(title, conv_price)

#Send the info via email
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('username', 'pwd')
    subject = 'PROTEIN PRICE IS DOWN'
    body = " Check the Amazon link: 'https://www.amazon.co.jp/gp/product/B08JFTKHF2/ref=ox_sc_saved_title_1?smid=A2A0GDJVUPL7UQ&psc=1' "
    
    msg = f"Subject: {subject} \n\n {body}"
    
    server.sendmail('username', 'username', msg)
    print('Hey the price of X has gone down')
    server.quit()
    

check_price()
