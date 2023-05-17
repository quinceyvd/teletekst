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
    if pag is None or pag == "101" or pag == "nieuws":
        res = requests.get('https://teletekst-data.nos.nl/webtekst?p=101')
        res = res.text
        soup = BeautifulSoup(res, 'html.parser')
        titles = soup.findAll('span', class_= 'cyan')
        pageNums = soup.findAll('span', class_= 'yellow')

        titlesList = []
        pageNumsList = []

        for title in titles:
            titlesList.append(title.get_text())
        
        for pageNum in pageNums:
            pageNumsList.append(pageNum.get_text())
        
        titlesList.pop()
        pageNumsList.pop()
        pageNumsList.pop(0)

        time = datetime.now()
        table = Table(box=None)
        table.add_column(f"N[red]O[/red]S Teletekst [{time.strftime('%H:%M:%S')}] - [cyan]nieuws[/cyan]\n")
        
        for title, pageNum in zip(titlesList, pageNumsList):
            table.add_row(f"[white]{title}[/white] - [cyan]{pageNum}[/cyan]")

        table.add_row(f"\n")
        print(table)
    elif pag == "100":
        res = requests.get('https://teletekst-data.nos.nl/webtekst?p=100')
        res = res.text
        soup = BeautifulSoup(res, 'html.parser')
        titles = soup.findAll('span', class_= 'blue bg-white')
        subtitles = soup.findAll('span', class_= 'bg-blue')
        titlesArray = []
        subtitlesArray = []

        for title in titles:
            titlesArray.append(title.get_text())

        for subtitle in subtitles:
            subtitle = re.sub(r"\s{2,}", " ", subtitle.get_text())
            subtitlesArray.append(subtitle)

        
        titlesArray = [item for item in titlesArray if not item.isspace()]
        subtitlesArray = [item for item in subtitlesArray if not item.isspace()]

        for _ in range(3):
            subtitlesArray.pop()

        time = datetime.now()
        table = Table(box=None)
        table.add_column(f"N[red]O[/red]S Teletekst [{time.strftime('%H:%M:%S')}] - [cyan]100[/cyan]\n")

        for title, subtitle in zip(titlesArray, subtitlesArray):
            title_split = title.split()  # split the title string into a list of words
            subtitle_split = subtitle.split()  # split the subtitle string into a list of words

            for i, entry in enumerate(title_split):
                if entry.isnumeric():
                    # wrap the number in a cyan markup
                    title_split[i] = f"[cyan]{entry}[/cyan]"
            
            for i, entry in enumerate(subtitle_split):
                if entry.isnumeric():
                    # wrap the number in a cyan markup
                    subtitle_split[i] = f"[cyan]{entry}[/cyan]"

            # re-join the modified title entries back into a string
            modified_title = " ".join(title_split)
            modified_subtitle = subtitle.strip()  # remove leading/trailing whitespace from subtitle
            modified_subtitle = " ".join(subtitle_split)

            # add the modified title and subtitle as a row to the table
            table.add_row(modified_title, modified_subtitle)

        table.add_row("\n")
        print(table)

    elif pag == "102" or pag == "103":
        res = requests.get(f'https://teletekst-data.nos.nl/webtekst?p={pag}')
        res = res.text
        soup = BeautifulSoup(res, 'html.parser')
        titles = soup.findAll('span', class_= 'yellow')
        pageNums = soup.findAll('a', class_= 'yellow')

        titlesList = []
        pageNumsList = []

        for title in titles:
            letters = re.findall(r'[a-zA-Z,: ]+', title.get_text())
            nummers = re.findall(r'\d+', title.get_text())
            titlesList.append(letters)
            pageNumsList.append(nummers)

            for item in pageNumsList:
                if item == []:
                    pageNumsList.remove(item)

            # for item in titlesList:
            #     for x in item:
            #         if x.isalpha() == False:
            #             item.remove(x)
            #         # if item == []:
            #             # titlesList.remove(item)


        print(titlesList)
        print(pageNumsList)

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
