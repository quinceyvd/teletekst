# Teletekst
Teletekst is een tool die het mogelijk maakt om [NOS Teletekst](https://nos.nl/teletekst) te bekijken vanuit de terminal. Het script is geschreven in Python 3.11.0 en maakt gebruik van een paar dependencies om de functionaliteit te bieden. 

Deze tool is ontworpen om het mogelijk te maken actueel nieuws snel te bekijken vanuit de terminal. Mooi voor als je geen zin hebt om de browser te openen en eindeloos te zitten scrollen om de laatste nieuwtjes mee te krijgen.

## 🔨 Installatie
Na het clonen of installeren van de repository moeten de benodigde dependencies worden geïnstalleerd. Dit kan worden gedaan via [pip](https://pypi.org/project/pip/). Voer het volgende commando om alle requirements te installeren:

```
pip install typer==0.7.0 requests==2.28.2 rich==12.6.0 bs4==0.0.1 beautifulsoup4==4.11.2 DateTime==5.0
```

## 📖 Gebruik
Om Teletekst te gebruiken, open je de terminal en navigeer je naar de locatie waar het script is opgeslagen. Voer vervolgens de volgende commando uit:

```
python teletekst.py
```

Na het uitvoeren van deze commando wordt de inhoud van [NOS Teletekst pagina 101](https://nos.nl/teletekst#101) uitgeprint in de terminal. 

Op basis van de paginanummers naast de kopjes kun je navigeren. Dit doe je door de paginanummer van het gewenste artikel mee te geven als argument:

```
python teletekst.py <paginanummer>
```

### Toevoegen aan Environment Variables (Windows)
Om Teletekst gemakkelijk vanuit elke directory in de terminal te kunnen gebruiken, kun je de map waarin het script zich bevindt toevoegen aan jouw Environment Variables. Want om nu steeds terug te navigeren naar de bestandslocatie van `teletekst.py` verslaat een beetje het idee van '**snel** actueel nieuws bekijken'.

Hoe je bij je Environment Variables navigeert verschilt per Windows release. Als je Windows 11 gebruikt kan je de instructies vanaf stap 1 volgen. Als je een oudere versie van Windows kan je de gids volgen vanaf stap 4, nadat je bij de Environment Variables bent gekomen.

1. Gebruik de `Win + X` shortcut en druk vervolgens op "System"
2. Klik op "Advanced system settings" onder het kopje "Device Specifications"
3. Klik op het kopje "Advanced" in de "System Properties" window. Klik vervolgens op de "Environment Variables" knop.
4. Nu komt het "Environment Variables" tabblad voor tevoorschijn. Onder het kopje "System Variables" navigeer je naar "Path".
5. Selecteer "Path" en klik vervolgens op de "Edit" knop. 
6. Klik op "New" en plak hier de locatie van de map waarin `teletekst.py` is opgeslagen.
7. Klik op "Ok". Klik vervolgens ook op "Ok" in de 'Environment Variables" en de "System Properties" windows.

Nu kan je het script laten runnen vanuit elke locatie in je terminal, door simpelweg een het volgende commando te gebruiken:
```
teletekst
```
En als je wilt navigeren naar een artikel:
```
teletekst <paginanummer>
```

## 🚧 Beperkingen
Momenteel zijn alleen de respectievelijke artikel-paginas, en pagina 101 toegankelijk via deze tool. In de toekomst hoop ik een groter deel van de paginas toegankelijk te maken.

## ⚙️ Dependencies
- [Typer](https://typer.tiangolo.com/)
- [Rich](https://rich.readthedocs.io/en/stable/#) (bijgeleverd met Typer)
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
- [Requests](https://requests.readthedocs.io/)

## ⚠️ Disclaimer
Deze software is ontworpen als een hobbyproject en is niet bedoeld voor commerciële doeleinden. Dit project heeft tevens geen affiliatie met de NOS. 