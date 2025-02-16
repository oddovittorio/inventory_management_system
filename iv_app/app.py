from flask import Flask, render_template
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# MySQL-Konfiguration für die Verbindung mit der Datenbank `mydb`
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Dein MySQL-Benutzername
app.config['MYSQL_PASSWORD'] = '*******'  # Dein MySQL-Passwort
app.config['MYSQL_DB'] = 'mydb'  # Deine Datenbank aus MySQL Workbench
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Gibt Ergebnisse als Dictionary zurück

# Funktion für eine Datenbankverbindung
def get_db_connection():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/artikel')
def artikel():
    connection = get_db_connection()  # Verbindung zur DB aufbauen
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Artikel")  # Alle Artikel abrufen
        artikel_daten = cursor.fetchall()  # Ergebnisse speichern
    connection.close()  # Verbindung schließen
    return render_template("artikel.html", artikel=artikel_daten)

@app.route('/lagerorte')
def lagerorte():
    connection = get_db_connection()  # Verbindung zur DB aufbauen
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Lagerort")  # Alle Lagerorte abrufen
        lagerorte_daten = cursor.fetchall()  # Ergebnisse speichern
    connection.close()  # Verbindung schließen
    return render_template("lagerorte.html", lagerorte=lagerorte_daten)

if __name__ == '__main__':
    app.run(debug=True)
