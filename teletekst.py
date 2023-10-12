# Importeer dependencies
import typer
from typing import Optional
from rich import print
from rich.table import Table
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import re

app = typer.Typer()

@app.command()
def teletekst(pag: Optional[str] = typer.Argument(None)):
    # Pagina 101 als standaard fetchen als er geen kanaalnummer argument wordt meegegeven
    if pag is None or pag == "101" or pag == "nieuws":
        # Fetch en parse data van NOS Teletekst
        res = requests.get('https://teletekst-data.nos.nl/webtekst?p=101')
        res = res.text
        soup = BeautifulSoup(res, 'html.parser')
        titles = soup.findAll('span', class_= 'cyan')
        pageNums = soup.findAll('span', class_= 'yellow')

        # Arrays voor headlines en paginanummers
        titlesList = []
        pageNumsList = []

        # Append headlines en paginanummers aan respecgievelijke arrays
        for title in titles:
            titlesList.append(title.get_text())
        
        # I.v.m. uitzonderlijke subtitels in teletekst pagina, verwijder alle subtitels uit de paginanummers array
        for pageNum in pageNums:
            pageNumText = pageNum.get_text()
            if any(char.isalpha() for char in pageNumText):
                pass
            else:
                pageNumsList.append(pageNum.get_text())
        
        # Lege items uit datafetch verwijderen uit arrays
        titlesList.pop()
        pageNumsList.pop()
        pageNumsList.pop(0)

        # Tabel maken om data netjes in te displayen
        time = datetime.now()
        table = Table(box=None)
        table.add_column(f"N[red]O[/red]S Teletekst [{time.strftime('%H:%M:%S')}] - [cyan]nieuws[/cyan]\n")
        
        for title, pageNum in zip(titlesList, pageNumsList):
            table.add_row(f"[white]{title}[/white] - [cyan]{pageNum}[/cyan]")

        table.add_row(f"\n")

        # Data in tabel printen
        print(table)
    elif pag == "100":
        # Fetch en parse data van NOS Teletekst
        res = requests.get('https://teletekst-data.nos.nl/webtekst?p=100')
        res = res.text
        soup = BeautifulSoup(res, 'html.parser')

        # Verwerking van headlines en kanaalopties data
        titles = soup.findAll('span', class_= 'blue bg-white')
        subtitles = soup.findAll('span', class_= 'bg-blue')

        titlesArray = []
        subtitlesArray = []

        for title in titles:
            titlesArray.append(title.get_text())

        for subtitle in subtitles:
            subtitle = re.sub(r"\s{2,}", " ", subtitle.get_text())
            subtitlesArray.append(subtitle)

        # Lege items uit datafetch verwijderen uit arrays
        titlesArray = [item for item in titlesArray if not item.isspace()]
        subtitlesArray = [item for item in subtitlesArray if not item.isspace()]

        for _ in range(3):
            subtitlesArray.pop()

        # Tabel maken om data netjes in te displayen
        time = datetime.now()
        table = Table(box=None)
        table.add_column(f"N[red]O[/red]S Teletekst [{time.strftime('%H:%M:%S')}] - [cyan]100[/cyan]\n")

        for title, subtitle in zip(titlesArray, subtitlesArray):
            title_split = title.split()
            subtitle_split = subtitle.split()

            # Blauwe highlighting voor paginanummers
            for i, entry in enumerate(title_split):
                if entry.isnumeric():
                    title_split[i] = f"[cyan]{entry}[/cyan]"
            
            for i, entry in enumerate(subtitle_split):
                if entry.isnumeric():
                    subtitle_split[i] = f"[cyan]{entry}[/cyan]"

            # Aangepaste entries terug re-joinen in een string
            modified_title = " ".join(title_split)
            modified_subtitle = subtitle.strip()
            modified_subtitle = " ".join(subtitle_split)

            # Bijgewerkte data toevoegen aan tabel
            table.add_row(modified_title, modified_subtitle)

        table.add_row("\n")

        # Data in tabel printen
        print(table)

    elif pag == "102" or pag == "103":
        print(f"Pagina {pag} is helaas niet beschikbaar op dit moment.")

    elif pag.isnumeric() == False:
        print("[red]![/red]: Vul s.v.p. een geldig paginanummer in.")
    else:
        res = requests.get(f'https://teletekst-data.nos.nl/webtekst?p={pag}')
        res = res.text
        soup = BeautifulSoup(res, 'html.parser')
        title = soup.find('span', class_= 'yellow bg-blue')
        content = soup.findAll('span', class_= 'cyan')
        contentList = []

        for item in content:
            contentList.append(item.get_text())

        contentList.pop()
        time = datetime.now()
        table = Table(box=None)
        table.add_column(f"N[red]O[/red]S Teletekst [{time.strftime('%H:%M:%S')}] - [cyan]{title.get_text()}[/cyan]\n")

        for item in contentList:
            table.add_row(f"{item}")

        table.add_row(f"\n")
        print(table)

if __name__ == "__main__":
    app()
