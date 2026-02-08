import logging
from deutschland.bundesanzeiger import Bundesanzeiger

def main():
    logging.basicConfig(
        level=logging.WARNING,  # Root: nur Warnungen
        format="%(levelname)s:%(name)s:%(message)s",
    )

    # Dein Modul laut drehen
    logging.getLogger("deutschland.bundesanzeiger.bundesanzeiger").setLevel(logging.DEBUG)

    ba = Bundesanzeiger()
    reports = ba.get_reports("deepwood GmbH", page_limit=1, year=2023)
    print("Reports:", len(reports))

if __name__ == "__main__":
    main()
