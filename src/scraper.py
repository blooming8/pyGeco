from mail import Mail 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from users import GecoUser, OutlookUser
from bs4 import BeautifulSoup
import yagmail
import requests
import shutil
import os 


class Scraper:

    def __init__(self):
        self.server = "outlook.office365.com"
        self.porta = 587
        self.credenziali = {"username": GecoUser().get_username(), "password": GecoUser().get_psw()}

    # def __del__(self):
    #     self.browser.quit()

  
    def login(self) -> bool:
        response = requests.Session().post(url= "https://sts3.reply.eu/adfs/ls/?wa=wsignin1.0&wtrealm=https%3a%2f%2fgeco.reply.com&wctx=rm%3d0%26id%3dpassive%26ru%3d%252f&wct=2023-10-23T16%3a29%3a51Z#t", data= self.credenziali)
        if response.status_code != 200:
            return False  
        return True
    

    def download_file(self) -> bool:
        response = requests.Session().get(url= "https://geco.reply.com/#t/timesheet/compiling:~:text=RIEPILOGO%20CLIENTE%20ADV-,RAPPORTO,-MENSILE")
        if response.status_code != 200:
            return False
        with open("timereporting.xs", "wb") as download:
            download.write(response.content)
            self.sposta_file(download)
        return True 


    def sposta_file(self, download: any) -> None:
        folder = os.path.realpath("consuntivi")
        if not os.path.exists(folder):
            os.mkdir(folder)
            print("\nCartella 'consuntivi' creata\n")
        shutil.move(os.path.realpath(download.name), folder)
        print("\nFile spostato in 'consuntivi'.\n")


    def invia_file(self) -> None:
        destinatari = ["alessio.liveli@gmail.com"]
        mittente = OutlookUser()
        mail = Mail()

        try:
            mittente = OutlookUser()
            with yagmail.SMTP(mittente.get_username(), mittente.get_psw()) as smtp:
                smtp.send(destinatari, mail.get_oggetto(), mail.get_corpo(), mail.get_file_path())
        except Exception as exception:
            print(exception)




# class Connection:

#     def __init__(cls):
#         cls.server = "outlook.office365.com"
#         cls.porta = 587


#     @classmethod
#     def get_server(cls):
#         return cls.server


#     @classmethod
#     def get_porta(cls):
#         return cls.porta  
        # response = requests.Session().get(url= "https://geco.reply.com/#t/timesheet/compiling")
        # soup = BeautifulSoup(response.text, "html.parser")
        # print(soup)
        # xs_links = soup.find_all("a", href= (lambda link: link and link.endswith(".xs")))
        # if not xs_links:
        #     return False
        # xs_urls = [link["href"] for link in xs_links]
        # for xs in xs_urls:
        #     response = requests.Session().get(xs)
        #     if response.status_code != 200:
        #         return False
        #     return True