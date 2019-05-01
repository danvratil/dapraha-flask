== Soubory a složky v tomhle projektu ==

static - obsahuje statické dokumenty, které se nikdy nemění, jako obrázky, CSS 
         styly, JavaScripty atd.

templates - obsahuje HTML šablony, ze kterých se pak poskládá stránka, která se
            zobrazí uživateli

main.py - hlavní (spouštěcí) program našeho webíku - v něm se vytvoří Flask a
          zaregistrují se jednotlivé Blueprinty

names_bp.py - náš vlastní Blueprint pro stránku na zobrazování, vkládání a mazání
              jmen z databáze

about_bp.py - náš vlastní Blueprint pro stránku "O mě"

mydb.sqlite - SQLite datábáze, nad kterou spouštíme všechny naše SQL dotazy

schema.sql - popis, jak vytvořit v mydb.sqlite tu tabulku, kterou použiváme




== Instalace/spouštění ==

Nejprve ve složce s tímto projektem musíme vytvořit nové virtualní prostředí Pythonu.
Otevři terminál a pomocí příkazu "cd" se naviguj do složky, kde jsi tento projekt
rozbalila.

Nyní spusť

    python3 -m venv venv

Tím se vytvoří virtuální prostředí. Tento kroky už v budoucnu nebudeš muset opakovat,
pokud budeš chtít spustit tenhle program znovu.


Nyní aktivuj virtualní prostředí:

    source ./venv/scripts/activate

Na začátku příkazové řádky by se ti mělo objevit "venv", což znamená, že jsi nyní
ve virtulálním prostředí našeho projektu. Tenhle krok musíš udělat vždycky, když
budeš chtít spustit tenhle program.

Nyní nainstaluj Flask, abychom ho mohli použivat:

    pip3 install flask

Tohle do našeho virtuálního prostředí nainstaluje Flask. Tenhle krok stačí udělat
jenom jednou, Flask zůstane v tomto prostředí nainstalovaný napořád.

A teď už můžeš spustit tuhle aplikaci:

    FLASK_APP=main.py flask run

V terminálu by se mělo objevit něco jako:

 * Serving Flask app "main"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Teď můžeš v prohlížeči otevřít tu adresu (http://127.0.0.1:5000) a všechno by mělo
fungovat. Až budeš chtít aplikaci ukončit, tak zmáčnki Ctrl+C (myslím, že i na
Macku musíš fakt zmáčknout Ctrl+C, ne Command+C)

