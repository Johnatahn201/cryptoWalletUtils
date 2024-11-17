import requests
import smtplib
from email.mime.text import MIMEText
from time import sleep

def get_crypto_price(crypto):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[crypto]['usd']

def send_email_alert(price, crypto, threshold, email):
    subject = f"Price Alert: {crypto.capitalize()} has reached ${price}"
    body = f"The current price of {crypto.capitalize()} is ${price}, which is above your threshold of ${threshold}."
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = email

    # Set up your email server and login credentials
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'your_email@gmail.com'
    smtp_password = 'your_email_password'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, email, msg.as_string())

def main():
    crypto = input("Enter the cryptocurrency (e.g., bitcoin): ")
    threshold = float(input("Enter the price threshold in USD: "))
    email = input("Enter your email address for alerts: ")

    print(f"Tracking {crypto}...")

    while True:
        price = get_crypto_price(crypto)
        print(f"Current price of {crypto}: ${price}")

        if price >= threshold:
            send_email_alert(price, crypto, threshold, email)
            print(f"Alert sent! {crypto} has reached ${price}.")
            break

        sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
