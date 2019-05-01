# Úkázková webová aplikace v Pythonu s knihovnou Flask pro DA Czechitas

Aplikace obsahuje dvě stránky: jednu statickou s pouhým HTML textem a jednu
s formulářem pro zadání jména a tabulkou se seznam již zadaných jmen.
Při odeslání formuláře se nové jméno uloží do databáze. Při vypisování
tabulky již zadaných jmen se zase z načte z oné databáze.

Jako databáze se používá SQLite, což je hodně odlehčená a jednoduchá databáze,
která vše ukládá do jednoho souboru (soubor mydb.sqlite v tomto případě), ale
dotazy pro ní se píšou pomocí SQL, úplně stejně jako do Snowflake, MySQL nebo
PostgreSQL - pro svůj skutečný projekt budeš chtít použít jednu z těchto databází
spíš než SQLite - jak se z Pythonu připojit na databázi jinou než SQLite ti
můžeme ukázat na pracovních skupinkách.

## Soubory a složky v tomhle projekt

static - obsahuje statické dokumenty, které se nikdy nemění, jako obrázky, CSS styly, JavaScripty atd.

templates - obsahuje HTML šablony, ze kterých se pak poskládá HTML stránka, která se zobrazí uživateli

db.py - samostatný prográmek pro vytvoření a práci s databází

main.py - hlavní (spouštěcí) program našeho webíku - v něm se vytvoří Flask a zaregistrují se jednotlivé Blueprinty

names_bp.py - náš vlastní Blueprint pro stránku na zobrazování, vkládání a mazání jmen z databáze

about_bp.py - náš vlastní Blueprint pro stránku "O mě"

mydb.sqlite - SQLite datábáze, nad kterou spouštíme všechny naše SQL dotazy

schema.sql - popis, jak vytvořit v mydb.sqlite tu tabulku, kterou použiváme


## Instalace/spouštění

Nejprve ve složce s tímto projektem musíme vytvořit nové virtualní prostředí Pythonu.
Otevři terminál a pomocí příkazu "cd" se naviguj do složky, kde jsi tento projekt
rozbalila.

Nyní nainstaluj Flask, abychom ho mohli použivat:

    pip install flask

(na Macu a Linuxu použij `pip3`)

Tohle do tvého počítače nainstaluje Pythoní knihovnu Flask. Tenhle krok stačí udělat
jenom jednou, Flask zůstane v nainstalovaný napořád.

A teď už můžeš spustit tuhle aplikaci.

Na Windows v Powershellu:

    $env:FLASK_APP="main.py"
    flask run

Na Macu a Linuxu:

    FLASK_APP=main.py flask run

V terminálu by se mělo objevit něco jako:

     * Serving Flask app "main"
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Teď můžeš v prohlížeči otevřít tu adresu (http://127.0.0.1:5000) a všechno by mělo
fungovat. Až budeš chtít aplikaci ukončit, tak zmáčnki Ctrl+C (i na Macu  musíš fakt
zmáčknout Ctrl+C, ne Command+C).

