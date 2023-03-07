import typer
from typing import Optional
from rich import print
from rich.table import Table
from bs4 import BeautifulSoup
from datetime import datetime
import requests

app = typer.Typer()

@app.command()
def teletekst(pag: Optional[str] = typer.Argument(None)):
    if pag is None or pag == "101":
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
        table.add_column(f"N[red]O[/red]S Teletekst [{time.strftime('%H:%M:%S')}]\n")
        
        for title, pageNum in zip(titlesList, pageNumsList):
            table.add_row(f"[white]{title}[/white] - [cyan]{pageNum}[/cyan]")

        table.add_row(f"\n")
        print(table)
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
