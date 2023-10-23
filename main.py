from scraper import Scraper
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def main():
    try:
        # caricamento pagina web
        print("\nMi sto connettendo a Geco...\n")
        with webdriver.Chrome(ChromeDriverManager().install()) as browser:
            browser.get("https://chrome.google.com/webstore/category/extensions?hl=it")

        # login 
        print("\nSto facendo il login su Geco...\n")
        with Scraper() as scraper:
            scraper.login()

            # scarica consuntivo
            print("\nSto scaricando il consuntivo da Geco...\n")
            scraper.download_file()

            # invia consuntivo
            print("\nSto inviando il file a Bit Spa...\n")
            scraper.invia_file()
            print("\nFile inviato con successo.\n")

    except Exception as exception:
        print(exception)

    finally:
        print("\nProgramma terminato.\n")


if __name__=='__main__':
    print("\n>> PyGeco <<\n")
    main()