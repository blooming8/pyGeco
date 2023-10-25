from mail import Mail 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from users import GecoUser, OutlookUser
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import yagmail
import requests
import shutil
import os 


class Scraper:

    def __init__(self):
        self.server = "outlook.office365.com"
        self.porta = 587
        self.user = GecoUser()
        self.credenziali = {"username": self.user.get_username(), "password": self.user.get_psw()}

    # def __del__(self):
    #     self.browser.quit()

  
    def login(self) -> bool:
        url = "https://sts3.reply.eu/adfs/ls/?wa=wsignin1.0&wtrealm=https%3a%2f%2fgeco.reply.com&wctx=rm%3d0%26id%3dpassive%26ru%3d%252f&wct=2023-10-23T16%3a29%3a51Z#t"
        response = requests.Session().post(url= url, data= self.credenziali)
        if response.ok is False:
            return False  
        return True
    

    def download_file(self) -> bool:
        try:
            url = "https://geco.reply.com/?downloadformat=.xs#t"
            params = {"downloadformat": ".xs"}
            size = 10 * 1024

            response = requests.Session().get(url= url, params= params, stream= True)
            if response.ok is False:
                return False
            
            print(response.content)
            with open("x.js", "wb") as x:
                x.write(response.content)

            with open("consuntivi/timereporting.xs", "wb") as download:
                for chunk in response.iter_content(chunk_size= size):
                   download.write(chunk)
            return True 
        except Exception as exception:
            print(exception)


    def sposta_file(self, download: any) -> None:
        folder = os.path.realpath("consuntivi")
        if not os.path.exists(folder):
            os.mkdir(folder)
            print("\nCartella 'consuntivi' creata\n")
        #shutil.move(os.path.realpath(download.name), folder)
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


    def pulisci_cartella() -> None:
        pass


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