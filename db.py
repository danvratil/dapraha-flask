# Import SQLITE
import sqlite3

def tableExists(con, tableName):
    cur = con.cursor()
    # Zkus...
    try:
        # Ziskat pocet tabulek s nazvem 'tableName' ze specialni tabulky sqlite_master
        cur.execute("SELECT COUNT(*) FROM sqlite_master WHERE type=? AND name=?;", ('table', tableName))
    except sqlite3.Error as e:
        # Ooops, neco se nepovedlo, napis, kde je problem a skocni
        print("SQL Error: {0}".format(e))
        exit(1)
    r = cur.fetchone()
    # Vrat True, pokud SQL dotaz nasel prave jeden zaznam (tzn. tabulka 'tableName' existuje),
    # nebo False, pokud SQL dotaz nenasel nic (tzn. tabulka 'tableName' neexistuje)
    return r[0] == 1

def createMyTable(con):
    cur = con.cursor()
    # Zkus ...
    try:
        # Vytvorit tabulku mytable
        cur.execute("CREATE TABLE mytable (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(60), date DATETIME);")
    except sqlite3.Error as e:
        # Ooops, neco se nepovadlo, napis, kde je problem a skonci
        print("SQL Error: {0}".format(e))
        exit(1)


# Otevri nasi databazi
con = sqlite3.connect('mydb.sqlite')
# Ziskej kurzor, "ukazatel" do nasi databaze
cur = con.cursor()

# Zkontroluj, jestli tabulka uz existuje a kdyz ne, tak ji vytvor
if not tableExists(con, 'mytable'):
    createMyTable(con)

# Zeptej se na jmeno
name = input("Zadej jmeno: ")

# Zkus...
try:
    # Vloz do tabulky zadane jmeno a aktualni datum a cas
    cur.execute("INSERT INTO mytable (name, date) VALUES(?, datetime('now'));", (name,));
except sqlite3.Error as e:
    # Kdyz se to nepovede, tak vypis proc a skonci
    print("SQL Error: {0}".format(e))
    exit(1)

# Vsechno se povedlo, ukonci transakci a data fyzicky uloz do databaze (na disk)
con.commit()

# Vyber vsechny zaznamy z tabulky
res = cur.execute("SELECT id, name, date FROM mytable ORDER BY date DESC;")

# Vezmi jeden zaznam z 'res' (vysledku')
row = res.fetchone()
# Opakuj, dokud row neni None (prazdny)
while row != None:
    # Vypis jmeno a datum z aktualniho zaznamu
    print("ID: {id:<5} Name: {name:10} Date: {date}".format(id = row[0], name=row[1], date=row[2]))
    # Posun se na dalsi zaznam z tabulky
    row = res.fetchone()

# Ukonci spojeni s databazi a skonci
con.close()
