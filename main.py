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
    reports = ba.get_reports("Deutsche Bahn", page_limit=float("inf"), year=2018)
    print("Reports:", len(reports))

if __name__ == "__main__":
    main()
