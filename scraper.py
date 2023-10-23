from mittente import Mittente
from mail import Mail 
from connection import Connection
import smtplib


class Scraper:

    def login(self, browser):
        user = Mittente()
    

    def download_file(self):
        pass


    def invia_file(self):
        destinatari = ["alessio.liveli@gmail.com"]
        mittente = Mittente()
        mail = Mail()

        try:
            with smtplib.SMTP(Connection.get_server(), Connection.get_porta()) as smtp:
                smtp.starttls()
                smtp.login(mittente.get_email(), mittente.get_psw())
                smtp.sendmail(mittente.get_email(), destinatari, mail.get_msg())
        except Exception as exception:
            print(exception)

