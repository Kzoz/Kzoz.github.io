import requests
from bs4 import BeautifulSoup
import smtplib
import time

#Define the source of the research (or the website from which the info will be picked up from)
URL = 'https://kakaku.com/item/J0000033539/' # Sony XM4
# URL = 'https://kakaku.com/item/K0001206017/' #Airpods Pro
headers= {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15'}

# Check price: Using Requests, 
# find which class or ID hold the title and price of the item we want to track.
#Convert the price(str) into num

def check_price():

    page = requests.get(URL,  headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    title = soup.find(attrs={'newBrand'}).get_text()
    price = soup.find(attrs={'priceTxt'}).get_text()
    conv_price = float(price[1:7].replace(',',''))

    if(conv_price < 32000):
        send_mail()
    print(title, conv_price)

#Send the info via email
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('d.pape.moussa@gmail.com', 'usveiyxrdoyysqab')
    subject = 'Sony XM4 price fell down'
    body = 'You programmed this PMD. Check the Kakaku link: https://kakaku.com/item/J0000033539/'
    
    msg = f"Subject: {subject} \n\n {body}"
    
    server.sendmail('d.pape.moussa@gmail.com', 'd.pape.moussa@gmail.com', msg)
    print('Hey the price reduction email has been sent!!')
    server.quit()
    

check_price()
#time.sleep(604800)