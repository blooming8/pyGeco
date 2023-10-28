from scraper import Scraper
from selenium import webdriver
import traceback
import sys


def main():
    try:
        scraper = Scraper()

        # cancella i consuntivi vecchi
        scraper.pulisci_cartella()

        # login 
        print("\nSto facendo il login su Geco...\n")
        scraper.login()

        # scarica consuntivo
        print("\nSto scaricando il consuntivo da Geco...\n")
        scraper.download_file()
        scraper.sposta_file()
        print("\nConsuntivo scaricato.\n")

        # invia consuntivo
        print("\nSto inviando il file a Bit Spa...\n")
        scraper.invia_file()
        print("\nFile inviato con successo.\n")

    except Exception as exception:
        traceback.print_exception()

    finally:
        print("\nProgramma terminato.\n")


if __name__ == '__main__':
    print("\n>> PyGeco <<\n")
    main()