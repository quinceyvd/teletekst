# Teletekst
Teletekst is een tool die het mogelijk maakt om [NOS Teletekst](https://nos.nl/teletekst) uit te lezen in de terminal. Het script is geschreven in Python 3.11.0 en maakt gebruik van een paar dependencies om de functionaliteit te bieden. 

Deze tool is ontworpen om het mogelijk te maken actueel nieuws snel te bekijken vanuit de terminal. Mooi voor als je geen tijd hebt om de browser te openen, en eindeloos door de kranten te scrollen om up-to-date te blijven.

## 🔨 Installatie
Na het clonen of installeren van de repository moeten de benodigde dependencies worden geïnstalleerd. Dit kan worden gedaan via [pip](https://pypi.org/project/pip/). Voer het volgende commando om alle requirements voor dit project te installeren:

```bash
pip install typer==0.7.0 requests==2.28.2 rich==12.6.0 bs4==0.0.1 beautifulsoup4==4.11.2 DateTime==5.0
```

## 📖 Gebruik
Om Teletekst te gebruiken, open je de terminal en navigeer je naar de locatie waar het script is opgeslagen. Voer vervolgens het volgende commando uit:

```bash
python teletekst.py
```

Na het uitvoeren van deze commando wordt de inhoud van [NOS Teletekst pagina 101](https://nos.nl/teletekst#101) uitgeprint in de terminal. 

Op basis van de paginanummers naast de kopjes kun je navigeren. Dit doe je door de paginanummer van het gewenste artikel mee te geven als argument:

```bash
python teletekst.py paginanummer
```

### Toevoegen aan Environment Variables (Windows)
Om Teletekst makkelijk en simpel aan te roepen door middel van een simpele `teletekst` commando in de terminal, kun je de map waarin het script zich bevindt toevoegen aan jouw Environment Variables. Dit is optioneel, maar wordt sterk aangeraden omdat het snelle fetchen het beste werkt in combinatie met globale toegang tot het script. Op deze manier kan je vanuit elke directory teletekst uitlezen in je terminal. 

Hoe je navigeert in je Environment Variables navigeert verschilt per Windows release. Windows 11 gebruikers kunnen de onderstaande instructies vanaf stap 1 volgen. Gebruikers van eerdere Windows versies kunnen de gids volgen vanaf stap 4, nadat de Environment Variables window is geopend.

1. Gebruik de `Win + X` shortcut en druk vervolgens op **System**
2. Klik op **Advanced system settings** onder het kopje *Device Specifications*
3. Klik op het kopje *Advanced* in de **System Properties** window. Klik vervolgens op de **Environment Variables** knop.
4. Nu komt de *Environment Variables* window voor tevoorschijn. Onder het kopje *System Variables* navigeer je naar **Path**.
5. Selecteer **Path** en klik vervolgens op de **Edit** knop. 
6. Klik op **New** en plak hier de locatie van de map waarin `teletekst.py` is opgeslagen.
7. Klik op **Ok**. Klik vervolgens wederom op **Ok** in de *Environment Variables* en de *System Properties* windows.

Het script is nu globaal toegankelijk! Je kan nu vanuit elke directory `teletekst` uitvoeren met het volgende commando:
```bash
teletekst
```
En als je wilt navigeren naar een artikel:
```bash
teletekst paginanummer
```

## 🚧 Beperkingen
Omdat de gefetchde data van NOS Teletekst een zeer variabele aard hebben zijn alleen de volgende paginas beschikbaar om uit te lezen via deze tool:
- Pagina 100
- Pagina 101
- De bijbehorende nieuwspagina's van de headlines die te vinden zijn op pagina 100 en 101.

Houd er dus rekening mee dat de tool beperkt is in zijn functionaliteit en niet geschikt is voor het uitlezen van andere pagina's op NOS Teletekst, zoals de sport- en weerpaginas.

## ⚙️ Dependencies
- [Typer](https://typer.tiangolo.com/)
- [Rich](https://rich.readthedocs.io/en/stable/#) (bijgeleverd met Typer)
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
- [Requests](https://requests.readthedocs.io/)

## 📄 Disclaimer
Deze software is ontworpen als een hobbyproject en is niet bedoeld voor commerciële doeleinden. Dit project heeft geen affiliatie met de NOS. 
