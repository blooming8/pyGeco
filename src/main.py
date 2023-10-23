from scraper import Scraper
from selenium import webdriver
import time 
import sys


def main():
    try:
        scraper = Scraper()

        # login 
        print("\nSto facendo il login su Geco...\n")
        while not scraper.login():
            time.wait(2)
            print("\nLOGIN ERROR\n")
            if time.time() == 30:
                sys.exit(0)
        print("\nLogin effettuato.\n")

        # scarica consuntivo
        print("\nSto scaricando il consuntivo da Geco...\n")
        if not scraper.download_file():
            print("\n")
        print("\nConsuntivo scaricato.\n")

        # invia consuntivo
        print("\nSto inviando il file a Bit Spa...\n")
        scraper.invia_file()
        print("\nFile inviato con successo.\n")

    except Exception as exception:
        print(exception)

    finally:
        print("\nProgramma terminato.\n")


if __name__ == '__main__':
    print("\n>> PyGeco <<\n")
    main()