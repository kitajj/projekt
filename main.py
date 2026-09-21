from scraper import fetcher, parser

def main():
    fetcher.pobierz_dane()
    parser.przetlumacz_dane()
    fetcher.usun_dane()
    print("koniec")

if __name__ == "__main__":
    main()