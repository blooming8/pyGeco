from mail import Mail 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from users import GecoUser, OutlookUser
from selenium.webdriver.chrome.service import Service as ChromeService 
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import yagmail
import requests
import shutil
import os 
import re
import time 
import js2py
import execjs


class Scraper:

    def __init__(self):
        self.server = "outlook.office365.com"
        self.porta = 587
        self.user = GecoUser()
        self.credenziali = {"username": self.user.get_username(), "password": self.user.get_psw()}

        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(service= ChromeService(ChromeDriverManager().install()), options= options) 


    # def __del__(self):
    #     self.browser.quit()

  
    def login(self) -> None:
        try:
            url = "https://sts3.reply.eu/adfs/ls/?wa=wsignin1.0&wtrealm=https%3a%2f%2fgeco.reply.com&wctx=rm%3d0%26id%3dpassive%26ru%3d%252f&wct=2023-10-23T16%3a29%3a51Z#t"
            self.browser.get(url)
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "userNameInput")))
            self.browser.find_element(By.ID, "userNameInput").send_keys("a.liveli@reply.it")
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "passwordInput")))
            self.browser.find_element(By.ID, "passwordInput").send_keys("BMed2023!!")
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "submitButton")))
            self.browser.find_element(By.ID, "submitButton").click()

            url = "https://geco.reply.com/WebServiceAD/GeCo.asmx/AppIn"
            response = requests.post(url= url, data= self.credenziali)
            if response.status_code == 200:
                print("login success")
            else:
                print("login error")
        except Exception as exception:
            raise exception

    
    def download_file(self) -> None:
        try:   
            self.browser.get("https://geco.reply.com/#t/timesheet/compiling")
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Rapporto Mensile")))
            self.browser.find_element(By.LINK_TEXT, "Rapporto Mensile").click()
        except Exception as exception:
            raise exception
        

    def sposta_file(self, download: any) -> None:
        try:
            folder = os.path.realpath("consuntivi")
            if not os.path.exists(folder):
                os.mkdir(folder)
                print("\nCartella 'consuntivi' creata.\n")
            
            print("\nFile spostato in 'consuntivi'.\n")
        except Exception as exception:
            raise exception


    def invia_file(self) -> None:
        destinatari = ["alessio.liveli@gmail.com"]
        mittente = OutlookUser()
        mail = Mail()

        try:
            with yagmail.SMTP(mittente.get_username(), mittente.get_psw()) as smtp:
                smtp.send(destinatari, mail.get_oggetto(), mail.get_corpo(), mail.get_file_path())
        except Exception as exception:
            print(exception)


    def pulisci_cartella() -> None:
        if os.getcwd() != "consuntivi":
            os.chdir("consuntivi")
        _ = [os.remove(file) for file in os.walk(os.getwcd())]


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